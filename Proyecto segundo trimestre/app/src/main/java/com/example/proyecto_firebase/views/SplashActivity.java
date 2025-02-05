package com.example.proyecto_firebase.views;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import com.example.proyecto_firebase.R;
import com.example.proyecto_firebase.utils.ThemeHelper;
import com.example.proyecto_firebase.repositories.UserRepository;
import com.google.firebase.auth.FirebaseUser;

public class SplashActivity extends AppCompatActivity {
    private UserRepository userRepository;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Aplicar tema antes de crear la activity
        if (ThemeHelper.isDarkMode(this)) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        userRepository = new UserRepository();

        new Handler().postDelayed(() -> {
            // Verificar si hay un usuario autenticado
            FirebaseUser currentUser = userRepository.obtenerUsuarioActual();

            Intent intent;
            if (currentUser != null) {
                // Si hay usuario autenticado, ir al Dashboard
                intent = new Intent(SplashActivity.this, DashboardActivity.class);
            } else {
                // Si no hay usuario autenticado, ir al Login
                intent = new Intent(SplashActivity.this, LoginActivity.class);
            }

            startActivity(intent);
            finish();
        }, 2000); // 2 segundos de splash
    }
}