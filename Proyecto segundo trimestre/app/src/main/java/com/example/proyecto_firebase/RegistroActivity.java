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
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;


public class RegistroActivity extends AppCompatActivity {

    EditText etNombre, etApellido, etCorreo, etContrasena, etConfirmContrasena, etTelefono, etDirrecion;
    Button btnRegistrar;


    TextView lblLoginR;
    FirebaseAuth firebaseAuth;
    private ProgressDialog progressDialog;


    String nombre = "", apellido = "", correo = "", contrasena = "", confirmarContrasena = "", telefono = "", direccion = "";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registro);

        //ID DE CONTROLES
        etNombre = findViewById(R.id.etNombre);
        etApellido = findViewById(R.id.etApellido);
        etCorreo = findViewById(R.id.etCorreo);
        etContrasena = findViewById(R.id.etContrasena);
        etConfirmContrasena = findViewById(R.id.etConfirmContrasena);
        etTelefono = findViewById(R.id.etTelefono);
        etDirrecion = findViewById(R.id.etDirrecion);
        btnRegistrar = findViewById(R.id.btnRgistrar);
        lblLoginR = findViewById(R.id.btnRgistrar);

        //Creacion de la Authenticacion
        firebaseAuth = FirebaseAuth.getInstance();

        //Progreso de Dialog se ejecute en Registro Activity
        progressDialog = new ProgressDialog(RegistroActivity.this);
        progressDialog.setTitle("Espere porfavor...");
        progressDialog.setCanceledOnTouchOutside(false);

        btnRegistrar.setOnClickListener(v -> validarDatos());


        lblLoginR = findViewById(R.id.lblLoginR);
        lblLoginR.setOnClickListener(view -> startActivity(new Intent(RegistroActivity.this, MainActivity.class)));

    }

    private void validarDatos() {
        nombre = etNombre.getText().toString();
        apellido = etApellido.getText().toString();
        correo = etCorreo.getText().toString();
        contrasena = etContrasena.getText().toString();
        confirmarContrasena = etConfirmContrasena.getText().toString();
        telefono = etTelefono.getText().toString();
        direccion = etDirrecion.getText().toString();

        if (TextUtils.isEmpty(nombre)) {
            Toast.makeText(this, "El campo esta Vacio", Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(apellido)) {
            Toast.makeText(this, "Ingrese Apellido", Toast.LENGTH_SHORT).show();
        } else if (!Patterns.EMAIL_ADDRESS.matcher(correo).matches()) {
            Toast.makeText(this, "Ingrese Correo Valido", Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(contrasena) || contrasena.length()<6) {
            Toast.makeText(this, "Ingrese Contraseña minimo 6 caracteres", Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(confirmarContrasena)) {
            Toast.makeText(this, "Ingrese Confirmar Contraseña minimo 6 caracteres", Toast.LENGTH_SHORT).show();
        }else if(!contrasena.equals(confirmarContrasena) || confirmarContrasena.length()<6){
            Toast.makeText(this, "Las contraseñas no coinciden", Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(telefono)) {
            Toast.makeText(this, "Ingrese Número de Teléfono", Toast.LENGTH_SHORT).show();
        } else if (telefono.length() < 9) {
            Toast.makeText(this, "El número de teléfono debe tener al menos 9 dígitos", Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(direccion)) {
            Toast.makeText(this, "Ingrese Dirección", Toast.LENGTH_SHORT).show();
        } else if (direccion.length() < 12) {
            Toast.makeText(this, "La dirección es demasiado corta", Toast.LENGTH_SHORT).show();
        }else {
            registrar();
        }

    }

    private void registrar() {
        progressDialog.setMessage("Registrando al Usuario");
        progressDialog.dismiss();

        firebaseAuth.createUserWithEmailAndPassword(correo,contrasena).
                addOnSuccessListener(authResult -> guardarUsuario()).addOnFailureListener(e -> Toast.makeText(RegistroActivity.this,"Ocurrio un problema, revisa los campos", Toast.LENGTH_SHORT).show());

    }

    private void guardarUsuario() {
        progressDialog.setMessage("Guardando Informacion");
        progressDialog.dismiss();

        String uid = firebaseAuth.getUid();
        HashMap<String , String> datosUsuario = new HashMap<>();
        datosUsuario.put("uid", uid);
        datosUsuario.put("nombre", nombre);
        datosUsuario.put("apellido",apellido);
        datosUsuario.put("correo", correo);
        datosUsuario.put("contrasena",contrasena);
        datosUsuario.put("telefono", telefono);
        datosUsuario.put("direccion", direccion);

        DatabaseReference databaseReference = FirebaseDatabase.getInstance().getReference("Usuarios");
        databaseReference.child(uid).setValue(datosUsuario).addOnSuccessListener(unused -> {
            progressDialog.dismiss();
            Toast.makeText(RegistroActivity.this,"Usuario Creado con Existo", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(RegistroActivity.this,DashboardActivity.class));
            finish();
        }).addOnFailureListener(e -> {
            progressDialog.dismiss();
            Toast.makeText(RegistroActivity.this,"Ocurrio un problema"+e.getMessage(), Toast.LENGTH_SHORT).show();
        });

    }
}