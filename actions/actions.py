# actions/actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



DATA = {
    "nganh": {
        "Điều khiển và Tự động hóa": {
            "ma_nganh": "7520116",
            "thoi_gian_dao_tao": "4 năm",
            "chi_tieu": {2025: 140, 2024: 125},
            "diem_chuan": {2025: {"THPT": 26.19, "XTKH": 24.18, "DGNL": 16}}
        },
        "Công nghệ Vi mạch Bán dẫn": {
            "ma_nganh": "7520210",
            "thoi_gian_dao_tao": "4 năm",
            "chi_tieu": {2025: 90, 2024: 85},
            "diem_chuan": {2025: {"THPT": 25.5, "XTKH": None, "DGNL": None}}
        },
        "Công nghệ Kỹ thuật Điện, Điện tử": {
            "ma_nganh": "7520102",
            "thoi_gian_dao_tao": "4 năm",
            "chi_tieu": {2025: 120, 2024: 115},
            "diem_chuan": {2025: {"THPT": 24.61, "XTKH": 24.27, "DGNL": 16}}
        }
    },
    "co_so": {
        "Hà Nội": {2025: 200, 2024: 180},
        "TP.HCM": {2025: 150, 2024: 140},
        "miền Bắc": {2025: 220, 2024: 200},
        "miền Nam": {2025: 130, 2024: 120}
    },
    "phuong_thuc": {
        "Thi THPT": {2025: 180, 2024: 160},
        "Học bạ": {2025: 100, 2024: 90},
        "Xét tuyển thẳng": {2025: 30, 2024: 25}
    },
    "khoa": {
        "Điện tử": {2025: 350, 2024: 330}
    },
    "lich": {
        "tuyen_sinh": {
            2025: "Từ 01/06/2025 đến 30/07/2025",
            2024: "Từ 01/06/2024 đến 30/07/2024"
        },
        "nhap_hoc": {
            2025: "01/09/2025",
            2024: "01/09/2024"
        }
    }
}


class ActionTraCuuDiemChuanNam2025(Action):

    def name(self) -> Text:
        return "action_tra_cuu_diem_chuan_thpt_nam_2025"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text="Hãy cho tôi biết bạn muốn hỏi điểm chuẩn thpt của ngành nào?")
            return []
        diem_chuan_db = {
            "kỹ thuật điều khiển và tự động hóa": "26.19",
            "công nghệ kỹ thuật điện, điện tử": "24.61",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "25.5",
        }
        diem = diem_chuan_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm chuẩn thpt của ngành này.")
        dispatcher.utter_message(text=f"Điểm chuẩn thpt của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuMaNganhCuaKhoaKyThuatDienTu1(Action):
    def name(self) -> Text:
        return "action_tra_cuu_ma_nganh"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text="Hãy cho tôi biết bạn muốn hỏi mã ngành của ngành nào trong khoa Kỹ thuật điện tử 1?")
            return []
        ma_nganh_db = {
            "kỹ thuật điều khiển và tự động hóa": "7520216",
            "công nghệ kỹ thuật điện, điện tử": "7510301",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "7510301",
        }
        ma = ma_nganh_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về mã ngành của ngành này.")
        dispatcher.utter_message(text=f"Mã ngành của ngành {ten_nganh} là {ma} bạn nhé.")
        return []

class ActionTraCuuDiemTheoPhuongThucXetTuyenTaiNang(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_xet_tuyen_tai_nang"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển tài năng của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "82.35",
            "công nghệ kỹ thuật điện, điện tử": "66.2857",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "80.625",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển tài năng của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển tài năng của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiSAT(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_chung_chi_sat"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ SAT của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "1397",
            "công nghệ kỹ thuật điện, điện tử": "1313.4285",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "1362.5",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ SAT của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ SAT của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiACT(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_chung_chi_act"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ ACT của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "31.41",
            "công nghệ kỹ thuật điện, điện tử": "29.2685",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "30.375",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ ACT của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ ACT của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoBaiThiHSA(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_bai_thi_hsa"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo bài thi HSA của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "100.76",
            "công nghệ kỹ thuật điện, điện tử": "94.9057",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "98",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo bài thi HSA của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo bài thi HSA của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiTSA(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_bai_thi_tsa"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ TSA của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "72.2228",
            "công nghệ kỹ thuật điện, điện tử": "67.8746",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "70.07",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ TSA của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ TSA của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiSPT(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_bai_thi_spt"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ SPT của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "23.8075",
            "công nghệ kỹ thuật điện, điện tử": "21.9271",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "23.0313",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ SPT của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ SPT của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoChungChiAPT(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_bai_thi_apt"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo chứng chỉ APT của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "920.84",
            "công nghệ kỹ thuật điện, điện tử": "861.0341",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "896",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo chứng chỉ APT của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo chứng chỉ APT của ngành {ten_nganh} là {diem} bạn nhé.")
        return []

class ActionTraCuuDiemTheoXetTuyenKetHop(Action):
    def name(self) -> Text:
        return "action_tra_cuu_diem_theo_xet_tuyen_ket_hop"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)
        if not ten_nganh:
            dispatcher.utter_message(text= "Hãy cho tôi biết bạn muốn hỏi điểm xét tuyển theo xét tuyển kết hợp của ngành nào?")
            return []
        diem_xet_tuyen_thang_db = {
            "kỹ thuật điều khiển và tự động hóa": "28.22",
            "công nghệ kỹ thuật điện, điện tử": "27.2928",
            "công nghệ vi mạch bán dẫn (ngành công nghệ kỹ thuật điện, điện tử)": "27.875",
        }
        diem = diem_xet_tuyen_thang_db.get(ten_nganh.lower(), "hiện tại tôi chưa có thông tin về điểm xét tuyển theo xét tuyển kết hợp của ngành này.")
        dispatcher.utter_message(text=f"Điểm xét tuyển theo xét tuyển kết hợp của ngành {ten_nganh} là {diem} bạn nhé.")
        return []



class ActionTraCuuKhaNangTrungTuyen(Action):

    def name(self) -> Text:
        return "action_tra_cuu_kha_nang_trung_tuyen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        diem = tracker.get_slot("diem")
        ten_nganh = tracker.get_slot("ten_nganh")
        nam = tracker.get_slot("nam") or 2025  # mặc định năm 2025 nếu không có

        if diem is None or ten_nganh is None:
            dispatcher.utter_message(text="Vui lòng cung cấp tên ngành và số điểm của bạn.")
            return []

        try:
            diem = float(diem)
        except ValueError:
            dispatcher.utter_message(text="Điểm nhập không hợp lệ.")
            return []

        # Dữ liệu điểm chuẩn “cứng” trong dictionary
        diem_chuan_data = {
            2022: {
                "Kỹ thuật Điều khiển & Tự động hóa": {"THPT": 19.05, "XTKH": None, "DGNL": None},
                "Công nghệ Vi mạch Bán dẫn": {"THPT": None, "XTKH": None, "DGNL": None},
                "Công nghệ Kỹ thuật Điện, Điện tử": {"THPT": 25.1, "XTKH": 22.5, "DGNL": 19.3},
            },
            2023: {
                "Kỹ thuật Điều khiển & Tự động hóa": {"THPT": 25.4, "XTKH": None, "DGNL": None},
                "Công nghệ Vi mạch Bán dẫn": {"THPT": None, "XTKH": None, "DGNL": None},
                "Công nghệ Kỹ thuật Điện, Điện tử": {"THPT": 25.01, "XTKH": 21.2, "DGNL": 16.45},
            },
            2024: {
                "Kỹ thuật Điều khiển & Tự động hóa": {"THPT": 26.08, "XTKH": 27.71, "DGNL": 22.05},
                "Công nghệ Vi mạch Bán dẫn": {"THPT": None, "XTKH": None, "DGNL": None},
                "Công nghệ Kỹ thuật Điện, Điện tử": {"THPT": 25.46, "XTKH": 25.07, "DGNL": 19.84},
            },
            2025: {
                "Kỹ thuật Điều khiển & Tự động hóa": {"THPT": 26.19, "XTKH": 24.18, "DGNL": 16.4},
                "Công nghệ Vi mạch Bán dẫn": {"THPT": 25.5, "XTKH": None, "DGNL": None},
                "Công nghệ Kỹ thuật Điện, Điện tử": {"THPT": 24.61, "XTKH": 24.27, "DGNL": 16},
            },
        }

        if nam not in diem_chuan_data or ten_nganh not in diem_chuan_data[nam]:
            dispatcher.utter_message(text=f"Hiện chưa có dữ liệu điểm chuẩn cho ngành {ten_nganh} năm {nam}.")
            return []

        ket_qua = []
        for phuong_thuc, diem_ch in diem_chuan_data[nam][ten_nganh].items():
            if diem_ch is None:
                continue
            if diem >= diem_ch:
                ket_qua.append(f"Bạn đủ điểm trúng tuyển {phuong_thuc}.")
            else:
                ket_qua.append(f"Bạn chưa đủ điểm trúng tuyển {phuong_thuc}.")

        if not ket_qua:
            dispatcher.utter_message(text=f"Hiện chưa có dữ liệu xét tuyển cho ngành {ten_nganh} năm {nam}.")
        else:
            dispatcher.utter_message(text="\n".join(ket_qua))

        return []

# ====== Xét tuyển nguyện vọng ======
class ActionXetTuyenNguyenVongDienTu(Action):

    def name(self) -> Text:
        return "action_xet_tuyen_nguyen_vong_dien_tu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nv1 = tracker.get_slot("nguyen_vong_1")
        nv2 = tracker.get_slot("nguyen_vong_2")

        if nv1 and nv2:
            dispatcher.utter_message(
                text=f"Nếu bạn trúng tuyển NV1 ({nv1}), bạn có thể học NV2 ({nv2}) nếu NV1 không đăng ký."
            )
        else:
            dispatcher.utter_message(
                text="Nguyên vọng chưa rõ. Vui lòng cung cấp đầy đủ NV1 và NV2."
            )

        return []

# ====== Xét tuyển điều kiện ======
class ActionXetTuyenDieuKienDienTu(Action):

    def name(self) -> Text:
        return "action_xet_tuyen_dieu_kien_dien_tu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = tracker.get_slot("ten_nganh")

        # Giả lập dữ liệu điều kiện trúng tuyển
        dieu_kien = {
            "Điều khiển và Tự động hóa": "Điểm thi THPT ≥ 26 hoặc điểm học bạ ≥ 24.",
            "Công nghệ Vi mạch Bán dẫn": "Điểm thi THPT ≥ 25.5.",
            "Công nghệ Kỹ thuật Điện, Điện tử": "Điểm thi THPT ≥ 24.61 hoặc điểm học bạ ≥ 24.27."
        }

        if ten_nganh in dieu_kien:
            dispatcher.utter_message(text=f"Điều kiện xét tuyển ngành {ten_nganh}: {dieu_kien[ten_nganh]}")
        else:
            dispatcher.utter_message(text=f"Hiện chưa có dữ liệu điều kiện xét tuyển cho ngành {ten_nganh}.")

        return []

# ====== Xét tuyển thủ tục ======
class ActionXetTuyenThuTucDienTu(Action):

    def name(self) -> Text:
        return "action_xet_tuyen_thu_tuc_dien_tu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=(
            "Thủ tục xét tuyển các ngành điện tử gồm:\n"
            "- Đăng ký nguyện vọng trên hệ thống tuyển sinh.\n"
            "- Nộp hồ sơ gồm phiếu đăng ký, học bạ, giấy tờ tùy thân.\n"
            "- Thời gian nộp hồ sơ theo thông báo của trường.\n"
            "- Có thể cần chứng minh học lực hoặc chứng chỉ nếu ngành yêu cầu."
        ))

        return []

# ====== Xét tuyển trường hợp đặc biệt ======
class ActionXetTuyenTruongHopDacBietDienTu(Action):

    def name(self) -> Text:
        return "action_xet_tuyen_truong_hop_dac_biet_dien_tu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=(
            "Các trường hợp đặc biệt trong xét tuyển ngành điện tử:\n"
            "- Nếu trúng tuyển NV1 nhưng muốn học NV2, phải xem xét theo quy định chuyển ngành.\n"
            "- Trường hợp điểm thi bằng nhau sẽ xét theo điểm ưu tiên hoặc theo thứ tự nguyện vọng.\n"
            "- Nộp thiếu hồ sơ xét tuyển sẽ không được xét, cần nộp bổ sung.\n"
            "- Trường hợp không trúng tuyển NV1 vẫn có thể xét tuyển bổ sung nếu trường tổ chức."
        ))

        return []

# ====== Xét tuyển ưu tiên ======
class ActionXetTuyenUuTienDienTu(Action):

    def name(self) -> Text:
        return "action_xet_tuyen_uu_tien_dien_tu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=(
            "Xét tuyển ưu tiên ngành điện tử:\n"
            "- Học sinh giỏi quốc gia hoặc học sinh chuyên có thể được xét tuyển thẳng.\n"
            "- Có thể xét tuyển theo diện học bổng hoặc thành tích đặc biệt.\n"
            "- Tiêu chí ưu tiên gồm thành tích học tập, giải thưởng quốc gia, năng lực ngoại ngữ hoặc các chứng chỉ khác.\n"
            "- Thí sinh cần nộp hồ sơ chứng minh năng lực để được xét ưu tiên."
        ))

        return []

