/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tcc;

import com.jcraft.jsch.JSchException;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import ssh.SSHUtils;
import ssh.ShellConnectionStream;

/**
 *
 * @author ramires
 */
public class TCC {
    private static String usuario = "pi";
    private static String senha = "ramires2313";
    private static String host = "192.168.11.7";
    private static int porta = 22;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws JSchException, IOException, InterruptedException {
        // TODO code application logic here
        System.out.println("");
        //SSHUtils.makeDir(usuario, senha, host, porta, "/home/pi/Desktop/TESTANDO/");
        //boolean res = SSHUtils.downloadFile(usuario, senha, host, porta, "/home/pi/Desktop/User.txt","/home/ramires/Desktop/User.txt");
        //System.out.println(res);
        
        ShellConnectionStream ssh = ShellConnectionStream.builder()
            .username(usuario)
            .password(senha)
            .host(host)
            .port(porta)
            .build();
        
        ssh.connect();
        String cmd = "scp -r pi@192.168.11.7:/home/pi/Desktop/Mensagens /home/ramires/Desktop";
        //String resultado = ssh.write(cmd);
        //System.out.println(resultado);
        Process proc = Runtime.getRuntime().exec(cmd);
        
        BufferedReader reader = new BufferedReader(new InputStreamReader(proc.getInputStream()));
        String line = "";
        while((line = reader.readLine()) != null) {
            System.out.print(line + "\n");
        }
        
        proc.waitFor(); 
        ssh.close();
    }
}
