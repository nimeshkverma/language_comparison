package controllers

import play.api._
import play.api.mvc._
import play.api.db._
import play.api.Play.current
import anorm._ 

object Application extends Controller {

  def index = Action {
    Ok(views.html.index("Your new application is ready."))
  }
  
  def scalaserver(milliseconds: Int ) = Action {
  		Thread.sleep(milliseconds)
  		val msg = "Slept for " + {milliseconds.toString} + " milliseconds";
		Ok(msg)
	}
  def crud() = Action {
  		DB.withConnection { 
  			implicit c =>
  			val qcreate: Boolean = SQL("INSERT INTO data_source(primary_id, data_int, data_string) VALUES(100,100,'Go Go Go');").execute()
  			val qread: Boolean = SQL("SELECT * from data_source;").execute()
  			val qupdate: Int = SQL("UPDATE data_source set data_string='GoGoGo' where data_int=100;").executeUpdate()
  			val qdelete: Int = SQL("DELETE from data_source where data_int=100;").executeUpdate()
	}
	val msg = "Performed CRUD operations"
	Ok(msg) 
  }

}