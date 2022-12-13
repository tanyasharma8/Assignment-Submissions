/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dao;
import java.util.ArrayList;
import javax.swing.JOptionPane;
import model.Category;
import java.sql.*;
/**
 *
 * @author tstan
 */
public class CategoryDao {
    public static void save(Category category){
       String query = "insert into category (name) values('"+category.getName()+"')";
       dbOperations.setDataorDelete(query,"Category Added Successfully");
    }
    
    public static ArrayList<Category> getAllRecords(){
        ArrayList<Category> arrayList = new ArrayList<>();
        try{
            ResultSet rs = dbOperations.getData("select * from category");
            while(rs.next()){
                Category category = new Category();
                category.setId(rs.getInt("id"));
                category.setName(rs.getString("name"));
                arrayList.add(category);
            }
        }
        catch(Exception e){
            JOptionPane.showMessageDialog(null, e, title, 0);
        }
        return arrayList;
    }
    
    public static void delete(String id){
        String query = "delete from category where id='"+id+"'";
        dbOperations.setDataorDelete(query,"Category Deleted Successfully");
                }
    
}
