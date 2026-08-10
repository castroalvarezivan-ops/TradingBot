// =========================================
// TradingBot Executive V8
// dashboard_v8.js (Completo Unificado)
// =========================================

// =========================================
// VARIABLES GLOBALES
// =========================================
let isScanning = false;
let radarChart = null;

// =========================================
// CACHE DEL DOM
// =========================================
const DOM = {
    balancePanel: document.getElementById("balance-panel"),
    botStatus: document.getElementById("bot-status"),
    lastScan: document.getElementById("last-scan"),
    signalsCount: document.getElementById("signals-count"),
    confidence: document.getElementById("confidence"),
    drawdown: document.getElementById("drawdown"),
    winrate: document.getElementById("winrate"),
    marketStatus: document.getElementById("market-status"),
    premiumSignal: document.getElementById("premium-signal"),
    signalsContainer: document.getElementById("signals-container"),
    gaugeFill: document.getElementById("gauge-fill"),
    gaugeValue: document.getElementById("gauge-value"),
    gaugeStatus: document.getElementById("gauge-status"),
    advisorPanel: document.getElementById("advisor-panel"),
    radarCanvas: document.getElementById("radarChart")
};

// =========================================
// NOTIFICACIONES
// =========================================
function notify(message, type = "success") {
    console.log(`[${type.toUpperCase()}] ${message}`);
}

// =========================================
// BALANCE
// =========================================
async function fetchBalance() {
    try {
        const response = await fetch("/api/balance");
        if (!response.ok) {
            throw new Error("Balance no disponible");
        }
        const data = await response.json();

        DOM.balancePanel.innerHTML = `
            <div class="text-right">
                <div class="text-gray-400">Balance</div>
                <div class="text-3xl font-bold text-emerald-400">
                    ${Number(data.total).toFixed(2)} USDT
                </div>
                <div class="text-sm text-gray-500">
                    Disponible ${Number(data.free).toFixed(2)}
                </div>
            </div>
        `;
    } catch (error) {
        console.error(error);
        DOM.balancePanel.innerHTML = `<span class="text-red-500">Error Balance</span>`;
    }
}

// =========================================
// STATUS
// =========================================
async function fetchStatus() {
    try {
        const response = await fetch("/api/status");
        if (!response.ok) {
            throw new Error("Estado no disponible");
        }
        const data = await response.json();

        DOM.botStatus.innerHTML = data.status ?? "OFFLINE";
        DOM.lastScan.innerHTML = data.last_scan ?? "--";
        DOM.signalsCount.innerHTML = Array.isArray(data.signals) ? data.signals.length : 0;

        if (DOM.winrate) {
            DOM.winrate.innerHTML = data.winrate ?? "--";
        }
        if (DOM.drawdown) {
            DOM.drawdown.innerHTML = data.drawdown ?? "--";
        }
    } catch (error) {
        console.error(error);
    }
}

// =========================================
// ESCANEAR MERCADO
// =========================================
async function scanMarket(dynamic = false) {
    if (isScanning) return;
    isScanning = true;

    DOM.marketStatus.innerHTML = "ESCANEANDO...";
    DOM.marketStatus.className = "market-box";

    try {
        const response = await fetch("/api/scan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ dynamic: dynamic })
        });

        if (!response.ok) {
            throw new Error("Error durante el escaneo");
        }

        const data = await response.json();
        renderSignals(data.signals || []);
        fetchStatus();
    } catch (error) {
        console.error(error);
        DOM.marketStatus.innerHTML = "ERROR";
    } finally {
        isScanning = false;
    }
}

// =========================================
// RENDER DE SEÑALES
// =========================================
function renderSignals(signals) {
    DOM.signalsContainer.innerHTML = "";
    DOM.premiumSignal.innerHTML = "";

    if (!signals || signals.length === 0) {
        DOM.marketStatus.innerHTML = "SIN OPORTUNIDADES";
        DOM.confidence.innerHTML = "0%";
        updateGauge(0);
        updateAdvisor(null);
        updateRadar([]);
        return;
    }

    let best = signals[0];
    signals.forEach(signal => {
        if (signal.score > best.score) best = signal;
    });

    DOM.marketStatus.innerHTML = `${best.action} (${best.score}%)`;
    DOM.marketStatus.className = "market-box";

    if (best.score >= 95) DOM.marketStatus.classList.add("glow-gold");
    else if (best.score >= 80) DOM.marketStatus.classList.add("glow-green");
    else DOM.marketStatus.classList.add("glow-red");

    DOM.confidence.innerHTML = best.score + "%";

    // OPORTUNIDAD PREMIUM
    if (best.score >= 95) {
        DOM.premiumSignal.innerHTML = `
            <div class="signal-card glow-gold premium-card">
                <div class="premium-title">⭐ OPORTUNIDAD PREMIUM ⭐</div>
                <div class="signal-symbol">${best.symbol}</div>
                <div class="signal-score">${best.score}%</div>
                <div class="signal-action">${best.action}</div>
                <div class="signal-price">Precio: ${Number(best.price).toFixed(4)}</div>
                <div>Stop Loss: ${Number(best.stop_loss).toFixed(4)}</div>
                <div>Take Profit: ${Number(best.take_profit).toFixed(4)}</div>
                <div class="text-gray-400 mt-3">${best.reason}</div>
                <button class="execute-button" onclick="executeTrade('${best.symbol}','${best.action}')">
                    🚀 EJECUTAR PREMIUM
                </button>
            </div>
        `;
    }

    // TARJETAS
    signals.forEach(signal => {
        let glow = "";
        if (signal.score >= 95) glow = "glow-gold";
        else if (signal.score >= 80) glow = "glow-green";

        DOM.signalsContainer.innerHTML += `
            <div class="signal-card ${glow}">
                <div class="signal-symbol">${signal.symbol}</div>
                <div class="signal-score">${signal.score}%</div>
                <div class="signal-action">${signal.action}</div>
                <div class="signal-price">Precio: ${Number(signal.price).toFixed(4)}</div>
                <div>Stop Loss: ${Number(signal.stop_loss).toFixed(4)}</div>
                <div>Take Profit: ${Number(signal.take_profit).toFixed(4)}</div>
                <div class="text-gray-400 mt-3">${signal.reason}</div>
                <button class="execute-button" onclick="executeTrade('${signal.symbol}','${signal.action}')">
                    EJECUTAR
                </button>
            </div>
        `;
    });

    updateGauge(best.score);
    updateAdvisor(best);
    updateRadar(signals);
}

