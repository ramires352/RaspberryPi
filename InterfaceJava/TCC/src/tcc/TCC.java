/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tcc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import ssh.ShellConnectionStream;
import view.TelaLogin;

/**
 *
 * @author ramires
 */
public class TCC {
    public static ShellConnectionStream ssh;

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     * @throws java.lang.InterruptedException
     */
    public static void main(String[] args) throws IOException, InterruptedException{
        new TelaLogin().setVisible(true);
        
        //String cmd = "scp -r pi@192.168.11.7:/home/pi/Desktop/Mensagens /home/ramires/Desktop";
        //String resultado = ssh.write(cmd);
        //System.out.println(resultado);
        /*Process proc = Runtime.getRuntime().exec(cmd);
        
        BufferedReader reader = new BufferedReader(new InputStreamReader(proc.getInputStream()));
        String line = "";
        while((line = reader.readLine()) != null) {
            System.out.print(line + "\n");
        }
        
        proc.waitFor(); 
        ssh.close();*/
    }
}
