package com.example.proyecto_firebase.models;

public class Pelicula {
    private String titulo;
    private String descripcion;
    private String imagen;

    // Constructor vacío (requerido para Firebase)
    public Pelicula() {
    }

    // Constructor con todos los campos
    public Pelicula(String titulo, String descripcion, String imagen) {
        this.titulo = titulo;
        this.descripcion = descripcion;
        this.imagen = imagen;
    }

    // Getters y Setters
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getImagen() {
        return imagen;
    }

    public void setImagen(String imagen) {
        this.imagen = imagen;
    }
}