// =========================================
// CONFIDENCE GAUGE
// =========================================
function updateGauge(score) {
    DOM.gaugeFill.style.width = score + "%";
    DOM.gaugeValue.innerHTML = score + "%";

    if (score >= 95) {
        DOM.gaugeValue.style.color = "#FFD700";
        DOM.gaugeStatus.innerHTML = "OPORTUNIDAD PREMIUM";
    } else if (score >= 80) {
        DOM.gaugeValue.style.color = "#00ff88";
        DOM.gaugeStatus.innerHTML = "OPERACIÓN FAVORABLE";
    } else if (score >= 60) {
        DOM.gaugeValue.style.color = "#facc15";
        DOM.gaugeStatus.innerHTML = "ESPERAR";
    } else {
        DOM.gaugeValue.style.color = "#ef4444";
        DOM.gaugeStatus.innerHTML = "NO OPERAR";
    }
}

// =========================================
// TRADING ADVISOR IA
// =========================================
function updateAdvisor(signal) {
    if (!signal) {
        DOM.advisorPanel.innerHTML = `
            <div class="text-gray-400">Esperando análisis...</div>
        `;
        return;
    }

    DOM.advisorPanel.innerHTML = `
        <div>
            <h3 style="font-size:22px;font-weight:bold;">${signal.symbol}</h3>
            <br>
            <b>Acción:</b> ${signal.action}<br><br>
            <b>Confianza:</b> ${signal.score}%<br><br>
            <b>Precio:</b> ${Number(signal.price).toFixed(4)}<br><br>
            <b>Stop Loss:</b> ${Number(signal.stop_loss).toFixed(4)}<br><br>
            <b>Take Profit:</b> ${Number(signal.take_profit).toFixed(4)}<br><br>
            <div class="text-gray-400">${signal.reason}</div>
        </div>
    `;
}

// =========================================
// RADAR DEL MERCADO
// =========================================
function updateRadar(signals) {
    if (!DOM.radarCanvas) return;

    const labels = [];
    const scores = [];

    signals.slice(0, 5).forEach(signal => {
        labels.push(signal.symbol);
        scores.push(signal.score);
    });

    if (radarChart !== null) {
        radarChart.destroy();
    }

    radarChart = new Chart(DOM.radarCanvas, {
        type: "radar",
        data: {
            labels: labels,
            datasets: [{
                label: "Confianza IA",
                data: scores,
                fill: true,
                backgroundColor: "rgba(0,255,136,.20)",
                borderColor: "#00ff88",
                borderWidth: 2,
                pointBackgroundColor: "#00ff88",
                pointRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: { color: "#ffffff" }
                }
            },
            scales: {
                r: {
                    min: 0,
                    max: 100,
                    ticks: {
                        color: "#94a3b8",
                        backdropColor: "transparent"
                    },
                    grid: { color: "#334155" },
                    angleLines: { color: "#334155" },
                    pointLabels: { color: "#ffffff" }
                }
            }
        }
    });
}

// =========================================
// EJECUTAR ORDEN
// =========================================
async function executeTrade(symbol, action) {
    try {
        const response = await fetch("/api/execute", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                symbol: symbol,
                action: action,
                amount: 15
            })
        });

        if (!response.ok) {
            throw new Error("No fue posible ejecutar la orden.");
        }

        const data = await response.json();
        notify("Orden ejecutada correctamente.");
        console.log(data);

        fetchBalance();
        fetchStatus();
    } catch (error) {
        console.error(error);
        notify("Error ejecutando la orden.", "error");
    }
}

// =========================================
// KILL SWITCH
// =========================================
function killSwitch() {
    const confirmacion = confirm("¿Desea detener inmediatamente el TradingBot?");
    if (!confirmacion) return;

    notify("Trading detenido.");
    console.log("BOT DETENIDO");
}

// =========================================
// ACTUALIZACIÓN GENERAL
// =========================================
function refreshDashboard() {
    fetchBalance();
    fetchStatus();
}

// =========================================
// INICIALIZACIÓN
// =========================================
window.addEventListener("load", () => {
    console.log("====================================");
    console.log(" TradingBot Executive V8");
    console.log(" Dashboard Inicializado");
    console.log("====================================");

    refreshDashboard();
    scanMarket(false);
});

// =========================================
// AUTO REFRESH
// =========================================
// Balance cada 5 segundos
setInterval(() => {
    fetchBalance();
}, 5000);

// Estado cada 3 segundos
setInterval(() => {
    fetchStatus();
}, 3000);

// Escaneo automático cada minuto
setInterval(() => {
    scanMarket(false);
}, 60000);