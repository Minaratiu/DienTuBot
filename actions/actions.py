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
