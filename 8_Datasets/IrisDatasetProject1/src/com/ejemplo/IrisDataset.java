package com.ejemplo;

import java.io.*;
import java.util.ArrayList;

public class IrisDataset {
    public static void main(String[] args) {
        // Ruta del archivo en el proyecto
        String fileName = "bezdekIris.data";
        ArrayList<ArrayList<Float>> data = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.trim().isEmpty()) {
                    System.out.println("Línea vacía encontrada y omitida.");
                    continue;
                }

                String[] values = line.split(",");
                if (values.length < 4) {
                    System.out.println("Línea con valores insuficientes encontrada y omitida: " + line);
                    continue;
                }

                ArrayList<Float> row = new ArrayList<>();
                for (int i = 0; i < 4; i++) {
                    if (!values[i].trim().isEmpty()) {
                        try {
                            row.add(Float.parseFloat(values[i].trim()));
                        } catch (NumberFormatException e) {
                            System.out.println("Error al parsear el valor: " + values[i]);
                        }
                    } else {
                        System.out.println("Valor vacío encontrado en la línea: " + line);
                    }
                }
                data.add(row);
            }
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        }

        // Verificación: Imprime las primeras 5 filas
        for (int i = 0; i < 5 && i < data.size(); i++) {
            System.out.println(data.get(i));
        }
    }
}