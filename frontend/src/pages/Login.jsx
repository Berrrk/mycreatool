import {useState, useEffect} from "react";
import {useNavigate} from "react-router-dom";
import {loginUser} from "../api";

export default function Login({onLogin}) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    // Eğer zaten token varsa otomatik profile'a gönder
    useEffect(() => {
        const token = localStorage.getItem("accessToken") || localStorage.getItem("access");
        if (token) {
            navigate("/profile", {replace: true});
        }
    }, [navigate]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        try {
            const data = await loginUser({email, password});

            // data'dan tokenleri çek (esnek: access veya accessToken)
            const access = data?.access ?? data?.accessToken;
            const refresh = data?.refresh ?? data?.refreshToken;
            const username = data?.username ?? data?.user?.username;

            // localStorage'a yaz (hem accessToken hem access koyuyoruz uyumluluk için)
            if (access) {
                localStorage.setItem("accessToken", access);
                localStorage.setItem("access", access);
            }
            if (refresh) {
                localStorage.setItem("refreshToken", refresh);
                localStorage.setItem("refresh", refresh);
            }
            if (username) {
                localStorage.setItem("userName", username);
            }
            localStorage.setItem("userEmail", email);

            // App.jsx'e bildir (anında UI güncellemesi için)
            if (typeof onLogin === "function") {
                onLogin({access, refresh, username});
            }

            // yönlendir
            navigate("/profile", {replace: true});
        } catch (err) {
            // hata mesajı backend'den geliyorsa onu göstermeye çalış
            let message = "Email veya şifre hatalı";
            if (err?.message) message = err.message;
            setError(message);
        }
    };

    return (
        <>
            <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
                <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                    <img
                        alt="Your Company"
                        src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600"
                        className="mx-auto h-10 w-auto"
                    />
                    <h2 className="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">
                        Sign in to your account
                    </h2>
                </div>

                <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                    {error && <p className="text-red-500 mb-4">{error}</p>}
                    <form onSubmit={handleSubmit} className="space-y-6">
                        <div>
                            <label htmlFor="email" className="block text-sm/6 font-medium text-gray-900">
                                Email address
                            </label>
                            <div className="mt-2">
                                <input
                                    id="email"
                                    name="email"
                                    type="email"
                                    required
                                    autoComplete="email"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                />
                            </div>
                        </div>

                        <div>
                            <div className="flex items-center justify-between">
                                <label htmlFor="password" className="block text-sm/6 font-medium text-gray-900">
                                    Password
                                </label>
                                <div className="text-sm">
                                    <a href="#" className="font-semibold text-indigo-600 hover:text-indigo-500">
                                        Forgot password?
                                    </a>
                                </div>
                            </div>
                            <div className="mt-2">
                                <input
                                    id="password"
                                    name="password"
                                    type="password"
                                    required
                                    autoComplete="current-password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                />
                            </div>
                        </div>

                        <div>
                            <button
                                type="submit"
                                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                            >
                                Sign in
                            </button>
                        </div>
                    </form>

                    <p className="mt-10 text-center text-sm/6 text-gray-500">
                        Not a member?{" "}
                        <a href="/register" className="font-semibold text-indigo-600 hover:text-indigo-500">
                            Start a 14 day free trial
                        </a>
                    </p>
                </div>
            </div>
        </>
    );
}