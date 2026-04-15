const API_URL = "http://localhost:8000"; // Usando backend local

const fmt = (v) => v.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });

async function calcular() {
    const tipo = document.getElementById("tipoCliente").value;
    const valor = parseFloat(document.getElementById("valorCompra").value);
    const desconto = parseFloat(document.getElementById("descontoPct").value) || 0;

    if (!valor || valor <= 0) return alert("Insira um valor válido.");

    const res = await fetch(`${API_URL}/calcular`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            tipo_cliente: tipo,
            valor_compra: valor,
            desconto_pct: desconto
        })
    });

    if (!res.ok) return alert("Erro ao calcular. Tente novamente.");

    const data = await res.json();
    document.getElementById("resValorFinal").textContent = fmt(data.valor_final);
    document.getElementById("resCashback").textContent = fmt(data.cashback);
    document.getElementById("resultado").style.display = "block";

    carregarHistorico();
}

async function carregarHistorico() {
    const res = await fetch(`${API_URL}/historico`);
    const rows = await res.json();
    const tbody = document.getElementById("historicoBody");
    const semH = document.getElementById("semHistorico");

    tbody.innerHTML = "";

    if (!rows.length) {
        semH.style.display = "block";
        return;
    }

    semH.style.display = "none";
    rows.forEach(r => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
      <td>${r.tipo_cliente}</td>
      <td>${fmt(r.valor_compra)}</td>
      <td>${r.desconto_pct}%</td>
      <td>${fmt(r.valor_final)}</td>
      <td class="highlight">${fmt(r.cashback)}</td>
      <td>${new Date(r.criado_em).toLocaleString("pt-BR")}</td>
    `;
        tbody.appendChild(tr);
    });
}

// Lógica de Modo Dark
const themeToggle = document.getElementById("themeToggle");
const currentTheme = localStorage.getItem("theme") || "light";

document.documentElement.setAttribute("data-theme", currentTheme);
const initialIcon = themeToggle.querySelector("i");
initialIcon.className = currentTheme === "dark" ? "fas fa-sun" : "fas fa-moon";

themeToggle.addEventListener("click", () => {
    let theme = document.documentElement.getAttribute("data-theme");
    const icon = themeToggle.querySelector("i");
    if (theme === "dark") {
        theme = "light";
        icon.className = "fas fa-moon";
    } else {
        theme = "dark";
        icon.className = "fas fa-sun";
    }
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
});

document.getElementById("calcBtn").addEventListener("click", calcular);
window.addEventListener("load", carregarHistorico);
