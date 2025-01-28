package com.example.proyecto_firebase.views;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import androidx.databinding.DataBindingUtil;

import com.bumptech.glide.Glide;
import com.example.proyecto_firebase.R;
import com.example.proyecto_firebase.databinding.ActivityDetailBinding;
import com.example.proyecto_firebase.models.Pelicula;

public class DetailActivity extends AppCompatActivity {

    private ActivityDetailBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_detail);

        // Obtener datos del Intent
        Pelicula pelicula = new Pelicula();
        pelicula.setTitulo(getIntent().getStringExtra("titulo"));
        pelicula.setDescripcion(getIntent().getStringExtra("descripcion"));
        pelicula.setImagen(getIntent().getStringExtra("imagen"));

        // Establecer los datos en el binding
        binding.setPelicula(pelicula);

        // Cargar la imagen con Glide
        Glide.with(this)
                .load(pelicula.getImagen())
                .centerCrop()
                .into(binding.ivPeliculaDetalle);
    }
}