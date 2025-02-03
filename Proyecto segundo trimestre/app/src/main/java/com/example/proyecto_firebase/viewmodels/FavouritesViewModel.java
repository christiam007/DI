package com.example.proyecto_firebase.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.proyecto_firebase.models.Pelicula;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import java.util.ArrayList;
import java.util.List;

public class FavouritesViewModel extends ViewModel {
    private MutableLiveData<List<Pelicula>> favoritos;
    private DatabaseReference favoritosRef;
    private DatabaseReference peliculasRef;
    private String userId;

    public FavouritesViewModel() {
        favoritos = new MutableLiveData<>(new ArrayList<>());
        userId = FirebaseAuth.getInstance().getCurrentUser().getUid();
        favoritosRef = FirebaseDatabase.getInstance().getReference()
                .child("usuarios")
                .child(userId)
                .child("favoritos");
        peliculasRef = FirebaseDatabase.getInstance().getReference().child("peliculas");
    }

    public LiveData<List<Pelicula>> getFavoritos() {
        return favoritos;
    }

    public void cargarFavoritos() {
        favoritosRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                List<Pelicula> listaFavoritos = new ArrayList<>();
                for (DataSnapshot favoritoSnapshot : dataSnapshot.getChildren()) {
                    String peliculaId = favoritoSnapshot.getKey();
                    cargarPeliculaFavorita(peliculaId, listaFavoritos);
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                // Manejar error
            }
        });
    }

    private void cargarPeliculaFavorita(String peliculaId, final List<Pelicula> listaFavoritos) {
        peliculasRef.child(peliculaId).addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                Pelicula pelicula = dataSnapshot.getValue(Pelicula.class);
                if (pelicula != null) {
                    listaFavoritos.add(pelicula);
                    favoritos.setValue(listaFavoritos);
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                // Manejar error
            }
        });
    }
}