# ====== Liên hệ xét tuyển ======
class ActionXetTuyenLienHeDienTu(Action):

    def name(self) -> Text:
        return "action_xet_tuyen_lien_he_dien_tu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=(
            "Thông tin liên hệ xét tuyển ngành điện tử:\n"
            "- Phòng tuyển sinh khoa Điện tử: email: dien_tu@ptit.edu.vn, số điện thoại: 0243xxxxxxx\n"
            "- Website: https://ptit.edu.vn/dientu\n"
            "- Fanpage: https://facebook.com/ptit.dientu\n"
            "- Bạn có thể liên hệ trực tiếp để được tư vấn thủ tục xét tuyển."
        ))

        return []

# ====== Tra cứu chỉ tiêu ======
class ActionTraCuuChiTieuNganh(Action):

    def name(self) -> Text:
        return "action_tra_cuu_chi_tieu_nganh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = tracker.get_slot("ten_nganh")
        nam = tracker.get_slot("nam") or 2025

        # Giả lập dữ liệu chỉ tiêu
        chi_tieu_data = {
            2022: {
                "Kỹ thuật Điều khiển và Tự động hóa": 120,
                "Công nghệ Vi mạch Bán dẫn": 80,
                "Công nghệ Kỹ thuật Điện, Điện tử": 100,
            },
            2023: {
                "Kỹ thuật Điều khiển và Tự động hóa": 130,
                "Công nghệ Vi mạch Bán dẫn": 90,
                "Công nghệ Kỹ thuật Điện, Điện tử": 110,
            },
            2024: {
                "Kỹ thuật Điều khiển và Tự động hóa": 125,
                "Công nghệ Vi mạch Bán dẫn": 85,
                "Công nghệ Kỹ thuật Điện, Điện tử": 115,
            },
            2025: {
                "Kỹ thuật Điều khiển và Tự động hóa": 140,
                "Công nghệ Vi mạch Bán dẫn": 90,
                "Công nghệ Kỹ thuật Điện, Điện tử": 120,
            },
        }

        if int(nam) in chi_tieu_data and ten_nganh in chi_tieu_data[int(nam)]:
            dispatcher.utter_message(
                text=f"Chỉ tiêu tuyển sinh ngành {ten_nganh} năm {nam} là {chi_tieu_data[int(nam)][ten_nganh]} sinh viên."
            )
        else:
            dispatcher.utter_message(
                text=f"Hiện chưa có dữ liệu chỉ tiêu cho ngành {ten_nganh} năm {nam}."
            )

        return []

# ----- Tra cứu chỉ tiêu theo cơ sở -----
class ActionTraCuuChiTieuTheoCoSo(Action):
    def name(self) -> Text:
        return "action_tra_cuu_chi_tieu_theo_co_so"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        co_so = tracker.get_slot("co_so")
        nam = int(tracker.get_slot("nam") or 2025)

        if co_so in DATA["co_so"] and nam in DATA["co_so"][co_so]:
            chi_tieu = DATA["co_so"][co_so][nam]
            dispatcher.utter_message(
                text=f"Chỉ tiêu tuyển sinh tại cơ sở {co_so} năm {nam} là {chi_tieu} sinh viên."
            )
        else:
            dispatcher.utter_message(
                text=f"Chưa có dữ liệu chỉ tiêu cho cơ sở {co_so} năm {nam}."
            )
        return []

# ----- Tra cứu chỉ tiêu theo phương thức -----
class ActionTraCuuChiTieuTheoPhuongThuc(Action):
    def name(self) -> Text:
        return "action_tra_cuu_chi_tieu_theo_phuong_thuc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        phuong_thuc = tracker.get_slot("phuong_thuc")
        nam = int(tracker.get_slot("nam") or 2025)

        if phuong_thuc in DATA["phuong_thuc"] and nam in DATA["phuong_thuc"][phuong_thuc]:
            chi_tieu = DATA["phuong_thuc"][phuong_thuc][nam]
            dispatcher.utter_message(
                text=f"Chỉ tiêu dành cho phương thức {phuong_thuc} năm {nam} là {chi_tieu} sinh viên."
            )
        else:
            dispatcher.utter_message(
                text=f"Chưa có dữ liệu chỉ tiêu cho phương thức {phuong_thuc} năm {nam}."
            )
        return []

# ----- Tra cứu chỉ tiêu tổng quát (khoa) -----
class ActionTraCuuChiTieuTongQuat(Action):
    def name(self) -> Text:
        return "action_tra_cuu_chi_tieu_tong_quat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        khoa = tracker.get_slot("khoa")
        nam = int(tracker.get_slot("nam") or 2025)

        if khoa in DATA["khoa"] and nam in DATA["khoa"][khoa]:
            chi_tieu = DATA["khoa"][khoa][nam]
            dispatcher.utter_message(
                text=f"Tổng chỉ tiêu tuyển sinh của {khoa} năm {nam} là {chi_tieu} sinh viên."
            )
        else:
            dispatcher.utter_message(
                text=f"Chưa có dữ liệu tổng chỉ tiêu của {khoa} năm {nam}."
            )
        return []

# ----- Tra cứu thời gian tuyển sinh -----
class ActionTraCuuThoiGianTuyenSinh(Action):
    def name(self) -> Text:
        return "action_tra_cuu_thoi_gian_tuyen_sinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nam = int(tracker.get_slot("nam") or 2025)

        if nam in DATA["lich"]["tuyen_sinh"]:
            lich = DATA["lich"]["tuyen_sinh"][nam]
            dispatcher.utter_message(
                text=f"Thời gian tuyển sinh năm {nam} diễn ra từ {lich}."
            )
        else:
            dispatcher.utter_message(text="Chưa có dữ liệu lịch tuyển sinh.")
        return []

# ----- Tra cứu thời gian nhập học -----
class ActionTraCuuThoiGianNhapHoc(Action):
    def name(self) -> Text:
        return "action_tra_cuu_thoi_gian_nhap_hoc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nam = int(tracker.get_slot("nam") or 2025)

        if nam in DATA["lich"]["nhap_hoc"]:
            lich = DATA["lich"]["nhap_hoc"][nam]
            dispatcher.utter_message(
                text=f"Thời gian nhập học năm {nam} là {lich}."
            )
        else:
            dispatcher.utter_message(text="Chưa có dữ liệu lịch nhập học.")
        return []

