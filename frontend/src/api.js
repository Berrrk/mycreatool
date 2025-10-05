const API_URL = "http://127.0.0.1:8000/api/accounts/";

// Kullanıcı giriş
export const loginUser = async (data) => {
    const res = await fetch(`${API_URL}login/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });

    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(
            err?.detail ||
            err?.non_field_errors?.[0] ||
            "Login failed"
        );
    }

    const result = await res.json();
    localStorage.setItem("access", result.access);
    localStorage.setItem("refresh", result.refresh);
    localStorage.setItem("username", result.username);

    return result;
};

// Kullanıcı kayıt
export const registerUser = async (data) => {
    const res = await fetch(`${API_URL}register/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });

    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        // Backend'ten gelen olası hata alanlarını kontrol et
        const message =
            err?.invite_code?.[0] ||
            err?.password?.[0] ||
            err?.username?.[0] ||
            err?.email?.[0] ||
            err?.detail ||
            "Registration failed";
        throw new Error(message);
    }

    return res.json();
};

// Kullanıcı profil bilgisi
export const fetchProfile = async () => {
    const token = localStorage.getItem("access");
    const res = await fetch(`${API_URL}profile/`, {
        headers: { Authorization: `Bearer ${token}` },
    });

    if (!res.ok) throw new Error("Not authorized");

    return res.json();
};

// Çıkış yap
export const logoutUser = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    localStorage.removeItem("username");
};