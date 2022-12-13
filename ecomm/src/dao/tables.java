/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dao;

import javax.swing.JOptionPane;

/**
 *
 * @author HP
 */
public class tables {
    public static void main(String[] args)
    {
        try{
           String userTable;
           userTable = "create table user(id int AUTO_INCREMENT primary key,name varchar(200),email varchar(200),mobileNumber varchar(10),address varchar(200),password varchar(200),securityQuestion varchar(200),answer varchar(200),status varchar(20))";
          
            // String adminDetails = "insert into user(name,email,mobileNumber,address,password,securityQuestion,answer,status) values('Admin','admin@gmail.com','123456789','india','admin','admin','admin','true')";
            String categoryTable = "create table category(id int AUTO_INCREMENT primary key,name varchar(200)";
            String productTable = "create table product(id int AUTO_INCREMENT primary key,name varchar(200),category varchar(200),price varchar(200)";
            
            dbOperations.setDataorDelete(userTable,"User Table created ");
            //dbOperations.setDataorDelete(adminDetails, "admin added");
            dbOperations.setDataorDelete(categoryTable,"Category Table created ");
            dbOperations.setDataorDelete(productTable,"Product Table created ");

        }
        catch(Exception e){
        JOptionPane.showMessageDialog(null, e);
        }
    }
}
