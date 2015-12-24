defmodule PhoenixServer.PageController do
  use PhoenixServer.Web, :controller

  def index(conn, _params) do
    render conn, "index.html"
  end

  def response(conn, params) do
  	:timer.sleep(elem Integer.parse(params["time"]), 0)
  	text conn, params["time"]
  end
end
