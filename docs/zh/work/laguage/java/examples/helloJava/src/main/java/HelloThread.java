public class HelloThread extends Thread{


    @Override
    public synchronized void start(){
        super.start();
    }

    @Override
    public void run(){
        while (true){
            try {
                Thread.sleep(1000);
                String name = Thread.currentThread().getName();
                System.out.println(name + 1);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

}
