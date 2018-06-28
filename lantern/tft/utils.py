# from .models import Lot, HoldLot
#
# def apply_lot(user, lot):
#     return HoldLot.create(lot=lot, status='applying', applicant=user)
#
#
# def apply_lots(user, lots):
#     for lot in lots:
#         HoldLot.create(lot=lot, status='applying', applicant=user)
#
#
# def verify(user, lot):
#     hold_lot = HoldLot.objects.get(lot=lot)
#     hold_lot.verifier = user
#     hold_lot.status = 'verified'
#     hold_lot.save()
#
#
# def verify(user, lots):
#     for lot in lots:
#         hold_lot = HoldLot.objects.get(lot=lot)
#         hold_lot.verifier = user
#         hold_lot.status = 'verified'
#         hold_lot.save()
