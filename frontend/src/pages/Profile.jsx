import {useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";
import {fetchProfile} from "../api"; // senin api.js içinde fetchProfile olmalı

export default function Profile({onLogout}) {
    const [profile, setProfile] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        let mounted = true;

        const load = async () => {
            try {
                const data = await fetchProfile();
                if (!mounted) return;
                setProfile(data);
            } catch (err) {
                // Eğer fetch başarısızsa (token yok/expired), localStorage fallback veya yönlendir
                const username = localStorage.getItem("userName");
                const email = localStorage.getItem("userEmail");
                if (username || email) {
                    setProfile({username: username || "User", email: email || "—", credits: null});
                } else {
                    // tamamen başarısızsa logout işlemini tetikle
                    if (typeof onLogout === "function") onLogout();
                    localStorage.clear();
                    navigate("/", {replace: true});
                }
            }
        };

        load();
        return () => {
            mounted = false;
        };
    }, [navigate, onLogout]);

    const handleLogout = () => {
        if (typeof onLogout === "function") onLogout();
        else {
            localStorage.removeItem("accessToken");
            localStorage.removeItem("refreshToken");
            localStorage.removeItem("access");
            localStorage.removeItem("refresh");
            localStorage.removeItem("userName");
            localStorage.removeItem("userEmail");
        }
        navigate("/", {replace: true});
    };

    if (!profile) {
        return (
            <div className="flex items-center justify-center min-h-screen bg-gray-50">
                <div className="text-center">Loading profile...</div>
            </div>
        );
    }

    return (
        <div className="min-h-screen flex flex-col bg-gray-50">
            {/* Header */}
            <header className="bg-indigo-600 text-white py-6 px-6 lg:px-8 shadow-md">
                <div className="max-w-4xl mx-auto">
                    <h1 className="text-3xl font-bold">Welcome, {profile.username || localStorage.getItem("userName") || "User"}</h1>
                    <p className="text-sm mt-1">{profile.email}</p>
                </div>
            </header>

            {/* Main */}
            <main className="flex-1 flex items-center justify-center px-6 py-12 lg:px-8">
                <div className="w-full max-w-3xl bg-white rounded-md shadow-md p-8 space-y-6">
                    <h2 className="text-2xl font-bold text-gray-900">Profile Details</h2>

                    <div className="grid grid-cols-1 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700">Name</label>
                            <p className="mt-1 text-gray-900">{profile.username || localStorage.getItem("userName") || "User"}</p>
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">Email</label>
                            <p className="mt-1 text-gray-900">{profile.email}</p>
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700">Credits</label>
                            <p className="mt-1 text-gray-900">{profile.credits ?? "—"}</p>
                        </div>
                    </div>

                    <div>
                        <button
                            onClick={handleLogout}
                            className="w-full flex justify-center rounded-md bg-red-600 px-3 py-2 text-white font-semibold hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-600"
                        >
                            Logout
                        </button>
                    </div>
                </div>
            </main>

            <footer className="bg-gray-100 py-4 text-center text-gray-500 text-sm">
                © {new Date().getFullYear()} MyCreatool. All rights reserved.
            </footer>
        </div>
    );
}