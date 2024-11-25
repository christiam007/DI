package com.example.mycatalog;
import android.widget.ImageView;

import android.os.Bundle;

import com.bumptech.glide.Glide;
import com.bumptech.glide.request.RequestOptions;
import android.widget.ImageView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_detail);
        ImageView productImageView = findViewById(R.id.productImageView);
        Glide.with(this)
                .load("https://es.chessbase.com/thumb/2540")
                .apply(RequestOptions.circleCropTransform()) // Recorte circular
                .into(productImageView);

    }
}