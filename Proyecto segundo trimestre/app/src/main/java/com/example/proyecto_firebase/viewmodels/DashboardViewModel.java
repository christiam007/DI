package com.example.proyecto_firebase.viewmodels;

import androidx.annotation.NonNull;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.proyecto_firebase.models.Pelicula;
import com.example.proyecto_firebase.repositories.DashboardRepository;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;


public class DashboardViewModel extends ViewModel {
    private DashboardRepository dashboardRepository;
    private MutableLiveData<Boolean> navigateToLogin;
    private MutableLiveData<List<Pelicula>> peliculas; // Cambiado a lista
    private MutableLiveData<String> error;

    public DashboardViewModel() {
        dashboardRepository = new DashboardRepository();
        navigateToLogin = new MutableLiveData<>();
        peliculas = new MutableLiveData<>(new ArrayList<>()); // Inicializado con lista vacía
        error = new MutableLiveData<>();
    }

    public LiveData<Boolean> getNavigateToLogin() {
        return navigateToLogin;
    }

    public LiveData<List<Pelicula>> getPeliculas() { // Método actualizado
        return peliculas;
    }

    public LiveData<String> getError() {
        return error;
    }

    public void cerrarSesion() {
        dashboardRepository.signOut();
        navigateToLogin.setValue(true);
    }

    public void cargarPeliculas() { // Método actualizado para cargar todas las películas
        dashboardRepository.getPeliculas(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                List<Pelicula> listaPeliculas = new ArrayList<>();

                for (DataSnapshot peliculaSnapshot : dataSnapshot.getChildren()) {
                    String titulo = peliculaSnapshot.child("titulo").getValue(String.class);
                    String descripcion = peliculaSnapshot.child("descripcion").getValue(String.class);
                    String imagen = peliculaSnapshot.child("imagen").getValue(String.class);

                    Pelicula pelicula = new Pelicula();
                    pelicula.setTitulo(titulo);
                    pelicula.setDescripcion(descripcion);
                    pelicula.setImagen(imagen);

                    listaPeliculas.add(pelicula);
                }

                peliculas.setValue(listaPeliculas);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {
                error.setValue("Error al cargar las películas: " + databaseError.getMessage());
            }
        });
    }
}