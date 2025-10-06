import {BrowserRouter as Router, Routes, Route, Navigate} from "react-router-dom";
import {useState, useEffect} from "react";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import Register from "./pages/Register";
import Index from "./pages/Index";

function App() {
    const getAuth = () => !!(localStorage.getItem("accessToken") || localStorage.getItem("access"));

    const [isAuthenticated, setIsAuthenticated] = useState(getAuth());

    // Listen to cross-tab storage changes
    useEffect(() => {
        const onStorage = (e) => {
            if (!e.key) {
                setIsAuthenticated(getAuth());
                return;
            }
            if (["accessToken", "access", "refreshToken", "refresh"].includes(e.key)) {
                setIsAuthenticated(getAuth());
            }
        };
        window.addEventListener("storage", onStorage);
        return () => window.removeEventListener("storage", onStorage);
    }, []);

    const handleLogin = (tokens) => {
        const access = tokens?.access ?? tokens?.accessToken ?? localStorage.getItem("accessToken") ?? localStorage.getItem("access");
        const refresh = tokens?.refresh ?? tokens?.refreshToken ?? localStorage.getItem("refreshToken") ?? localStorage.getItem("refresh");
        const username = tokens?.username ?? localStorage.getItem("userName");
        const email = tokens?.email ?? localStorage.getItem("userEmail");

        if (access) {
            localStorage.setItem("accessToken", access);
            localStorage.setItem("access", access);
        }
        if (refresh) {
            localStorage.setItem("refreshToken", refresh);
            localStorage.setItem("refresh", refresh);
        }
        if (username) localStorage.setItem("userName", username);
        if (email) localStorage.setItem("userEmail", email);

        setIsAuthenticated(true);
    };

    const handleLogout = () => {
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        localStorage.removeItem("userName");
        localStorage.removeItem("userEmail");
        setIsAuthenticated(false);
    };

    return (
        <Router>
            <Routes>
                {/* Login sayfası */}
                <Route path="/" element={<Index />} />
                <Route
                    path="/login"
                    element={
                        isAuthenticated ? (
                            <Navigate to="/profile" replace/>
                        ) : (
                            <Login onLogin={handleLogin}/>
                        )
                    }
                />
                {/* Register sayfası */}
                <Route
                    path="/register"
                    element={
                        isAuthenticated ? (
                            <Navigate to="/profile" replace/>
                        ) : (
                            <Register onRegister={handleLogin}/>
                        )
                    }
                />
                {/* Profile sayfası */}
                <Route
                    path="/profile"
                    element={
                        isAuthenticated ? (
                            <Profile onLogout={handleLogout}/>
                        ) : (
                            <Navigate to="/login" replace/>
                        )
                    }
                />
                {/* Fallback tüm bilinmeyen rotalar */}
                <Route path="*" element={<Navigate to="/" replace/>}/>
            </Routes>
        </Router>
    );
}

export default App;