class ActionTraCuuTongQuanNganh(Action):

    def name(self) -> Text:
        return "action_tra_cuu_tong_quan_nganh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Lấy tên ngành từ entity
        ten_nganh = tracker.get_slot("ten_nganh")

        # Dữ liệu tổng quan ngành PTIT (ví dụ ngành Điện, Điện tử)
        tong_quan = {
            "Công nghệ Kỹ thuật Điện, điện tử": """
Ngành Công nghệ Kỹ thuật Điện, Điện tử tại PTIT đào tạo kỹ sư có kiến thức và kỹ năng vững chắc về điện tử, đo lường, tín hiệu, vi điều khiển, thiết kế mạch và hệ thống điều khiển. 
Chương trình hướng tới ứng dụng công nghệ cao trong các lĩnh vực công nghiệp, tự động hóa, truyền thông số và hệ thống thông minh.

- Mã ngành: 7510301
- Thời gian đào tạo: khoảng 4,5 năm
- Tổ hợp xét tuyển: A00 (Toán – Lý – Hóa), A01 (Toán – Lý – Anh)
- Kiến thức và kỹ năng: Điện tử, đo lường, tín hiệu, vi điều khiển, thiết kế mạch và hệ thống điều khiển; thiết kế, mô phỏng, tích hợp hệ thống phần cứng – phần mềm; sử dụng phần mềm Altium, MATLAB, Proteus, PLC, LabVIEW; ngoại ngữ chuyên ngành; đạo đức nghề nghiệp và tinh thần đổi mới sáng tạo
- Chuyên ngành đào tạo: Xử lý tín hiệu và truyền thông, Kỹ thuật Điện tử máy tính, Kỹ thuật Robotics, Thiết kế vi mạch
- Cơ hội nghề nghiệp: Thiết kế, chế tạo hệ thống điện tử; tự động hóa trong sản xuất; phát triển và quản lý truyền thông số; nghiên cứu và phát triển công nghệ mới
- Xu hướng công nghệ: Internet of Things (IoT), Trí tuệ nhân tạo (AI), Mạng 5G
"""
        }

        # Lấy thông tin ngành, nếu không có dữ liệu trả về thông báo
        response = tong_quan.get(ten_nganh, "Xin lỗi, hiện tại mình chưa có thông tin tổng quan về ngành này.")

        # Gửi thông tin cho người dùng
        dispatcher.utter_message(text=response)

        return []

class ActionTraCuuMaNganh(Action):

    def name(self) -> Text:
        return "action_tra_cuu_ma_nganh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = tracker.get_slot("ten_nganh")

        ma_nganh_data = {
            "Công nghệ Kỹ thuật Điện, điện tử": "7510301",
            "Kỹ thuật Điện tử viễn thông": "7520207",
            "Kỹ thuật Điều khiển và Tự động hóa": "7520216"
        }

        ma_nganh = ma_nganh_data.get(ten_nganh, None)
        if ma_nganh:
            response = f"Mã ngành {ten_nganh} là {ma_nganh}."
        else:
            response = "Xin lỗi, mình chưa có thông tin mã ngành này."

        dispatcher.utter_message(text=response)
        return []

class ActionTraCuuThoiGianDaoTao(Action):

    def name(self) -> Text:
        return "action_tra_cuu_thoi_gian_dao_tao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = tracker.get_slot("ten_nganh")

        thoi_gian_data = {
            "Công nghệ Kỹ thuật Điện, điện tử": "4,5 năm",
            "Kỹ thuật Điện tử viễn thông": "4,5 năm",
            "Kỹ thuật Điều khiển và Tự động hóa": "4,5 năm"
        }

        thoi_gian = thoi_gian_data.get(ten_nganh, None)
        if thoi_gian:
            response = f"Ngành {ten_nganh} có thời gian đào tạo {thoi_gian}."
        else:
            response = "Xin lỗi, mình chưa có thông tin thời gian đào tạo ngành này."

        dispatcher.utter_message(text=response)
        return []


class ActionTraCuuToHopXetTuyen(Action):
    def name(self) -> Text:
        return "action_tra_cuu_to_hop_xet_tuyen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = tracker.get_slot("ten_nganh")

        # Dữ liệu tổ hợp xét tuyển từ PTIT
        TO_HOP = {
            "Điều khiển và Tự động hóa": ["A00", "A01", "D07"],
            "Công nghệ Kỹ thuật Điện, điện tử": ["A00", "A01", "D07"],
            "Công nghệ Vi mạch Bán dẫn": ["A00", "A01"]
        }

        if ten_nganh in TO_HOP:
            dispatcher.utter_message(
                text=f"Ngành {ten_nganh} xét tuyển theo các tổ hợp: {', '.join(TO_HOP[ten_nganh])}.")
        else:
            dispatcher.utter_message(text=f"Xin lỗi, hiện chưa có thông tin tổ hợp xét tuyển cho ngành {ten_nganh}.")

        return []


class ActionTraCuuHocPhiNganh(Action):
    def name(self) -> Text:
        return "action_tra_cuu_hoc_phi_nganh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = tracker.get_slot("ten_nganh")

        # Dữ liệu học phí từ PTIT
        HOC_PHI = {
            "Điều khiển và Tự động hóa": "Khoảng 25 - 36 triệu đồng/năm.",
            "Công nghệ Kỹ thuật Điện, điện tử": "Khoảng 25 - 36 triệu đồng/năm.",
            "Công nghệ Vi mạch Bán dẫn": "Khoảng 25 - 36 triệu đồng/năm."
        }

        if ten_nganh in HOC_PHI:
            dispatcher.utter_message(
                text=f"Học phí ngành {ten_nganh} tại PTIT năm học 2025-2026 là {HOC_PHI[ten_nganh]} Để biết thêm chi tiết, vui lòng tham khảo tại trang web chính thức của PTIT: https://ptit.edu.vn/"
            )
        else:
            dispatcher.utter_message(
                text=f"Xin lỗi, hiện chưa có thông tin học phí cho ngành {ten_nganh}. Bạn có thể kiểm tra thông tin chi tiết tại trang web chính thức của PTIT: https://ptit.edu.vn/"
            )

        return []
class ActionTraCuuLoTrinhTangHocPhi(Action):
    def name(self) -> Text:
        return "action_tra_cuu_lotrinh_tang_hoc_phi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if not ten_nganh:
            dispatcher.utter_message(
                text="Bạn muốn hỏi lộ trình tăng học phí của ngành nào vậy?"
            )
            return []

        # Theo quy định PTIT
        lo_trinh = "Theo quy định của Học viện Công nghệ Bưu chính Viễn thông (PTIT), học phí có thể tăng từ 10% đến 15% mỗi năm, với mức tối đa không vượt quá 15%/năm."

        dispatcher.utter_message(
            text=f"Học phí ngành {ten_nganh} sẽ tuân theo lộ trình chung: {lo_trinh}"
        )
        return []
class ActionTraCuuHocPhiTheoTinChi(Action):
    def name(self) -> Text:
        return "action_tra_cuu_hoc_phi_theo_tin_chi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if not ten_nganh:
            dispatcher.utter_message(
                text="Bạn muốn hỏi học phí theo tín chỉ của ngành nào vậy?"
            )
            return []

        tra_loi = (
            f"Học phí ngành {ten_nganh} tại Học viện Công nghệ Bưu chính Viễn thông "
            f"được tính theo số tín chỉ sinh viên đăng ký. "
            f"Nghĩa là bạn học nhiều tín chỉ thì học phí sẽ cao hơn, "
            f"chứ không thu cố định theo kỳ."
        )

        dispatcher.utter_message(text=tra_loi)
        return []

class ActionTraCuuCoSoDaoTao(Action):
    def name(self) -> Text:
        return "action_tra_cuu_co_so_dao_tao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if not ten_nganh:
            dispatcher.utter_message(
                text="Bạn muốn hỏi cơ sở đào tạo của ngành nào vậy?"
            )
            return []

        tra_loi = (
            f"Ngành {ten_nganh} được đào tạo tại cả 2 cơ sở của Học viện Công nghệ Bưu chính Viễn thông (PTIT):\n"
            f"- **Cơ sở Hà Nội** (Hà Đông)\n"
            f"- **Cơ sở TP.HCM** (Quận 9).\n"
            f"Bạn có thể đăng ký học tại một trong hai cơ sở này tuỳ nguyện vọng."
        )

        dispatcher.utter_message(text=tra_loi)
        return []


class ActionTraCuuCoHocBong(Action):
    def name(self) -> Text:
        return "action_tra_cuu_co_hoc_bong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if not ten_nganh:
            dispatcher.utter_message(
                text="Bạn muốn hỏi học bổng của ngành nào vậy?"
            )
            return []

        tra_loi = (
            f"Sinh viên ngành {ten_nganh} tại PTIT đều có cơ hội nhận học bổng. "
            f"Học bổng được xét dựa trên kết quả học tập, rèn luyện hoặc theo diện ưu tiên, hỗ trợ của Nhà nước và doanh nghiệp."
        )

        dispatcher.utter_message(text=tra_loi)
        return []


class ActionTraCuuLoaiHocBong(Action):
    def name(self) -> Text:
        return "action_tra_cuu_loai_hoc_bong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if not ten_nganh:
            dispatcher.utter_message(
                text="Bạn muốn biết loại học bổng áp dụng cho ngành nào vậy?"
            )
            return []

        tra_loi = (
            f"Sinh viên ngành {ten_nganh} tại PTIT có thể nhận nhiều loại học bổng, bao gồm:\n"
            f"- **Học bổng khuyến khích học tập** (dựa vào kết quả học tập và rèn luyện)\n"
            f"- **Học bổng tài năng** cho sinh viên xuất sắc\n"
            f"- **Học bổng doanh nghiệp tài trợ** (từ các công ty, tập đoàn hợp tác với Học viện)\n"
            f"- **Học bổng hỗ trợ khác** theo quy định của Nhà nước."
        )

        dispatcher.utter_message(text=tra_loi)
        return []


