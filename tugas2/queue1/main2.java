import java.utils.ArrayDeque;

public class antrian2 {
    public static void main(String[] args){
        ArrayDeque<String> daftar = new ArrayDeque<String>();
        daftar.add("Aminudin");
        daftar.add("Bahtiar Rivai");
        daftar.add("Cita Citata");
        daftar.add("Dul Sumbang");
        daftar.add("Engel Lelga");
        daftar.add("Farah Nurlaela");
        daftar.add("Galih");
        daftar.add("Herwantyoko");
        daftar.add("Indah Kusuma");

        System.out.println("Isi Antrian:");
        while(!daftar.isEmpty()){
            String nama = daftar.remove();
            System.out.println(nama)
        }
        }
    }
}