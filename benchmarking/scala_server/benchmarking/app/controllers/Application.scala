package controllers

import play.api._
import play.api.mvc._

object Application extends Controller {
  
  def index = Action {
    Ok(views.html.index("Your new application is ready."))
  }
  
  def scalaserver(milliseconds: Int ) = Action {
  		Thread.sleep(milliseconds)
  		val msg = "Slept for " + {milliseconds.toString} + " milliseconds";
		Ok(msg)
	}
}