class ActionTraCuuDieuKienHocBong(Action):
    def name(self) -> Text:
        return "action_tra_cuu_dieu_kien_hoc_bong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if not ten_nganh:
            dispatcher.utter_message(
                text="Bạn muốn biết điều kiện học bổng của ngành nào vậy?"
            )
            return []

        tra_loi = (
            f"Để được xét học bổng ngành {ten_nganh} tại PTIT, sinh viên cần:\n"
            f"- Đạt kết quả học tập từ khá, giỏi trở lên.\n"
            f"- Có điểm rèn luyện tốt.\n"
            f"- Không vi phạm kỷ luật.\n"
            f"👉 Riêng **học bổng tài năng** yêu cầu sinh viên xuất sắc hoặc đạt giải thưởng nghiên cứu khoa học, cuộc thi chuyên môn."
        )

        dispatcher.utter_message(text=tra_loi)
        return []


class ActionTraCuuGiaTriHocBong(Action):
    def name(self) -> Text:
        return "action_tra_cuu_gia_tri_hoc_bong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if not ten_nganh:
            dispatcher.utter_message(
                text="Bạn muốn biết giá trị học bổng của ngành nào vậy?"
            )
            return []

        tra_loi = (
            f"Học bổng ngành {ten_nganh} tại PTIT thường có giá trị như sau:\n"
            f"- **Học bổng khuyến khích học tập**: khoảng 1 đến 1,5 tháng học phí.\n"
            f"- **Học bổng tài năng**: mức cao hơn, có thể từ vài triệu đồng/đợt.\n"
            f"- **Học bổng doanh nghiệp tài trợ**: có thể toàn phần hoặc theo mức hỗ trợ riêng của từng doanh nghiệp.\n"
            f"👉 Như vậy, sinh viên xuất sắc hoàn toàn có thể nhận học bổng toàn phần."
        )

        dispatcher.utter_message(text=tra_loi)
        return []

class ActionTraCuuKhaiNiemNghienCuuKhoaHoc(Action):
    def name(self) -> Text:
        return "action_tra_cuu_khai_niem_nghien_cuu_khoa_hoc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tra_loi = (
            "Nghiên cứu khoa học (NCKH) là quá trình sinh viên và giảng viên tìm tòi, "
            "khám phá, sáng tạo tri thức mới, hoặc vận dụng kiến thức đã có để giải quyết các vấn đề thực tiễn. "
            "Trong trường đại học, NCKH có thể là làm đề tài, báo cáo, tham gia hội nghị, "
            "chứ không chỉ đơn thuần là viết luận văn."
        )

        dispatcher.utter_message(text=tra_loi)
        return []

class ActionTraCuuCoHoiNghienCuuKhoaHoc(Action):
    def name(self) -> Text:
        return "action_tra_cuu_co_hoi_nghien_cuu_khoa_hoc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if not ten_nganh:
            dispatcher.utter_message(
                text="Bạn muốn biết cơ hội nghiên cứu khoa học của ngành nào vậy?"
            )
            return []

        tra_loi = (
            f"Sinh viên ngành {ten_nganh} tại PTIT đều có cơ hội tham gia nghiên cứu khoa học. "
            f"Học viện có các câu lạc bộ học thuật, nhóm nghiên cứu và giảng viên trực tiếp hướng dẫn. "
            f"👉 Như vậy, bạn hoàn toàn có thể làm đề tài, tham gia dự án nghiên cứu ngay từ khi còn là sinh viên."
        )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionTraCuuDieuKienNghienCuuKhoaHoc(Action):
    def name(self) -> Text:
        return "action_tra_cuu_dieu_kien_nghien_cuu_khoa_hoc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tra_loi = (
            "Điều kiện để tham gia nghiên cứu khoa học tại PTIT khá linh hoạt:\n"
            "- Sinh viên bất kỳ năm nào cũng có thể đăng ký, nhưng từ năm 2 trở đi sẽ thuận lợi hơn do đã có kiến thức nền.\n"
            "- Cần có ý tưởng hoặc mong muốn tham gia đề tài.\n"
            "- Đăng ký với giảng viên hướng dẫn hoặc tham gia nhóm nghiên cứu.\n"
            "👉 Quan trọng nhất là tinh thần ham học hỏi và chủ động tìm tòi."
        )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionTraCuuLoiIchNghienCuuKhoaHoc(Action):
    def name(self) -> Text:
        return "action_tra_cuu_loi_ich_nghien_cuu_khoa_hoc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tra_loi = (
            "Tham gia nghiên cứu khoa học (NCKH) mang lại nhiều lợi ích cho sinh viên:\n"
            "- Rèn luyện tư duy sáng tạo, kỹ năng giải quyết vấn đề.\n"
            "- Nâng cao kiến thức chuyên môn, tiếp cận công nghệ mới.\n"
            "- Cơ hội nhận học bổng, giải thưởng và cộng điểm rèn luyện.\n"
            "- Tăng lợi thế khi xin học bổng du học, thực tập và việc làm sau khi ra trường.\n"
            "👉 Nói cách khác, NCKH vừa giúp học tập, vừa mở rộng cơ hội nghề nghiệp."
        )

        dispatcher.utter_message(text=tra_loi)
        return []


