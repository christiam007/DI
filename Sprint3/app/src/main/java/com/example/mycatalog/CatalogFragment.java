package com.example.mycatalog;



import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;


public class CatalogFragment extends Fragment {


    public CatalogFragment() {
        // Required empty public constructor
    }

    public static CatalogFragment newInstance() {  // Método corregido
        return new CatalogFragment();
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_catalog, container, false);
        Button button = view.findViewById(R.id.naviFragment);
        button.setOnClickListener(v-> {
                    Intent intent = new Intent(requireContext(), DetailActivity.class);
                    startActivity(intent);
                }
        );

        return view;
    }
}