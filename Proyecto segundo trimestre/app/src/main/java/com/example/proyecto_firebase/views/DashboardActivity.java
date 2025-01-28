
package com.example.proyecto_firebase.views;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.proyecto_firebase.R;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class DashboardActivity extends AppCompatActivity {
    Button btnCerrarSesion;
    FirebaseAuth firebaseAuth;
    FirebaseUser firebaseUser;
    DatabaseReference databaseReference;
    TextView tvTitulo, tvDescripcion;
    ImageView ivPelicula;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        // Inicializar Firebase
        firebaseAuth = FirebaseAuth.getInstance();
        firebaseUser = firebaseAuth.getCurrentUser();
        databaseReference = FirebaseDatabase.getInstance().getReference().child("peliculas");

        // Inicializar vistas
        btnCerrarSesion = findViewById(R.id.btnCerrarSesion);
        tvTitulo = findViewById(R.id.tvTitulo);
        tvDescripcion = findViewById(R.id.tvDescripcion);
        ivPelicula = findViewById(R.id.ivPelicula);

        // Cargar datos desde Firebase
        cargarPelicula();

        btnCerrarSesion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cierreSesion();
            }
        });
    }

    private void cargarPelicula() {
        // Obtener solo el primer elemento
        DatabaseReference databaseReference = FirebaseDatabase.getInstance().getReference("peliculas").child("2");
        Log.d("firebase", databaseReference.getDatabase().toString());


        ValueEventListener userListener = new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                // Obtener los datos
                String titulo = dataSnapshot.child("titulo").getValue(String.class);
                String descripcion = dataSnapshot.child("descripcion").getValue(String.class);
                String imageUrl = dataSnapshot.child("imagen").getValue(String.class);

                // Mostrar los datos en la UI
                tvTitulo.setText(titulo);
                tvDescripcion.setText(descripcion);


                // Cargar imagen usando Glide
                Glide.with(DashboardActivity.this)
                        .load(imageUrl)
                        .into(ivPelicula);
            }


            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {
                Log.w("Firebase", "Error al leer datos", databaseError.toException());
            }
        };

        databaseReference.addListenerForSingleValueEvent(userListener);


    }

    private void cierreSesion() {
        firebaseAuth.signOut();
        startActivity(new Intent(DashboardActivity.this, MainActivity.class));
        Toast.makeText(this, "Cerraste Sesion Exitosamente", Toast.LENGTH_SHORT).show();
        finish();
    }
}