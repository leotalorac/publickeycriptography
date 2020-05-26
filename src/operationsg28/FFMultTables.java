public class FFMultTables {
   public byte[] E = new byte[256];
   public byte[] L = new byte[256];
   private String[] dig = {"0","1","2","3","4","5","6","7",
                           "8","9","a","b","c","d","e","f"};
   public byte FFMul(byte a, byte b) {
      byte aa = a, bb = b, r = 0, t;
      while (aa != 0) {
         if ((aa & 1) != 0)
            r = (byte)(r ^ bb);
         t = (byte)(bb & 0x80);
         bb = (byte)(bb << 1);
         if (t != 0)
            bb = (byte)(bb ^ 0x1b);
         aa = (byte)((aa & 0xff) >> 1); 
      }
      return r;
   }

   public String hex(byte a) {
      return dig[(a & 0xff) >> 4] + dig[a & 0x0f];
   }

   public String hex(int a) {
      return dig[a];
   }

   public void loadE() {
      byte x = (byte)0x01;
      int index = 0;
      E[index++] = (byte)0x01;
      for (int i = 0; i < 255; i++) {
         byte y = FFMul(x, (byte)0x03);
         E[index++] = y;
         // System.out.print(hex(y) + " ");
         x = y;
      }
   }

   public void loadL() {
      int index;
      for (int i = 0; i < 255; i++) {
          L[E[i] & 0xff] = (byte)i;
      }
   }

   public void printE() {
      System.out.println("E table");
      System.out.println("[");
      for (int i = 0; i < 256; i++) {
         if(i%16==0)
            System.out.print("[");
         if(i%16 != 15)
            System.out.print("'"+hex(E[i]) + "',");
         else
            System.out.println("'"+hex(E[i])+ "'],");
      }
      System.out.println("]");
   }

   public void printL() {
      System.out.println("L table");
      System.out.println("[");
      for (int i = 0; i < 256; i++) {
         if(i%16==0)
            System.out.print("[");
         if (i == 0)
            System.out.print("'',");
         else{
            if(i%16 != 15)
               System.out.print( "'"+hex(L[i]) + "',");
            else
               System.out.println("'"+hex(L[i]) +"'],");
         }
         
      }
      System.out.println("]");
   }

   public static void main(String[] args) {
      FFMultTables ffm = new FFMultTables();
      ffm.loadE();
      ffm.loadL();
      ffm.printL();
      ffm.printE();
   }
}
