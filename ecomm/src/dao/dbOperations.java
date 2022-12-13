/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dao;
import java.awt.HeadlessException;
import java.sql.*;
import javax.swing.JOptionPane;

/**
 *
 * @author HP
 */
public class dbOperations {
    public static void setDataorDelete(String Query,String msg)
    {
    try{
        Connection con = connectionProvider.getcon();
       
           Statement st=con.createStatement();
           
           st.executeUpdate(Query);
           System.out.println("table created");
           if(!msg.equals(""))
               {
                   JOptionPane.showMessageDialog(null, msg);
           }
    }
    catch(HeadlessException | SQLException e){
        JOptionPane.showMessageDialog(null,e,"message",JOptionPane.ERROR_MESSAGE);
    }
    
    }
    public static ResultSet getData(String query){
        try{
         Connection con = connectionProvider.getcon();
       
           Statement st=con.createStatement();
           ResultSet rs = st.executeQuery(query);
           return rs;
        }
        catch(SQLException e){
            JOptionPane.showMessageDialog(null,e,"message",JOptionPane.ERROR_MESSAGE);
            return null;
        
    }
    }
}
