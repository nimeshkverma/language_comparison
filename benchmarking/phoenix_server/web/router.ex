defmodule PhoenixServer.Router do
  use PhoenixServer.Web, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", PhoenixServer do
    pipe_through :browser # Use the default browser stack

    get "/", PageController, :index
    get "/response", PageController, :response
    get "/crud", PageController, :crud
  end

  # Other scopes may use custom stacks.
  # scope "/api", PhoenixServer do
  #   pipe_through :api
  # end
end
