// TaxiApp.js
function requestTaxi(userLocation) {
    console.log("사용자 앱: 택시 호출 요청");

    const callInfo = {
        location: userLocation,
        time: new Date()
    };

    const result = sendToServer(callInfo);
    showResultToUser(result);
}

function sendToServer(callInfo) {
    console.log("앱 → 서버: 호출 정보 전송");

    const isDriverAvailable = Math.random() > 0.2; // 80% 확률로 배차 성공
    if (isDriverAvailable) {
        return {
            success: true,
            driver: "홍길동 기사님",
            carNumber: "12가 3456"
        };
    } else {
        return {
            success: false,
            message: "현재 근처에 배차 가능한 차량이 없습니다."
        };
    }
}

function showResultToUser(result) {
    if (result.success) {
        console.log("🚖 배차 완료:", result.driver, result.carNumber);
    } else {
        console.log("❌ 배차 실패:", result.message);
    }
}

// 실행 예시
requestTaxi("서울 성동구 왕십리로 222");
