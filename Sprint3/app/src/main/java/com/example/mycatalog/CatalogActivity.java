package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class CatalogActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);

        // Encuentra el botón
        Button btnLaunchDetail = findViewById(R.id.detalleButton);

        // Configura el listener de clics
        btnLaunchDetail.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Lanza la actividad DetailActivity
                Intent intent = new Intent(CatalogActivity.this, DetailActivity.class);
                startActivity(intent);
            }
        });
    }
}