/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package dao;
import java.sql.*;
/**
 *
 * @author HP
 */
public class connectionProvider {
    public static Connection getcon(){
      try
       {
           Class.forName("com.mysql.cj.jdbc.Driver");
           
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/comm","root", "");
            System.out.print("Database is connected !");
            return con;
        }
        catch(ClassNotFoundException | SQLException e) {
            System.out.print("Do not connect to DB - Error:"+e);
        }
        return null;
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        // TODO code application logic here
    }
}
