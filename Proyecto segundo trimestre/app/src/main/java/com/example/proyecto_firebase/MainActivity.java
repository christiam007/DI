package com.example.proyecto_firebase;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Patterns;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

import java.util.Objects;


public class MainActivity extends AppCompatActivity {

    EditText etCorreoL, etContrasenaL;

    Button btnIngresarL;

    TextView lblRegistrar;

    ProgressDialog progressDialog;
    FirebaseAuth firebaseAuth;

    String correo ="", contrasena = "";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etCorreoL = findViewById(R.id.etCorreoL);
        etContrasenaL = findViewById(R.id.etContrasenaL);
        btnIngresarL = findViewById(R.id.btnIngresarL);

        firebaseAuth = FirebaseAuth.getInstance();

        progressDialog = new ProgressDialog(MainActivity.this);
        progressDialog.setTitle("Espere por favor...");
        progressDialog.setCanceledOnTouchOutside(false);

        btnIngresarL.setOnClickListener(v -> validarDatos());


        lblRegistrar = findViewById(R.id.lblRegistrar);
        lblRegistrar.setOnClickListener(view -> startActivity(new Intent(MainActivity.this,RegistroActivity.class)));
    }

    private void validarDatos() {
        correo = etCorreoL.getText().toString();
        contrasena = etContrasenaL.getText().toString();

        if(!Patterns.EMAIL_ADDRESS.matcher(correo).matches()){
            Toast.makeText(this,"Ingrese correo Valido", Toast.LENGTH_SHORT).show();

        } else if (TextUtils.isEmpty(contrasena)) {
            Toast.makeText(this,"Ingrese Contraseña", Toast.LENGTH_SHORT).show();

        }else{
            logearUsuario();
        }
    }

    private void logearUsuario() {
        progressDialog.setMessage("Iniciando Session...");
        progressDialog.show();

        firebaseAuth.signInWithEmailAndPassword(correo, contrasena)
                .addOnCompleteListener(MainActivity.this, task -> {
                    if(task.isSuccessful()){
                        progressDialog.dismiss();
                        FirebaseUser firebaseUser = firebaseAuth.getCurrentUser();
                        startActivity(new Intent(MainActivity.this, DashboardActivity.class));
                        Toast.makeText(MainActivity.this,"Bienvenido(a): " + Objects.requireNonNull(firebaseUser).getEmail(),Toast.LENGTH_LONG).show();
                        finish();
                    }else{
                        progressDialog.dismiss();
                        Toast.makeText(MainActivity.this,"Verifique si el correo o contraseña son los Correctos...", Toast.LENGTH_SHORT).show();
                    }
                }).addOnFailureListener(e -> {

                });

    }
}
