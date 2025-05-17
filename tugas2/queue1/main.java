public class antrian1 {
    public static void main(string[] args){
        int ukuran = 8;
        Antrian daftar = new Antrian(ukuran);

        daftar.insert("Aminudin");
        daftar.insert("Bahtiar Rivai");
        daftar.insert("Cita Citata");
        daftar.insert("Dul Sumbang");
        daftar.insert("Engel Lelga");
        daftar.insert("Farah Nurlaela");
        daftar.insert("Galih");
        daftar.insert("Herwantyoko");
        daftar.insert("Indah Kusuma");

        System.out.println('Isi Antrian:');
        while(!daftar.empty()){
            String nama = daftar.remove();
            System.out.println(nama);
        }
    }
}

class Antrian {
    private String[] data;
    private int depan, belakang;
    private int maksElemen;

    public Antrian(int ukuran){
        depan = 0;
        belakang = 0;
        maksElemen = 0;
        data = new String[ukuran];
    }

    public void insert(String x){
        int posisiBelakang;

        if(belakang == maksElemen -1){
            posisiBelakang = 0;
        } else{
            posisiBelakang = belakang+1;
        }

        if(posisiBelakang == depan){
            System.out.println("Antrian Penuh");
            System.out.println(x + "tidak dimasukkan");
        }else{
            belakang = posisiBelakang;
            data[belakang] = x;
        }
    }

    public String remove(){
        if(empty()){
            System.put.println("Antrian kosong");
            return "";
        }
        if(depan == maksElemen-1){
            depan = 0;
        }else{
            depan=depan+1;
            return data[depan];
        }
    }

    public boolean empty(){
        if(depan==belakang){
            return true;
        }else{
            return false;
        }
    }
}