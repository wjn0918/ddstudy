package com.example;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

/***
 * 反射demo
 */

public class UseReflect {


    public static void main(String[] args) {

        try {
            Class myReflect = Class.forName("com.example.MyReflect");
            String[] argv = new String[]{"123"};
            Method mainMethod = myReflect.getMethod("main", String[].class);
            mainMethod.invoke(null, (Object) argv);
        }
        catch (NoSuchMethodException e) {
            throw new RuntimeException(e);
        }
        catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
        catch (InvocationTargetException ite) {
        }
        catch (IllegalAccessException ite) {

        }


    }
}
