package com.example.proyecto_firebase.adapters;

import android.view.LayoutInflater;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.databinding.DataBindingUtil;
import androidx.recyclerview.widget.RecyclerView;
import com.example.proyecto_firebase.R;
import com.example.proyecto_firebase.databinding.ItemPeliculaBinding;
import com.example.proyecto_firebase.models.Pelicula;
import com.bumptech.glide.Glide;
import com.bumptech.glide.load.resource.drawable.DrawableTransitionOptions;
import java.util.List;


public class PeliculaAdapter extends RecyclerView.Adapter<PeliculaAdapter.PeliculaViewHolder> {
    private List<Pelicula> peliculas;
    private OnPeliculaClickListener clickListener;

    // Interfaz para el click listener
    public interface OnPeliculaClickListener {
        void onPeliculaClick(Pelicula pelicula);
    }

    public PeliculaAdapter(List<Pelicula> peliculas, OnPeliculaClickListener listener) {
        this.peliculas = peliculas;
        this.clickListener = listener;
    }

    public void setPeliculas(List<Pelicula> peliculas) {
        this.peliculas = peliculas;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public PeliculaViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        ItemPeliculaBinding binding = DataBindingUtil.inflate(
                LayoutInflater.from(parent.getContext()),
                R.layout.item_pelicula,
                parent,
                false
        );
        return new PeliculaViewHolder(binding);
    }

    @Override
    public void onBindViewHolder(@NonNull PeliculaViewHolder holder, int position) {
        Pelicula pelicula = peliculas.get(position);
        holder.bind(pelicula, clickListener);
    }

    @Override
    public int getItemCount() {
        return peliculas != null ? peliculas.size() : 0;
    }

    static class PeliculaViewHolder extends RecyclerView.ViewHolder {
        private final ItemPeliculaBinding binding;

        public PeliculaViewHolder(@NonNull ItemPeliculaBinding binding) {
            super(binding.getRoot());
            this.binding = binding;
        }

        public void bind(Pelicula pelicula, OnPeliculaClickListener listener) {
            binding.setPelicula(pelicula);

            // Configurar el click listener
            binding.getRoot().setOnClickListener(v -> {
                if (listener != null) {
                    listener.onPeliculaClick(pelicula);
                }
            });

            Glide.with(binding.getRoot().getContext())
                    .load(pelicula.getImagen())
                    .centerCrop()
                    .transition(DrawableTransitionOptions.withCrossFade())
                    .into(binding.ivPelicula);

            binding.executePendingBindings();
        }
    }
}

