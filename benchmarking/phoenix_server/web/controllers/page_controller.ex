defmodule PhoenixServer.PageController do
  use PhoenixServer.Web, :controller

  def index(conn, _params) do
    render conn, "index.html"
  end

  def response(conn, params) do
  	:timer.sleep(elem Integer.parse(params["time"]), 0)
  	text conn, params["time"]
  end

  def crud(conn, params) do
  	{:ok, pid} = Postgrex.Connection.start_link(hostname: "host_ip", username: "test1", password: "mypassword", database: "testdb")
  	Postgrex.Connection.query!(pid, "INSERT INTO data_source(primary_id, data_int, data_string) VALUES(100,100,'Go Go Go');", [])
  	Postgrex.Connection.query!(pid, "SELECT data_int FROM data_source", [])
  	Postgrex.Connection.query!(pid, "UPDATE data_source set data_string='GoGoGo' where data_int=100;", [])
  	Postgrex.Connection.query!(pid, "DELETE from data_source where data_int=100;", [])
  	text conn, params["time"]
  end
end
