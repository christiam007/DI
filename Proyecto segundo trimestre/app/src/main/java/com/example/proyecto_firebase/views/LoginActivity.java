package com.example.proyecto_firebase.views;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;

import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import com.example.proyecto_firebase.R;
import com.example.proyecto_firebase.viewmodels.LoginViewModel;


public class LoginActivity extends AppCompatActivity {
    private EditText etCorreoL, etContrasenaL;
    private Button btnIngresarL;
    private TextView lblRegistrar;
    private ProgressDialog dialogoProgreso;
    private LoginViewModel loginViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_main);
        inicializarVistas();
        configurarViewModel();
        configurarObservadores();
        configurarClickListeners();
    }

    private void inicializarVistas() {
        etCorreoL = findViewById(R.id.etCorreoL);
        etContrasenaL = findViewById(R.id.etContrasenaL);
        btnIngresarL = findViewById(R.id.btnIngresarL);
        lblRegistrar = findViewById(R.id.lblRegistrar);

        // Inicializar DialogoProgreso
        dialogoProgreso = new ProgressDialog(this);
        dialogoProgreso.setMessage("Iniciando sesión...");
        dialogoProgreso.setCancelable(false);
    }

    private void configurarViewModel() {
        loginViewModel = new ViewModelProvider(this).get(LoginViewModel.class);
    }

    private void configurarObservadores() {
        // Observar resultado del login
        loginViewModel.getLoginResult().observe(this, usuarioFirebase -> {
            dialogoProgreso.dismiss();
            if (usuarioFirebase != null) {
                // Login exitoso
                startActivity(new Intent(LoginActivity.this, DashboardActivity.class)); // Cambiar a DashboardActivity
                finish();
            }
        });

        // Observar errores
        loginViewModel.getLoginError().observe(this, error -> {
            dialogoProgreso.dismiss();
            if (error != null) {
                Toast.makeText(LoginActivity.this, error, Toast.LENGTH_SHORT).show();
            }
        });

        // Observar estado de carga
        loginViewModel.getIsLoading().observe(this, estaCargando -> {
            if (estaCargando != null) {
                if (estaCargando) {
                    dialogoProgreso.show();
                } else {
                    dialogoProgreso.dismiss();
                }
            }
        });
    }

    private void configurarClickListeners() {
        btnIngresarL.setOnClickListener(v -> intentarLogin());

        lblRegistrar.setOnClickListener(v -> {
            startActivity(new Intent(LoginActivity.this, RegisterActivity.class));
        });
    }

    private void intentarLogin() {
        String correo = etCorreoL.getText().toString().trim();
        String contrasena = etContrasenaL.getText().toString().trim();
        loginViewModel.login(correo, contrasena);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (dialogoProgreso != null && dialogoProgreso.isShowing()) {
            dialogoProgreso.dismiss();
        }
    }
}
