package com.example;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.TimeUnit;

public class HelloThread {
    public static final long PRE_READ_MS = 5000;
    private volatile boolean scheduleThreadToStop = false;

    private static Logger logger = LoggerFactory.getLogger(HelloThread.class);

    public static void main(String[] args) {
        new HelloThread().start();
    }

    public void start(){
        Thread scanJobInfo = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    TimeUnit.MILLISECONDS.sleep(5000 - System.currentTimeMillis() % 1000);
                } catch (InterruptedException e) {
                    if (!scheduleThreadToStop) {
                        logger.error(e.getMessage(), e);
                    }
                }
                logger.info(">>>>>>>>> init datax-web admin scheduler success.");
                while (!scheduleThreadToStop) {
                    try {
                        TimeUnit.MILLISECONDS.sleep(PRE_READ_MS);
                        System.out.println("scan job info");
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }

                };

            }
        });

        scanJobInfo.start();


        Thread scanJobInfo2 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    TimeUnit.MILLISECONDS.sleep(5000 - System.currentTimeMillis() % 1000);
                } catch (InterruptedException e) {
                    if (!scheduleThreadToStop) {
                        logger.error(e.getMessage(), e);
                    }
                }
                logger.info(">>>>>>>>> init datax-web admin scheduler success2.");
                while (!scheduleThreadToStop) {
                    try {
                        TimeUnit.MILLISECONDS.sleep(PRE_READ_MS);
                        System.out.println("scan job info2");
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }

                };

            }
        });

        scanJobInfo2.start();
    }



}
