package com.example.proyecto_firebase.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class DetailViewModel extends ViewModel {
    private MutableLiveData<Boolean> esFavorito;
    private DatabaseReference favoritosRef;
    private String peliculaId;
    private String userId;

    public DetailViewModel() {
        esFavorito = new MutableLiveData<>(false);
        userId = FirebaseAuth.getInstance().getCurrentUser().getUid();
        favoritosRef = FirebaseDatabase.getInstance().getReference()
                .child("usuarios")
                .child(userId)
                .child("favoritos");
    }

    public void setPeliculaId(String titulo) {
        this.peliculaId = titulo; // Usando el título como ID por ahora
        verificarSiEsFavorito();
    }

    public LiveData<Boolean> getEsFavorito() {
        return esFavorito;
    }

    private void verificarSiEsFavorito() {
        favoritosRef.child(peliculaId).addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                esFavorito.setValue(dataSnapshot.exists());
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                // Manejar error
            }
        });
    }

    public void toggleFavorito() {
        Boolean favorito = esFavorito.getValue();
        if (favorito != null) {
            if (favorito) {
                // Eliminar de favoritos
                favoritosRef.child(peliculaId).removeValue();
            } else {
                // Agregar a favoritos
                favoritosRef.child(peliculaId).setValue(true);
            }
        }
    }
}