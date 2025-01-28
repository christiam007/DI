package com.example.proyecto_firebase.repositories;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class PeliculaRepository {
    private DatabaseReference databaseReference;

    public PeliculaRepository() {
        databaseReference = FirebaseDatabase.getInstance().getReference().child("peliculas");
    }

    public void getPelicula(String peliculaId, ValueEventListener listener) {
        databaseReference.child(peliculaId).addListenerForSingleValueEvent(listener);
    }

    public void getAllPeliculas(ValueEventListener listener) {
        databaseReference.addListenerForSingleValueEvent(listener);
    }
}

