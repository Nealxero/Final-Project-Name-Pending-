import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "../styles/navbar.css"; // the import here was ./home.css
import "../styles/index.css";
import "../styles/searchbar.css";
import injectContext from "./store/appContext";
import Dashboard from "./pages/dashboard.jsx";
import RecipeSearch from "./pages/recipesearch.jsx";
import Favorites from "./pages/favorites.jsx";
import Sidebar from "./component/sidebar.jsx";
import Account from "./pages/account.jsx"; // this wasn't here
import Logout from "./pages/logout.jsx";
import ScrollToTop from "./component/scrollToTop";
import { Login } from "./pages/login";
import { SignUp } from "./pages/signup";
import { ForgotPassword } from "./pages/forgot";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  return (
    <div>
      <BrowserRouter basename={basename}>
        <ScrollToTop>
          <div>
          <Sidebar>
            <Routes>
              <Route path="/" element={<Dashboard/>} />
              <Route path="/dashboard" element={<Dashboard/>} />
              <Route path="/recipesearch" element={<RecipeSearch />} />
              <Route path="/favorites" element={<Favorites />} />
              <Route path="/account" element={<Account/>} />
              <Route element={<Logout />} path="/logout"  />
              <Route element={<Login />} path="/login" />
              <Route element={<ForgotPassword />} path="/forgotpassword" />
              <Route element={<SignUp />} path="/signup" />
              <Route element={<h1>Not found!</h1>} />
            </Routes>
          </Sidebar>
          </div>
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

// code
export default injectContext(Layout);
