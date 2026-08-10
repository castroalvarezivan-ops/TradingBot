/* ==========================================
   TradingBot Executive V8
   Trading Advisor IA
========================================== */

function updateAdvisor(bestSignal){

    const advisor = document.getElementById("advisor-panel");

    if(!advisor) return;

    if(!bestSignal){

        advisor.innerHTML = `
            <div class="text-gray-400">
                Esperando análisis...
            </div>
        `;

        return;

    }

    let riesgo = "ALTO";
    let color = "#ef4444";

    if(bestSignal.score >= 95){
        riesgo = "MUY BAJO";
        color = "#22c55e";
    }
    else if(bestSignal.score >= 85){
        riesgo = "BAJO";
        color = "#84cc16";
    }
    else if(bestSignal.score >= 75){
        riesgo = "MODERADO";
        color = "#facc15";
    }

    advisor.innerHTML = `

        <div style="line-height:32px;">

            <h3 style="font-size:22px;margin-bottom:15px;">
                🤖 Trading Advisor
            </h3>

            <p>
                ✔ Activo:
                <b>${bestSignal.symbol}</b>
            </p>

            <p>
                ✔ Acción:
                <b>${bestSignal.action}</b>
            </p>

            <p>
                ✔ Confianza:
                <b>${bestSignal.score}%</b>
            </p>

            <p>
                ✔ Riesgo:
                <b style="color:${color}">
                    ${riesgo}
                </b>
            </p>

            <p>
                ✔ Precio:
                ${Number(bestSignal.price).toFixed(4)}
            </p>

            <p>
                ✔ Stop Loss:
                ${Number(bestSignal.stop_loss).toFixed(4)}
            </p>

            <p>
                ✔ Take Profit:
                ${Number(bestSignal.take_profit).toFixed(4)}
            </p>

            <hr style="margin:18px 0;">

            <p>
                ${bestSignal.reason}
            </p>

        </div>

    `;

}