class ActionTraCuuNoiDungNghienCuuKhoaHoc(Action):
    def name(self) -> Text:
        return "action_tra_cuu_noi_dung_nghien_cuu_khoa_hoc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if ten_nganh:
            tra_loi = (
                f"Sinh viên ngành {ten_nganh} có thể tham gia nghiên cứu khoa học trong nhiều mảng: "
                f"thiết kế hệ thống, phát triển sản phẩm mới, ứng dụng công nghệ hiện đại. "
                f"Ví dụ: đề tài liên quan đến {ten_nganh} như nghiên cứu chip, mạch tích hợp, IoT, robot, trí tuệ nhân tạo."
            )
        else:
            tra_loi = (
                "Nội dung nghiên cứu khoa học của sinh viên rất đa dạng, "
                "bao gồm thiết kế mạch điện tử, tự động hóa, vi mạch, IoT, trí tuệ nhân tạo, "
                "ứng dụng công nghệ trong viễn thông và năng lượng. "
                "👉 Mỗi ngành sẽ có những mảng nghiên cứu đặc thù phù hợp."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionPhongLabDanhSach(Action):
    def name(self) -> Text:
        return "action_phong_lab_danh_sach"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tra_loi = (
            "Hiện tại, khoa Điện tử của PTIT có nhiều phòng thí nghiệm và thực hành cho sinh viên, gồm:\n"
            "- Phòng Lab Điện tử sáng tạo\n"
            "- Phòng Lab Vi mạch bán dẫn\n"
            "- Phòng Lab Tự động hóa và Robot\n"
            "- Phòng Lab IoT và Hệ thống nhúng\n"
            "- Các phòng thực hành Điện – Điện tử cơ bản\n\n"
            "👉 Sinh viên có thể tham gia học tập, nghiên cứu và làm đồ án tại các phòng lab này."
        )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionPhongLabThietBi(Action):
    def name(self) -> Text:
        return "action_phong_lab_thiet_bi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_lab = next(tracker.get_latest_entity_values("ten_lab"), None)

        if ten_lab:
            tra_loi = (
                f"Phòng lab {ten_lab} được trang bị đầy đủ máy móc và thiết bị phục vụ học tập, nghiên cứu, "
                f"bao gồm: máy tính cấu hình mạnh, thiết bị đo lường (oscilloscope, máy phát tín hiệu), "
                f"kit vi xử lý, board mạch, robot, cảm biến, và các thiết bị IoT hiện đại."
            )
        else:
            tra_loi = (
                "Các phòng lab của khoa Điện tử PTIT được trang bị hiện đại: "
                "máy đo oscilloscope, máy phát tín hiệu, robot, bộ kit IoT, FPGA, "
                "thiết bị tự động hóa, hệ thống điều khiển và mạch điện tử thực hành."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionPhongLabDieuKienSuDung(Action):
    def name(self) -> Text:
        return "action_phong_lab_dieu_kien_su_dung"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tra_loi = (
            "Điều kiện sử dụng phòng lab của khoa Điện tử PTIT:\n"
            "- Sinh viên các ngành thuộc khoa Điện tử đều có thể đăng ký sử dụng.\n"
            "- Thông thường, sinh viên từ năm 2 trở lên sẽ được học và thực hành trong lab.\n"
            "- Phải đăng ký với bộ môn/phòng quản lý để được cấp quyền sử dụng.\n"
            "- Tuân thủ các quy định an toàn, không mang thức ăn, nước uống vào lab.\n"
            "- Khi làm việc phải có sự giám sát của giảng viên hoặc kỹ thuật viên."
        )

        dispatcher.utter_message(text=tra_loi)
        return []

class ActionPhongLabGioMoCua(Action):
    def name(self) -> Text:
        return "action_phong_lab_gio_mo_cua"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_lab = next(tracker.get_latest_entity_values("ten_lab"), None)

        if ten_lab:
            tra_loi = (
                f"Phòng lab {ten_lab} của khoa Điện tử PTIT thường mở cửa từ **8h00 - 17h00**, "
                f"từ **thứ 2 đến thứ 6**. Một số lab có thể mở thêm buổi tối hoặc cuối tuần "
                f"nếu có lớp học, đồ án hoặc nghiên cứu được đăng ký trước."
            )
        else:
            tra_loi = (
                "Các phòng lab của khoa Điện tử PTIT thường mở cửa trong giờ hành chính "
                "(8h00 - 17h00, thứ 2 đến thứ 6). Ngoài ra, một số lab có thể mở buổi tối hoặc cuối tuần "
                "cho sinh viên làm đồ án hoặc nghiên cứu, nếu có đăng ký với giảng viên/phòng quản lý."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionPhongLabKhoaHocThucHanh(Action):
    def name(self) -> Text:
        return "action_phong_lab_khoa_hoc_thuc_hanh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_lab = next(tracker.get_latest_entity_values("ten_lab"), None)

        if ten_lab:
            tra_loi = (
                f"Phòng lab {ten_lab} được sử dụng cho nhiều học phần thực hành, "
                f"như: Thực hành Điện – Điện tử, Vi xử lý – Vi điều khiển, Hệ thống nhúng, "
                f"Điều khiển tự động, IoT, và các học phần liên quan đến chuyên ngành."
            )
        else:
            tra_loi = (
                "Các phòng lab của khoa Điện tử PTIT phục vụ cho nhiều môn học thực hành: "
                "Điện – Điện tử cơ bản, Mạch điện, Kỹ thuật số, Vi xử lý – Vi điều khiển, "
                "Thiết kế vi mạch, Hệ thống nhúng, IoT, Robot và Tự động hóa."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionPhongLabLienHe(Action):
    def name(self) -> Text:
        return "action_phong_lab_lien_he"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_lab = next(tracker.get_latest_entity_values("ten_lab"), None)

        if ten_lab:
            tra_loi = (
                f"Phòng lab {ten_lab} do các giảng viên trong khoa Điện tử phụ trách. "
                f"Bạn có thể liên hệ qua Văn phòng Khoa Điện tử PTIT hoặc email của giảng viên phụ trách lab. "
                f"Thông tin chi tiết thường được công bố trên website chính thức hoặc bảng thông báo của khoa."
            )
        else:
            tra_loi = (
                "Các phòng lab của khoa Điện tử PTIT đều có giảng viên phụ trách. "
                "Bạn có thể liên hệ trực tiếp qua Văn phòng Khoa Điện tử hoặc email công vụ trên website PTIT. "
                "Ngoài ra, một số lab còn có fanpage/website riêng để hỗ trợ sinh viên."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionPhongLabLienKetDoanhNghiep(Action):
    def name(self) -> Text:
        return "action_phong_lab_lien_ket_doanh_nghiep"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_lab = next(tracker.get_latest_entity_values("ten_lab"), None)

        if ten_lab:
            tra_loi = (
                f"Phòng lab {ten_lab} của khoa Điện tử PTIT có hợp tác với nhiều doanh nghiệp "
                f"trong lĩnh vực điện tử, viễn thông, và công nghệ bán dẫn. "
                f"Các đối tác này thường tài trợ thiết bị, học bổng, hoặc phối hợp tổ chức "
                f"các dự án nghiên cứu, thực tập cho sinh viên."
            )
        else:
            tra_loi = (
                "Các phòng lab của khoa Điện tử PTIT đều có liên kết với doanh nghiệp, "
                "nhất là trong các lĩnh vực: thiết kế vi mạch, viễn thông, IoT, tự động hóa. "
                "Doanh nghiệp tham gia có thể tài trợ thiết bị, đồng hành nghiên cứu hoặc mở chương trình thực tập."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionTraCuuCoHoiViecLam(Action):
    def name(self) -> Text:
        return "action_tra_cuu_co_hoi_viec_lam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if ten_nganh:
            tra_loi = (
                f"Sinh viên ngành {ten_nganh} sau khi tốt nghiệp có thể làm việc tại các công ty, "
                f"tập đoàn trong lĩnh vực điện tử, viễn thông, năng lượng, tự động hóa, công nghệ bán dẫn. "
                f"Cơ hội nghề nghiệp bao gồm kỹ sư thiết kế, lập trình hệ thống, quản lý kỹ thuật, "
                f"và nghiên cứu phát triển sản phẩm."
            )
        else:
            tra_loi = (
                "Sinh viên khoa Điện tử PTIT sau khi tốt nghiệp có nhiều cơ hội nghề nghiệp: "
                "làm kỹ sư tại doanh nghiệp điện tử, viễn thông, công nghệ bán dẫn, "
                "tham gia nghiên cứu, hoặc khởi nghiệp trong lĩnh vực công nghệ."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionTraCuuNhuCauTuyenDung(Action):
    def name(self) -> Text:
        return "action_tra_cuu_nhu_cau_tuyen_dung"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if ten_nganh:
            tra_loi = (
                f"Ngành {ten_nganh} hiện có nhu cầu tuyển dụng rất cao trên thị trường lao động, "
                f"đặc biệt khi Việt Nam đang phát triển mạnh mẽ về công nghệ số, IoT và bán dẫn. "
                f"Nhiều doanh nghiệp trong và ngoài nước liên tục tuyển kỹ sư {ten_nganh}."
            )
        else:
            tra_loi = (
                "Các ngành thuộc khoa Điện tử PTIT đều có nhu cầu tuyển dụng lớn. "
                "Doanh nghiệp công nghệ, viễn thông, năng lượng, và sản xuất thiết bị điện tử "
                "đều cần kỹ sư tốt nghiệp từ các ngành này."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionTraCuuViecLamQuocTe(Action):
    def name(self) -> Text:
        return "action_tra_cuu_viec_lam_quoc_te"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if ten_nganh:
            tra_loi = (
                f"Sinh viên ngành {ten_nganh} sau khi tốt nghiệp hoàn toàn có cơ hội làm việc tại nước ngoài, "
                f"nhất là ở Nhật Bản, Hàn Quốc, Mỹ, châu Âu, nơi có nhiều tập đoàn điện tử và bán dẫn. "
                f"PTIT cũng có các chương trình liên kết, hỗ trợ sinh viên tiếp cận thị trường quốc tế."
            )
        else:
            tra_loi = (
                "Sinh viên khoa Điện tử PTIT có thể làm việc tại các tập đoàn quốc tế "
                "trong lĩnh vực điện tử, viễn thông, công nghệ thông tin và bán dẫn. "
                "Nhiều sinh viên đã đi làm tại Nhật, Hàn, Mỹ sau khi tốt nghiệp."
            )

        dispatcher.utter_message(text=tra_loi)
        return []
class ActionTraCuuLuongNganh(Action):
    def name(self) -> Text:
        return "action_tra_cuu_luong_nganh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ten_nganh = next(tracker.get_latest_entity_values("ten_nganh"), None)

        if ten_nganh:
            tra_loi = (
                f"Sinh viên ngành {ten_nganh} sau khi ra trường có mức lương khởi điểm "
                f"khoảng 10–15 triệu đồng/tháng. Với kinh nghiệm và làm ở các tập đoàn lớn, "
                f"mức thu nhập có thể từ 20–30 triệu đồng/tháng hoặc cao hơn."
            )
        else:
            tra_loi = (
                "Sinh viên các ngành của khoa Điện tử PTIT thường có lương khởi điểm 10–15 triệu/tháng. "
                "Nếu làm việc tại doanh nghiệp quốc tế hoặc trong lĩnh vực bán dẫn, "
                "thu nhập có thể trên 20 triệu/tháng."
            )

        dispatcher.utter_message(text=tra_loi)
        return []

class ActionTraCuuDieuKienTuyenSinh(Action):
    def name(self):
        return "action_tra_cuu_dieu_kien_tuyen_sinh"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")

        answer = (
            f"Để xét tuyển vào ngành {ten_nganh if ten_nganh else ''} tại PTIT, thí sinh cần đáp ứng các điều kiện chung:\n"
            "- Tốt nghiệp THPT hoặc tương đương.\n"
            "- Tham gia xét tuyển theo một trong các phương thức do PTIT quy định (thi THPT, xét học bạ, chứng chỉ quốc tế, đánh giá năng lực...).\n"
            "- Đạt mức điểm chuẩn tối thiểu của ngành theo từng năm tuyển sinh.\n"
            "- Một số ngành có thể yêu cầu thêm chứng chỉ tiếng Anh quốc tế hoặc điểm thi ngoại ngữ tùy phương thức.\n\n"
            "📌 Chi tiết xem tại: https://portal.ptit.edu.vn/tuyen-sinh/"
        )

        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuQuyTrinhNhapHoc(Action):
    def name(self):
        return "action_tra_cuu_quy_trinh_nhap_hoc"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")

        answer = (
            f"Quy trình nhập học cho ngành {ten_nganh if ten_nganh else ''} tại PTIT gồm các bước cơ bản:\n"
            "1. Xác nhận nhập học trực tuyến trên hệ thống của PTIT.\n"
            "2. Nộp hồ sơ nhập học đầy đủ theo quy định.\n"
            "3. Đóng học phí và các khoản phí khác theo hướng dẫn.\n"
            "4. Tham gia tuần sinh hoạt công dân đầu khóa.\n\n"
            "📌 Hướng dẫn chi tiết tại: https://portal.ptit.edu.vn/huong-dan-nhap-hoc/"
        )

        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuHoSoNhapHoc(Action):
    def name(self):
        return "action_tra_cuu_ho_so_nhap_hoc"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")

        answer = (
            f"Hồ sơ nhập học ngành {ten_nganh if ten_nganh else ''} tại PTIT thường bao gồm:\n"
            "- Giấy báo trúng tuyển (bản chính).\n"
            "- Học bạ THPT (bản sao công chứng).\n"
            "- Bằng tốt nghiệp THPT hoặc giấy chứng nhận tốt nghiệp tạm thời.\n"
            "- Giấy khai sinh (bản sao công chứng).\n"
            "- Căn cước công dân/CMND (bản sao công chứng).\n"
            "- Ảnh thẻ 3x4 hoặc 4x6.\n"
            "- Các giấy tờ ưu tiên (nếu có).\n"
            "- Biên lai nộp học phí.\n\n"
            "📌 Danh mục hồ sơ đầy đủ được cập nhật tại: https://portal.ptit.edu.vn/ho-so-nhap-hoc/"
        )

        dispatcher.utter_message(text=answer)
        return []
class ActionTraCuuKienThucCoBan(Action):
    def name(self):
        return "action_tra_cuu_kien_thuc_co_ban"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Sinh viên ngành {ten_nganh if ten_nganh else ''} tại PTIT cần có kiến thức cơ bản sau:\n"
            "- Kiến thức khoa học tự nhiên và toán học để làm nền tảng cho các môn chuyên ngành.\n"
            "- Kiến thức cơ sở về điện, điện tử, mạch, tín hiệu, máy tính và lập trình.\n"
            "- Hiểu biết chung về kinh tế, xã hội, pháp luật và chính trị.\n\n"
            "📌 Đây là chuẩn đầu ra về kiến thức nền tảng được PTIT quy định."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuKienThucChuyenMon(Action):
    def name(self):
        return "action_tra_cuu_kien_thuc_chuyen_mon"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Chuẩn đầu ra về kiến thức chuyên môn của ngành {ten_nganh if ten_nganh else ''} tại PTIT gồm:\n"
            "- Nắm vững các môn chuyên ngành như: mạch điện, điện tử công suất, điều khiển tự động, vi mạch, IoT, hệ thống nhúng...\n"
            "- Hiểu biết về thiết kế, chế tạo, vận hành và bảo trì hệ thống điện - điện tử.\n"
            "- Có khả năng ứng dụng CNTT, phần mềm mô phỏng, công cụ thiết kế kỹ thuật trong công việc.\n\n"
            "📌 Đây là khối kiến thức chuyên sâu phục vụ nghề nghiệp."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuKyNangNgheNghiep(Action):
    def name(self):
        return "action_tra_cuu_ky_nang_nghe_nghiep"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Sinh viên ngành {ten_nganh if ten_nganh else ''} được trang bị kỹ năng nghề nghiệp:\n"
            "- Kỹ năng thiết kế, phân tích, lắp ráp và vận hành các hệ thống điện tử.\n"
            "- Kỹ năng sử dụng thành thạo các thiết bị đo lường, kiểm tra, thí nghiệm.\n"
            "- Kỹ năng lập trình, mô phỏng và triển khai giải pháp kỹ thuật.\n"
            "- Khả năng nghiên cứu khoa học và phát triển sản phẩm mới.\n\n"
            "📌 Đây là những kỹ năng cứng theo chuẩn đầu ra PTIT."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuKyNangMem(Action):
    def name(self):
        return "action_tra_cuu_ky_nang_mem"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Sinh viên ngành {ten_nganh if ten_nganh else ''} tại PTIT cần phát triển kỹ năng mềm:\n"
            "- Kỹ năng giao tiếp, làm việc nhóm và thuyết trình.\n"
            "- Kỹ năng quản lý thời gian, lập kế hoạch và giải quyết vấn đề.\n"
            "- Kỹ năng tự học, nghiên cứu độc lập và sáng tạo.\n"
            "- Kỹ năng sử dụng ngoại ngữ (đặc biệt là tiếng Anh chuyên ngành).\n\n"
            "📌 Đây là chuẩn kỹ năng mềm bắt buộc đối với sinh viên PTIT."
        )
        dispatcher.utter_message(text=answer)
        return []
class ActionTraCuuChuongTrinhHocNganh(Action):
    def name(self):
        return "action_tra_cuu_chuong_trinh_hoc_nganh"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Chương trình học ngành {ten_nganh if ten_nganh else ''} tại PTIT thường được cấu trúc như sau:\n"
            "- Khối kiến thức đại cương: Toán, Lý, Tin học, Chính trị, Ngoại ngữ (khoảng 50 tín chỉ).\n"
            "- Khối kiến thức cơ sở ngành: mạch điện, điện tử, tín hiệu – hệ thống, điều khiển, lập trình (50-60 tín chỉ).\n"
            "- Khối kiến thức chuyên ngành: các môn chuyên sâu theo định hướng (60-70 tín chỉ).\n"
            "- Thực tập, đồ án và khóa luận tốt nghiệp (10-15 tín chỉ).\n\n"
            "📌 Tổng khối lượng khoảng 130 – 150 tín chỉ tùy ngành."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuChuyenNganhTrongNganh(Action):
    def name(self):
        return "action_tra_cuu_chuyen_nganh_trong_nganh"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Ngành {ten_nganh if ten_nganh else ''} tại PTIT có các chuyên ngành/định hướng đào tạo, ví dụ:\n"
            "- Kỹ thuật Điều khiển và Tự động hóa.\n"
            "- Công nghệ Vi mạch bán dẫn.\n"
            "- Công nghệ Kỹ thuật Điện, điện tử.\n\n"
            "📌 Tùy từng năm đào tạo, khoa có thể điều chỉnh, cập nhật chuyên ngành phù hợp nhu cầu thực tế."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuTinChiThucTapDoAn(Action):
    def name(self):
        return "action_tra_cuu_tin_chi_thuc_tap_do_an"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Sinh viên ngành {ten_nganh if ten_nganh else ''} tại PTIT phải hoàn thành:\n"
            "- Thực tập doanh nghiệp: khoảng 3 – 5 tín chỉ.\n"
            "- Đồ án tốt nghiệp/khóa luận: khoảng 6 – 10 tín chỉ.\n\n"
            "📌 Đây là phần bắt buộc để rèn luyện kỹ năng thực tế và làm cơ sở bảo vệ tốt nghiệp."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuKetNoiDoanhNghiep(Action):
    def name(self):
        return "action_tra_cuu_ket_noi_doanh_nghiep"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "Học viện Công nghệ Bưu chính Viễn thông (PTIT) có nhiều kết nối với doanh nghiệp để hỗ trợ sinh viên:\n"
            "- Các tập đoàn, công ty lớn trong và ngoài nước: VNPT, Viettel, Samsung, Intel, Synopsys...\n"
            "- Doanh nghiệp hỗ trợ học bổng, học liệu, phòng lab và các dự án nghiên cứu.\n"
            "- Hàng năm có ngày hội việc làm, chương trình internship và hội thảo nghề nghiệp.\n\n"
            "📌 Nhờ vậy, sinh viên có nhiều cơ hội thực tập, việc làm và khởi nghiệp ngay từ khi còn học."
        )
        dispatcher.utter_message(text=answer)
        return []
class ActionTraCuuThongTinLienHe(Action):
    def name(self):
        return "action_tra_cuu_thong_tin_lien_he"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "📌 Thông tin liên hệ tuyển sinh PTIT:\n"
            "- Phòng Tuyển sinh: Tầng 1, Nhà A1, Học viện Công nghệ Bưu chính Viễn thông.\n"
            "- Điện thoại: 024 3352 8121 (Hà Nội), 028 3829 4216 (TP.HCM).\n"
            "- Email: tuyensinh@ptit.edu.vn\n"
            "- Fanpage: https://www.facebook.com/tuyensinhptit\n"
            "- Website: https://tuyensinh.ptit.edu.vn\n"
            "- Khoa Kỹ thuật Điện tử: Tòa nhà A3 – PTIT Hà Đông."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuPhuHopNu(Action):
    def name(self):
        return "action_tra_cuu_phu_hop_nu"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Nữ học ngành {ten_nganh if ten_nganh else ''} hoàn toàn phù hợp 👍.\n"
            "- Các môn học tập trung vào tư duy logic, thiết kế, lập trình, nghiên cứu.\n"
            "- Công việc hiện nay thiên về công nghệ, mô phỏng, phân tích số liệu, không đòi hỏi sức khỏe nhiều.\n"
            "📌 Rất nhiều sinh viên nữ của PTIT đã học và thành công trong ngành này."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuDacThuCongViecNu(Action):
    def name(self):
        return "action_tra_cuu_dac_thu_cong_viec_nu"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Đặc thù công việc ngành {ten_nganh if ten_nganh else ''} đối với nữ:\n"
            "- Không yêu cầu làm việc nặng nhọc.\n"
            "- Chủ yếu làm ở văn phòng, phòng lab, công ty công nghệ.\n"
            "- Một số công việc có thể đi công trình nhưng sinh viên nữ thường chọn hướng nghiên cứu, thiết kế, giảng dạy hoặc quản lý dự án.\n"
            "📌 Vì vậy nữ hoàn toàn có thể yên tâm theo ngành này."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuViecLamChoNu(Action):
    def name(self):
        return "action_tra_cuu_viec_lam_cho_nu"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Cơ hội việc làm cho nữ ngành {ten_nganh if ten_nganh else ''} rất rộng mở:\n"
            "- Kỹ sư thiết kế, lập trình, kiểm thử trong công ty công nghệ.\n"
            "- Nghiên cứu viên, giảng viên tại trường đại học, viện nghiên cứu.\n"
            "- Chuyên viên kỹ thuật, quản lý dự án, tư vấn giải pháp.\n"
            "- Các công ty lớn như Samsung, Intel, VNPT, Viettel đều tuyển nhiều nữ kỹ sư.\n"
            "📌 Thực tế sinh viên nữ của PTIT ra trường có tỉ lệ việc làm rất cao."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuCoHoiThangTienNu(Action):
    def name(self):
        return "action_tra_cuu_co_hoi_thang_tien_nu"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        answer = (
            f"Nữ học ngành {ten_nganh if ten_nganh else ''} có nhiều cơ hội thăng tiến:\n"
            "- Có thể trở thành quản lý kỹ thuật, trưởng nhóm, giám đốc dự án.\n"
            "- Nhiều nữ kỹ sư tại VNPT, Viettel, Samsung đã giữ vị trí cao.\n"
            "- Cơ hội làm giảng viên, nghiên cứu sinh, du học hoặc khởi nghiệp.\n"
            "📌 Ngành kỹ thuật không hề giới hạn nam hay nữ, quan trọng là năng lực và đam mê."
        )
        dispatcher.utter_message(text=answer)
        return []
class ActionPtitGioiThieuLichSu(Action):
    def name(self):
        return "action_ptit_gioi_thieu_lich_su"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "📖 **Lịch sử PTIT**:\n"
            "- Học viện Công nghệ Bưu chính Viễn thông (PTIT) được thành lập năm 1997, "
            "trực thuộc Bộ Thông tin và Truyền thông.\n"
            "- Tiền thân của PTIT là Trường Đào tạo Bưu cục, sau phát triển thành Trường Đại học Bưu chính Viễn thông.\n"
            "- PTIT là trung tâm đào tạo, nghiên cứu và chuyển giao công nghệ hàng đầu trong lĩnh vực CNTT và Điện tử Viễn thông.\n"
            "🌟 Với hơn 25 năm phát triển, PTIT đã trở thành một trong những trường đại học trọng điểm quốc gia."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionPtitGioiThieuSuMenhTamNhin(Action):
    def name(self):
        return "action_ptit_gioi_thieu_su_menh_tam_nhin"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "🎯 **Sứ mệnh & Tầm nhìn của PTIT**:\n"
            "- **Sứ mệnh**: Đào tạo nguồn nhân lực chất lượng cao trong các lĩnh vực CNTT, Điện tử Viễn thông, Kinh tế và Quản lý; "
            "nghiên cứu khoa học và chuyển giao công nghệ phục vụ sự phát triển của ngành Thông tin và Truyền thông cũng như đất nước.\n"
            "- **Tầm nhìn**: Trở thành trường đại học trọng điểm quốc gia, có uy tín trong khu vực châu Á về đào tạo, nghiên cứu và đổi mới sáng tạo.\n"
            "- **Giá trị cốt lõi**: Chất lượng – Sáng tạo – Trách nhiệm – Hội nhập."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionPtitGioiThieuCoCauToChuc(Action):
    def name(self):
        return "action_ptit_gioi_thieu_co_cau_to_chuc"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "🏛 **Cơ cấu tổ chức của PTIT**:\n"
            "- **Ban Giám đốc Học viện**: Giám đốc và các Phó Giám đốc.\n"
            "- **Các khoa đào tạo**:\n"
            "  • Khoa Công nghệ Thông tin\n"
            "  • Khoa Kỹ thuật Điện tử 1\n"
            "  • Khoa Kỹ thuật Điện tử 2\n"
            "  • Khoa Viễn thông 1\n"
            "  • Khoa Viễn thông 2\n"
            "  • Khoa Quốc tế và Đào tạo sau đại học\n"
            "  • Khoa Cơ bản\n"
            "  • Khoa Quản trị Kinh doanh\n"
            "- **Các phòng chức năng**: Đào tạo, Công tác sinh viên, Hành chính – Tổng hợp, Khoa học công nghệ, Hợp tác quốc tế...\n"
            "- **Các viện, trung tâm nghiên cứu** trực thuộc Học viện.\n\n"
            "👉 Nhờ cơ cấu tổ chức này, PTIT vừa đảm bảo chất lượng đào tạo, vừa đẩy mạnh nghiên cứu và hợp tác doanh nghiệp."
        )
        dispatcher.utter_message(text=answer)
        return []
class ActionPtitGioiThieuDiaChi(Action):
    def name(self):
        return "action_ptit_gioi_thieu_dia_chi"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "📍 **Địa chỉ các cơ sở của PTIT**:\n"
            "- **Cơ sở Hà Nội (trụ sở chính)**: 122 Hoàng Quốc Việt, Cầu Giấy, Hà Nội.\n"
            "- **Cơ sở Hà Đông**: Km10, Nguyễn Trãi, Hà Đông, Hà Nội.\n"
            "- **Cơ sở TP. Hồ Chí Minh**: 11 Nguyễn Đình Chiểu, Quận 1, TP.HCM.\n"
            "👉 Sinh viên có thể học tập và nghiên cứu tại cả hai cơ sở Hà Nội và TP.HCM."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionPtitGioiThieuQuyMoDaoTao(Action):
    def name(self):
        return "action_ptit_gioi_thieu_quy_mo_dao_tao"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "🎓 **Quy mô đào tạo của PTIT**:\n"
            "- PTIT đào tạo hơn **30.000 sinh viên, học viên** mỗi năm.\n"
            "- Các bậc đào tạo: Đại học, Sau đại học (Thạc sĩ, Tiến sĩ).\n"
            "- Trường có **9 khoa đào tạo** và nhiều viện nghiên cứu, trung tâm hỗ trợ.\n"
            "- Đội ngũ gồm khoảng **700 giảng viên, cán bộ**; trong đó nhiều PGS, TS, chuyên gia đầu ngành.\n"
            "🌟 PTIT là một trong những cơ sở đào tạo lớn và uy tín hàng đầu trong lĩnh vực CNTT và Điện tử Viễn thông tại Việt Nam."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionPtitGioiThieuThanhTuuNoiBat(Action):
    def name(self):
        return "action_ptit_gioi_thieu_thanh_tuu_noi_bat"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "🏆 **Thành tựu nổi bật của PTIT**:\n"
            "- Được Nhà nước công nhận là **trường trọng điểm quốc gia** trong lĩnh vực CNTT và Viễn thông.\n"
            "- Nhiều năm liền đạt danh hiệu **Huân chương Lao động** các hạng.\n"
            "- Sinh viên PTIT thường xuyên đạt giải cao trong các kỳ thi quốc gia và quốc tế: Olympic Tin học, Olympic Toán học, ACM/ICPC.\n"
            "- Học viện có nhiều **đề tài nghiên cứu khoa học cấp Nhà nước và cấp Bộ** được ứng dụng thực tiễn.\n"
            "- Là đối tác chiến lược của nhiều tập đoàn lớn: Viettel, VNPT, FPT, Samsung, Huawei...\n"
            "🌐 PTIT đang mở rộng hợp tác quốc tế với hơn 50 trường đại học và tổ chức nghiên cứu trên thế giới."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionPtitGioiThieuLienHe(Action):
    def name(self):
        return "action_ptit_gioi_thieu_lien_he"

    def run(self, dispatcher, tracker, domain):
        answer = (
            "📞 **Thông tin liên hệ PTIT**:\n"
            "- **Phòng Tuyển sinh & Công tác sinh viên (CS1 - Hà Nội):**\n"
            "  • Địa chỉ: 122 Hoàng Quốc Việt, Cầu Giấy, Hà Nội.\n"
            "  • Điện thoại: (024) 3756 2186.\n"
            "  • Email: tuyensinh@ptit.edu.vn\n\n"
            "- **Phòng Tuyển sinh (CS2 - TP.HCM):**\n"
            "  • Địa chỉ: 11 Nguyễn Đình Chiểu, Quận 1, TP.HCM.\n"
            "  • Điện thoại: (028) 3829 3825.\n\n"
            "- **Website chính thức**: https://ptit.edu.vn\n"
            "- **Fanpage Facebook**: https://www.facebook.com/HocvienPTIT\n\n"
            "👉 Bạn có thể liên hệ trực tiếp để được tư vấn chi tiết về tuyển sinh và đào tạo."
        )
        dispatcher.utter_message(text=answer)
        return []


class ActionTraCuuGiangVien(Action):
    def name(self) -> Text:
        return "action_tra_cuu_giang_vien"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        ten_khoa = tracker.get_slot("ten_khoa")

        if ten_nganh:
            dispatcher.utter_message(
                text=f"Ngành {ten_nganh} hiện do các giảng viên của khoa Kỹ thuật Điện tử phụ trách. "
                     f"Ví dụ: PGS.TS Nguyễn Văn A, TS Trần Thị B, ThS Lê Văn C..."
            )
        elif ten_khoa:
            dispatcher.utter_message(
                text=f"Khoa {ten_khoa} có đội ngũ giảng viên trình độ cao, gồm nhiều PGS, TS và ThS. "
                     f"Danh sách cụ thể được công bố trên website chính thức của khoa."
            )
        else:
            dispatcher.utter_message(
                text="Bạn vui lòng cung cấp tên ngành hoặc tên khoa để tra cứu giảng viên nhé."
            )
        return []


class ActionTraCuuTrinhDoGiangVien(Action):
    def name(self) -> Text:
        return "action_tra_cuu_trinh_do_giang_vien"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")
        ten_khoa = tracker.get_slot("ten_khoa")

        if ten_nganh:
            dispatcher.utter_message(
                text=f"Đội ngũ giảng viên ngành {ten_nganh} chủ yếu có học vị tiến sĩ và thạc sĩ, "
                     f"nhiều giảng viên tốt nghiệp từ các trường đại học uy tín trong và ngoài nước."
            )
        elif ten_khoa:
            dispatcher.utter_message(
                text=f"Khoa {ten_khoa} có tỷ lệ tiến sĩ chiếm trên 60%, còn lại là thạc sĩ. "
                     f"Nhiều giảng viên từng tu nghiệp tại nước ngoài."
            )
        else:
            dispatcher.utter_message(
                text="Bạn vui lòng cho biết tên ngành hoặc khoa để tra cứu trình độ giảng viên."
            )
        return []


class ActionTraCuuChuyenMonGiangVien(Action):
    def name(self) -> Text:
        return "action_tra_cuu_chuyen_mon_giang_vien"

    def run(self, dispatcher, tracker, domain):
        ten_mon = tracker.get_slot("ten_mon")
        ten_nganh = tracker.get_slot("ten_nganh")
        ten_khoa = tracker.get_slot("ten_khoa")

        if ten_mon:
            dispatcher.utter_message(
                text=f"Môn {ten_mon} được giảng dạy bởi các giảng viên chuyên sâu trong lĩnh vực này, "
                     f"đảm bảo cả lý thuyết và thực hành."
            )
        elif ten_nganh:
            dispatcher.utter_message(
                text=f"Giảng viên ngành {ten_nganh} có chuyên môn về các lĩnh vực điện tử, vi mạch, tự động hóa, "
                     f"điều khiển và các công nghệ tiên tiến."
            )
        elif ten_khoa:
            dispatcher.utter_message(
                text=f"Khoa {ten_khoa} tập trung nghiên cứu và giảng dạy trong các mảng điện tử, tự động hóa, "
                     f"hệ thống nhúng, viễn thông, và công nghệ bán dẫn."
            )
        else:
            dispatcher.utter_message(
                text="Bạn vui lòng cung cấp tên môn, ngành hoặc khoa để tra cứu chuyên môn giảng viên."
            )
        return []


class ActionTraCuuLichDayGiangVien(Action):
    def name(self) -> Text:
        return "action_tra_cuu_lich_day_giang_vien"

    def run(self, dispatcher, tracker, domain):
        ten_mon = tracker.get_slot("ten_mon")
        ten_nganh = tracker.get_slot("ten_nganh")

        if ten_mon:
            dispatcher.utter_message(
                text=f"Lịch giảng dạy môn {ten_mon} được cập nhật chi tiết trên hệ thống quản lý đào tạo của PTIT. "
                     f"Bạn có thể tra cứu trên website chính thức bằng tài khoản sinh viên."
            )
        elif ten_nganh:
            dispatcher.utter_message(
                text=f"Giảng viên ngành {ten_nganh} giảng dạy theo phân công từng học kỳ. "
                     f"Lịch học chi tiết được thông báo trên cổng thông tin sinh viên."
            )
        else:
            dispatcher.utter_message(
                text="Bạn cần cung cấp tên môn học hoặc ngành để xem lịch dạy cụ thể."
            )
        return []
class ActionCauLacBoDanhSach(Action):
    def name(self) -> Text:
        return "action_cau_lac_bo_danh_sach"

    def run(self, dispatcher, tracker, domain):
        ten_khoa = tracker.get_slot("ten_khoa")
        ten_nganh = tracker.get_slot("ten_nganh")

        if ten_khoa:
            dispatcher.utter_message(
                text=f"Khoa {ten_khoa} có nhiều câu lạc bộ học thuật và kỹ năng dành cho sinh viên, "
                     f"tiêu biểu như CLB Học thuật Điện tử, CLB Sáng tạo và Khởi nghiệp, CLB Nghiên cứu khoa học. "
                     f"Các CLB thường xuyên tổ chức workshop, seminar và cuộc thi chuyên môn."
            )
        elif ten_nganh:
            dispatcher.utter_message(
                text=f"Ngành {ten_nganh} có các CLB sinh viên gắn liền với chuyên môn, ví dụ: CLB Thiết kế chip, "
                     f"CLB Tự động hóa sáng tạo... giúp sinh viên rèn luyện kỹ năng và kết nối học tập."
            )
        else:
            dispatcher.utter_message(
                text="Các khoa và ngành trong PTIT đều có nhiều câu lạc bộ học thuật, kỹ năng và văn nghệ. "
                     "Bạn vui lòng cho biết khoa/ngành cụ thể để mình liệt kê chi tiết nhé."
            )
        return []


class ActionCauLacBoDieuKien(Action):
    def name(self) -> Text:
        return "action_cau_lac_bo_dieu_kien"

    def run(self, dispatcher, tracker, domain):
        ten_khoa = tracker.get_slot("ten_khoa")
        ten_nganh = tracker.get_slot("ten_nganh")

        if ten_khoa or ten_nganh:
            dispatcher.utter_message(
                text=f"Sinh viên của {ten_khoa or ten_nganh} đều có thể tham gia các câu lạc bộ. "
                     f"Điều kiện tham gia rất đơn giản: chỉ cần là sinh viên PTIT, đăng ký với ban chủ nhiệm CLB "
                     f"và có tinh thần nhiệt tình, trách nhiệm. Không yêu cầu kỹ năng đặc biệt, "
                     f"CLB sẽ đào tạo và hỗ trợ thêm cho thành viên mới."
            )
        else:
            dispatcher.utter_message(
                text="Mọi sinh viên PTIT đều có thể tham gia các CLB. "
                     "Chỉ cần đăng ký, có tinh thần học hỏi và tích cực tham gia hoạt động."
            )
        return []


class ActionCauLacBoSuKien(Action):
    def name(self) -> Text:
        return "action_cau_lac_bo_su_kien"

    def run(self, dispatcher, tracker, domain):
        ten_khoa = tracker.get_slot("ten_khoa")
        ten_nganh = tracker.get_slot("ten_nganh")

        if ten_khoa:
            dispatcher.utter_message(
                text=f"Các CLB của khoa {ten_khoa} thường xuyên tổ chức workshop, seminar học thuật, "
                     f"các cuộc thi sáng tạo và hoạt động ngoại khóa. "
                     f"Lịch sự kiện mới nhất được cập nhật trên fanpage của khoa và CLB."
            )
        elif ten_nganh:
            dispatcher.utter_message(
                text=f"CLB thuộc ngành {ten_nganh} thường tổ chức các buổi training kỹ thuật, "
                     f"các cuộc thi thiết kế, và meetup chia sẻ kinh nghiệm. "
                     f"Bạn có thể theo dõi fanpage CLB để biết lịch cụ thể."
            )
        else:
            dispatcher.utter_message(
                text="Các CLB tại PTIT có nhiều sự kiện: workshop, seminar, giao lưu học thuật, "
                     "ngoại khóa và cuộc thi kỹ thuật. Bạn hãy theo dõi fanpage PTIT và các CLB để cập nhật lịch sự kiện."
            )
        return []
class ActionCauLacBoCuocThi(Action):
    def name(self) -> Text:
        return "action_cau_lac_bo_cuoc_thi"

    def run(self, dispatcher, tracker, domain):
        ten_khoa = tracker.get_slot("ten_khoa")
        ten_nganh = tracker.get_slot("ten_nganh")

        if ten_khoa:
            dispatcher.utter_message(
                text=f"Các CLB của khoa {ten_khoa} thường tổ chức nhiều cuộc thi học thuật và sáng tạo "
                     f"như contest lập trình, thiết kế mạch, thi robot và IoT. "
                     f"Sinh viên có thể tham gia để rèn luyện kỹ năng và nhận học bổng, giải thưởng."
            )
        elif ten_nganh:
            dispatcher.utter_message(
                text=f"CLB ngành {ten_nganh} thường xuyên tổ chức các cuộc thi chuyên môn, ví dụ: "
                     f"cuộc thi Thiết kế chip, Robotics Challenge, IoT Hackathon... "
                     f"Đây là sân chơi lớn để sinh viên thử sức và kết nối với doanh nghiệp."
            )
        else:
            dispatcher.utter_message(
                text="Các CLB tại PTIT tổ chức nhiều cuộc thi: Robot Contest, IoT Hackathon, Thiết kế chip, "
                     "cuộc thi sáng tạo khởi nghiệp... Bạn nên theo dõi fanpage CLB để cập nhật lịch thi mới nhất."
            )
        return []


class ActionCauLacBoLienKet(Action):
    def name(self) -> Text:
        return "action_cau_lac_bo_lien_ket"

    def run(self, dispatcher, tracker, domain):
        ten_nganh = tracker.get_slot("ten_nganh")

        if ten_nganh:
            dispatcher.utter_message(
                text=f"Các CLB ngành {ten_nganh} có nhiều hoạt động liên kết với doanh nghiệp: "
                     f"được tài trợ bởi các công ty công nghệ, tổ chức workshop cùng chuyên gia, "
                     f"và giới thiệu thực tập cho sinh viên. Đây là cơ hội tốt để trải nghiệm môi trường doanh nghiệp."
            )
        else:
            dispatcher.utter_message(
                text="Các CLB tại PTIT đều có kết nối doanh nghiệp, nhận được sponsor từ các công ty lớn "
                     "như Viettel, VNPT, FPT, Synopsys… Họ thường tổ chức workshop, training, "
                     "và giới thiệu sinh viên tham gia dự án thực tế."
            )
        return []


class ActionKTXDanhSach(Action):
    def name(self) -> Text:
        return "action_ktx_danh_sach"

    def run(self, dispatcher, tracker, domain):
        ten_khoa = tracker.get_slot("ten_khoa")

        if ten_khoa:
            dispatcher.utter_message(
                text=f"Sinh viên khoa {ten_khoa} được ưu tiên đăng ký ở KTX của Học viện. "
                     f"Hiện PTIT có KTX tại cơ sở Hà Đông (Hà Nội) và cơ sở quận 9 (TP.HCM), "
                     f"cung cấp đầy đủ phòng ở, internet, khu sinh hoạt chung cho sinh viên."
            )
        else:
            dispatcher.utter_message(
                text="PTIT hiện có hệ thống ký túc xá tại:\n"
                     "- **Cơ sở Hà Đông (Hà Nội):** nhiều tòa nhà KTX phục vụ sinh viên.\n"
                     "- **Cơ sở quận 9 (TP.HCM):** khu ký túc xá hiện đại, đầy đủ tiện nghi.\n"
                     "Các KTX đều có khu học tập, thể thao và dịch vụ thiết yếu cho sinh viên."
            )
        return []
class ActionKTXDieuKien(Action):
    def name(self) -> Text:
        return "action_ktx_dieu_kien"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Ký túc xá PTIT ưu tiên cho sinh viên chính quy của Học viện. "
                 "Tất cả sinh viên năm 1 đến năm cuối đều có thể đăng ký ở KTX nếu còn chỗ trống. "
                 "Khi đăng ký, sinh viên cần nộp đơn, thẻ sinh viên và giấy tờ tùy thân. "
                 "Không yêu cầu về điểm số, chỉ cần tuân thủ nội quy của KTX."
        )
        return []


class ActionKTXChiPhi(Action):
    def name(self) -> Text:
        return "action_ktx_chi_phi"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Chi phí ở ký túc xá PTIT khá phù hợp với sinh viên. "
                 "Mức giá dao động tùy loại phòng (4-8 người) khoảng 200.000 - 400.000đ/tháng/sinh viên. "
                 "Điện, nước, internet tính riêng theo mức sử dụng. "
                 "Thông tin chi tiết được thông báo tại ban quản lý KTX mỗi cơ sở."
        )
        return []


class ActionKTXGioMoCua(Action):
    def name(self) -> Text:
        return "action_ktx_gio_mo_cua"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Ký túc xá PTIT mở cửa hàng ngày từ 5h00 sáng đến 23h00 đêm. "
                 "Sinh viên cần tuân thủ giờ ra vào để đảm bảo an ninh. "
                 "KTX có bảo vệ trực 24/7, nhưng sau 23h muốn vào phải đăng ký với quản lý. "
                 "Lịch sinh hoạt chung (giờ giấc, vệ sinh, nội quy) được dán tại bảng tin từng tòa nhà."
        )
        return []
