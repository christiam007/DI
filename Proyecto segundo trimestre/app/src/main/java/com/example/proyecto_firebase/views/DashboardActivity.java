
package com.example.proyecto_firebase.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.proyecto_firebase.views.DetailActivity;
//import com.example.proyecto_firebase.DetailActivity;
import com.example.proyecto_firebase.R;

import com.example.proyecto_firebase.databinding.ActivityDashboardBinding;
import com.example.proyecto_firebase.adapters.PeliculaAdapter;
import com.example.proyecto_firebase.models.Pelicula;
import com.example.proyecto_firebase.viewmodels.DashboardViewModel;

import java.util.ArrayList;
import java.util.List;


import java.util.ArrayList;
import java.util.List;
public class DashboardActivity extends AppCompatActivity implements PeliculaAdapter.OnPeliculaClickListener {
    private ActivityDashboardBinding binding;
    private DashboardViewModel dashboardViewModel;
    private PeliculaAdapter peliculaAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this, R.layout.activity_dashboard);
        binding.setLifecycleOwner(this);

        // Inicializar ViewModel
        dashboardViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        // Configurar RecyclerView
        setupRecyclerView();

        // Observar cambios en los datos
        observeViewModel();

        // Configurar listeners
        setupListeners();

        // Cargar datos
        dashboardViewModel.cargarPeliculas();
    }

    private void setupRecyclerView() {
        peliculaAdapter = new PeliculaAdapter(new ArrayList<>(), this); // Pasar this como listener
        binding.recyclerViewPeliculas.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerViewPeliculas.setAdapter(peliculaAdapter);
    }

    private void observeViewModel() {
        dashboardViewModel.getPeliculas().observe(this, new Observer<List<Pelicula>>() {
            @Override
            public void onChanged(List<Pelicula> peliculas) {
                if (peliculas != null) {
                    peliculaAdapter.setPeliculas(peliculas);
                }
            }
        });

        dashboardViewModel.getNavigateToLogin().observe(this, shouldNavigate -> {
            if (shouldNavigate) {
                startActivity(new Intent(DashboardActivity.this, LoginActivity.class));
                finish();
            }
        });
    }

    private void setupListeners() {
        binding.btnCerrarSesion.setOnClickListener(v -> {
            dashboardViewModel.cerrarSesion();
            Toast.makeText(this, "Cerraste Sesión Exitosamente", Toast.LENGTH_SHORT).show();
        });
    }

    @Override
    public void onPeliculaClick(Pelicula pelicula) {
        // Navegar a DetailActivity cuando se hace click en una película
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("titulo", pelicula.getTitulo());
        intent.putExtra("descripcion", pelicula.getDescripcion());
        intent.putExtra("imagen", pelicula.getImagen());
        startActivity(intent);
    }
}