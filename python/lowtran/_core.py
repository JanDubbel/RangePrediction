"""Generated Python port of LOWTRAN 7. See README.md for provenance."""
import math
from ._runtime import *

def _ft_trans(_state, iph, isourc, iday, anglem, nwl, txpy, vpy, alampy, tracepy, unifpy, sumapy, irradpy, sumvvpy):
    wnlohi_iwlh2o = _state.view(148512, '<i4')
    wnlohi_iwlo3 = _state.view(148572, '<i4')
    wnlohi_iwlco2 = _state.view(148596, '<i4')
    wnlohi_iwlco = _state.view(148640, '<i4')
    wnlohi_iwlch4 = _state.view(148656, '<i4')
    wnlohi_iwln2o = _state.view(148676, '<i4')
    wnlohi_iwlo2 = _state.view(148724, '<i4')
    wnlohi_iwlnh3 = _state.view(148752, '<i4')
    wnlohi_iwlno = _state.view(148764, '<i4')
    wnlohi_iwlno2 = _state.view(148772, '<i4')
    wnlohi_iwlso2 = _state.view(148788, '<i4')
    wnlohi_iwhh2o = _state.view(148808, '<i4')
    wnlohi_iwho3 = _state.view(148868, '<i4')
    wnlohi_iwhco2 = _state.view(148892, '<i4')
    wnlohi_iwhco = _state.view(148936, '<i4')
    wnlohi_iwhch4 = _state.view(148952, '<i4')
    wnlohi_iwhn2o = _state.view(148972, '<i4')
    wnlohi_iwho2 = _state.view(149020, '<i4')
    wnlohi_iwhnh3 = _state.view(149048, '<i4')
    wnlohi_iwhno = _state.view(149060, '<i4')
    wnlohi_iwhno2 = _state.view(149068, '<i4')
    wnlohi_iwhso2 = _state.view(149084, '<i4')
    __BLNK___tx = _state.view(265924, '<f4')
    __BLNK___w = _state.view(266176, '<f4')
    __BLNK___wpath = _state.view(266428, '<f4')
    __BLNK___tbby = _state.view(283564, '<f4')
    aabbcc_ibnd = _state.view(245956, '<i4')
    aabbcc_a = _state.view(246000, '<f4')
    aabbcc_cps = _state.view(246044, '<f4')
    aer_xx1 = _state.view(231840, '<f4')
    aer_xx2 = _state.view(231844, '<f4')
    aer_xx3 = _state.view(231848, '<f4')
    aer_xx4 = _state.view(231852, '<f4')
    aer_xx5 = _state.view(231856, '<f4')
    aer_yy1 = _state.view(231860, '<f4')
    aer_yy2 = _state.view(231864, '<f4')
    aer_yy3 = _state.view(231868, '<f4')
    aer_yy4 = _state.view(231872, '<f4')
    aer_yy5 = _state.view(231876, '<f4')
    aer_zz1 = _state.view(231880, '<f4')
    aer_zz2 = _state.view(231884, '<f4')
    aer_zz3 = _state.view(231888, '<f4')
    aer_zz4 = _state.view(231892, '<f4')
    aer_zz5 = _state.view(231896, '<f4')
    card1_iemsct = _state.view(209576, '<i4')
    card1_noprnt = _state.view(209596, '<i4')
    card1_tbound = _state.view(209600, '<f4')
    card1_salb = _state.view(209604, '<f4')
    card2_icld = _state.view(231760, '<i4')
    card3_h1 = _state.view(246128, '<f4')
    card3_h2 = _state.view(246132, '<f4')
    card3_angle = _state.view(246136, '<f4')
    card4_v1 = _state.view(286864, '<f4')
    card4_v2 = _state.view(286868, '<f4')
    card4_dv = _state.view(286872, '<f4')
    cnstns_pi = _state.view(246160, '<f4')
    cnstns_ca = _state.view(246164, '<f4')
    cnstns_bignum = _state.view(246176, '<f4')
    cnstns_bigexp = _state.view(246180, '<f4')
    cntrl_kmax = _state.view(245600, '<i4')
    cntrl_ikmax = _state.view(245608, '<i4')
    cntrl_ml = _state.view(245616, '<i4')
    cntrl_iklo = _state.view(245620, '<i4')
    cntrl_imult = _state.view(245628, '<i4')
    h2o_cph2o = _state.view(132640, '<f4')
    icll_icall = _state.view(231696, '<i4')
    mnlt_tbbms = _state.view(214416, '<f4')
    mnlt_wpms = _state.view(214552, '<f4')
    mnlt_imsmx = _state.view(223120, '<i4')
    mnlt_wpmss = _state.view(223124, '<f4')
    model_zm = _state.view(231904, '<f4')
    model_tm = _state.view(232176, '<f4')
    msrd_tle = _state.view(209760, '<f4')
    msrd_cosbar = _state.view(209896, '<f4')
    msrd_omega0 = _state.view(210032, '<f4')
    msrd_dtx7 = _state.view(213088, '<f4')
    msrd_daers = _state.view(213224, '<f4')
    msrd_asyik = _state.view(213360, '<f4')
    msrd_asydm = _state.view(213496, '<f4')
    msrd_dmols = _state.view(213772, '<f4')
    msrd_dstrn = _state.view(213908, '<f4')
    msrd_fdnsrt = _state.view(214052, '<f4')
    msrd_fdntrt = _state.view(214064, '<f4')
    o3_cpo3 = _state.view(146720, '<f4')
    path_qtheta = _state.view(242416, '<f4')
    path_aht = _state.view(242700, '<f4')
    sols_wpaths = _state.view(190016, '<f4')
    sols_angsun = _state.view(208256, '<f4')
    srad_teb1 = _state.view(242976, '<f4')
    srad_teb2sv = _state.view(243000, '<f4')
    traceg_cpnh3 = _state.view(117280, '<f4')
    traceg_cpno = _state.view(119004, '<f4')
    traceg_cpno2 = _state.view(119252, '<f4')
    traceg_cpso2 = _state.view(119820, '<f4')
    tran_abb = _state.view(188320, '<f4')
    tran_tmd = _state.view(188732, '<f4')
    tran_dcont = _state.view(189276, '<f4')
    ufmix1_cpco2 = _state.view(120736, '<f4')
    ufmix2_cpco = _state.view(125632, '<f4')
    ufmix2_cpch4 = _state.view(126324, '<f4')
    ufmix2_cpn2o = _state.view(128296, '<f4')
    ufmix2_cpo2 = _state.view(131112, '<f4')
    factor = _ZERO32
    alam = _ZERO32
    t1 = _ZERO32
    hno3 = _zeros(50, '<f4')
    ab = _ZERO32
    abbuv = _ZERO32
    abt = _ZERO32
    alpha2 = _ZERO32
    altx9 = _ZERO32
    asy = _ZERO32
    asymr = _zeros(1, '<f4')
    bbg = _ZERO32
    bbik = _ZERO32
    bet = _zeros(68, '<f4')
    c0 = _zeros(1, '<f4')
    cozen = _zeros(1, '<f4')
    cp = _zeros(1, '<f4')
    cssa = _zeros(1, '<f4')
    ct1 = _zeros(1, '<f4')
    ct2 = _zeros(1, '<f4')
    denom = _ZERO32
    dist = _zeros(1, '<i4')
    dmf = _zeros(34, '<f4')
    dmfs = _zeros(34, '<f4')
    dtau = _ZERO32
    emiss = _ZERO32
    ext = _ZERO32
    fdg = _zeros(1, '<f4')
    fh2o = _zeros(1, '<f4')
    ib = 0
    icount = 0
    idv = 0
    iemiss = 0
    ient = _zeros(1, '<i4')
    iiii = 0
    ik = _zeros(1, '<i4')
    ik1 = _zeros(1, '<i4')
    ikm = 0
    ikmax1 = 0
    ikmaxp = 0
    ikmx = 0
    ikp1 = 0
    imap = _zeros(68, '<i4')
    imlt = 0
    imol = 0
    indch4 = _zeros(1, '<i4')
    indco = _zeros(1, '<i4')
    indco2 = _zeros(1, '<i4')
    indh2o = _zeros(1, '<i4')
    indn2o = _zeros(1, '<i4')
    indnh3 = _zeros(1, '<i4')
    indno = _zeros(1, '<i4')
    indno2 = _zeros(1, '<i4')
    indo2 = _zeros(1, '<i4')
    indo3 = _zeros(1, '<i4')
    indso2 = _zeros(1, '<i4')
    init = 0
    ioff = 0
    ipath = _zeros(1, '<i4')
    ipython = 0
    ubound_0 = 0
    stride_1 = 0
    offset_2 = 0
    size_3 = 0
    iscttr = 0
    itzero = _zeros(1, '<i4')
    iv = _zeros(1, '<i4')
    iv1 = 0
    iv2 = 0
    jk = 0
    k = 0
    ml1 = 0
    n = 0
    n1 = 0
    phase = _zeros(1, '<i4')
    radfn0 = _ZERO32
    radfn1 = _ZERO32
    radmax = _ZERO32
    radmin = _ZERO32
    radsum = _ZERO32
    rain63 = _ZERO32
    rainav = _zeros(1, '<f4')
    rfd = _zeros(1, '<f4')
    rflfac = _ZERO32
    rfls = _ZERO32
    rflsol = _ZERO32
    rflss = _ZERO32
    rflsss = _ZERO32
    rnexph = _ZERO32
    sct = _ZERO32
    sh2ot0 = _zeros(1, '<f4')
    sh2ot1 = _zeros(1, '<f4')
    sigo20 = _zeros(1, '<f4')
    sigo2a = _zeros(1, '<f4')
    sigo2b = _zeros(1, '<f4')
    sms = _ZERO32
    smss = _ZERO32
    solil = _zeros(1, '<f4')
    soliv = _ZERO32
    ss = _zeros(1, '<f4')
    ssol = _ZERO32
    stsol = _ZERO32
    sum = _ZERO32
    suma = _ZERO32
    summs = _ZERO32
    sums = _ZERO32
    sumss = _ZERO32
    sumssr = _zeros(1, '<f4')
    sumsss = _ZERO32
    sumt = _ZERO32
    sumtt = _ZERO32
    sumv = _ZERO32
    sumvv = _ZERO32
    surdsr = _ZERO32
    surdtr = _ZERO32
    t0 = _ZERO32
    tcrris = _ZERO32
    temp = _ZERO32
    tlnew = _ZERO32
    tlold = _ZERO32
    tmprn = _zeros(1, '<f4')
    total = _ZERO32
    trace = _ZERO32
    train = _ZERO32
    traipl = _ZERO32
    tsolil = _ZERO32
    tsoliv = _ZERO32
    ubound_4 = 0
    stride_5 = 0
    offset_6 = 0
    size_7 = 0
    umf = _zeros(34, '<f4')
    umfs = _zeros(34, '<f4')
    unif = _ZERO32
    v = _zeros(1, '<f4')
    vrmax = _ZERO32
    vrmin = _ZERO32
    vtemp = _ZERO32
    w12d = _ZERO32
    w13d = _ZERO32
    w14d = _ZERO32
    w16d = _ZERO32
    w1o3 = _ZERO32
    w2o3 = _ZERO32
    w7d = _ZERO32
    wcrris = _ZERO32
    wo3 = _ZERO32
    wt2 = _ZERO32
    xd = _ZERO32
    xh2o = _ZERO32
    D_7909 = 0
    D_7910 = 0
    D_7911 = 0
    D_7912 = 0
    D_7913 = 0
    D_7914 = 0
    D_7511 = 0
    D_7514 = 0
    D_7539 = 0
    D_7542 = 0
    D_7576 = _ZERO32
    D_7577 = _ZERO32
    D_7632 = 0
    D_7633 = 0
    D_7636 = 0
    D_7642 = 0
    D_7645 = 0
    D_7648 = 0
    D_7656 = 0
    D_7659 = 0
    D_7666 = 0
    D_7669 = 0
    D_7674 = 0
    D_7679 = _ZERO32
    D_7709 = 0
    D_7720 = 0
    D_7814 = 0
    D_7817 = 0
    D_7841 = _ZERO32
    D_7842 = _ZERO32
    D_7854 = _ZERO32
    D_7855 = _ZERO32
    D_7857 = _ZERO32
    D_7858 = _ZERO32
    D_7865 = _ZERO32
    D_7866 = _ZERO32
    D_7868 = _ZERO32
    D_7869 = _ZERO32
    D_7873 = _ZERO32
    D_7874 = _ZERO32
    D_7882 = 0
    D_7883 = _ZERO32
    D_7884 = 0
    S_8 = 0
    D_7886 = 0
    D_7887 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = nwl[0]
                ubound_4 = _int(_int(_1))
                stride_5 = _int(ubound_4)
                stride_5 = _int(max(stride_5, 0))
                size_7 = _int(stride_5 * 63)
                size_7 = _int(max(size_7, 0))
                D_7912 = _int(size_7 + -1)
                size_100_2 = _int(size_7)
                _3 = _int(size_100_2)
                D_7913 = _int(_3 * 32)
                size_101_4 = _int(size_7)
                D_7914 = _int(size_101_4 * 4)
                offset_6 = _int(~stride_5)
                _5 = nwl[0]
                ubound_0 = _int(_int(_5))
                stride_1 = _int(ubound_0)
                stride_1 = _int(max(stride_1, 0))
                size_3 = _int(stride_1 * 3)
                size_3 = _int(max(size_3, 0))
                D_7909 = _int(size_3 + -1)
                size_102_6 = _int(size_3)
                _7 = _int(size_102_6)
                D_7910 = _int(_7 * 32)
                size_103_8 = _int(size_3)
                D_7911 = _int(size_103_8 * 4)
                offset_2 = _int(~stride_1)
                alpha2 = _f32(4.0e+4)
                _9 = cntrl_imult[0]
                _pc = 1 if _9 == 1 else 2
                continue
            case 1:  # <D.17717>
                _ft_mapms(_state, cntrl_ml, cntrl_ikmax, model_zm, path_aht, imap)
                _pc = 2
                continue
            case 2:  # L.1
                ioff = _int(0)
                _10 = card3_h1[0]
                _11 = card3_h2[0]
                _pc = 3 if _10 >= _11 else 4
                continue
            case 3:  # <D.17720>
                ioff = _int(1)
                _pc = 4
                continue
            case 4:  # L.2
                _12 = card3_angle[0]
                _pc = 5 if _12 > 9.0e+1 else 6
                continue
            case 5:  # <D.17723>
                ioff = _int(1)
                _pc = 6
                continue
            case 6:  # L.3
                _13 = cntrl_imult[0]
                _pc = 7 if _13 == 1 else 15
                continue
            case 7:  # <D.17726>
                D_7511 = _int(cntrl_ml[0])
                ik[0] = 1
                _pc = 8
            case 8:  # <D.17728>
                ik_104_14 = ik[0]
                D_7514 = _int(D_7511 < ik_104_14)
                _pc = 14 if D_7514 != 0 else 9
                continue
            case 9:  # <D.17729>
                _15 = cntrl_ml[0]
                ik_105_16 = ik[0]
                _17 = _15 - ik_105_16
                _18 = _17 + 1
                _19 = _int(_18)
                _20 = _19 + -1
                ik_106_21 = ik[0]
                _22 = _int(ik_106_21)
                _23 = _22 + -1
                _24 = model_tm[_20]
                msrd_tle[_23] = _24
                ik_107_25 = ik[0]
                _26 = mnlt_imsmx[0]
                _pc = 10 if ik_107_25 <= _26 else 11
                continue
            case 10:  # <D.17730>
                ik_108_27 = ik[0]
                _28 = _int(ik_108_27)
                _29 = _28 + -1
                ik_109_30 = ik[0]
                _31 = _int(ik_109_30)
                _32 = _31 + -1
                _33 = mnlt_tbbms[_29]
                tran_tmd[_32] = _33
                _pc = 11
                continue
            case 11:  # L.7
                ik_110_34 = ik[0]
                _35 = mnlt_imsmx[0]
                _pc = 12 if ik_110_34 > _35 else 13
                continue
            case 12:  # <D.17733>
                _36 = mnlt_imsmx[0]
                _37 = _int(_36)
                _38 = _37 + -1
                ik_111_39 = ik[0]
                _40 = _int(ik_111_39)
                _41 = _40 + -1
                _42 = mnlt_tbbms[_38]
                tran_tmd[_41] = _42
                _pc = 13
                continue
            case 13:  # L.5
                ik_112_43 = ik[0]
                _44 = ik_112_43 + 1
                ik[0] = _44
                _pc = 8
                continue
            case 14:  # L.6
                _45 = cntrl_ml[0]
                _46 = _int(_45)
                _47 = _46 + -1
                _48 = cntrl_ml[0]
                _49 = _48 + 1
                _50 = _int(_49)
                _51 = _50 + -1
                _52 = tran_tmd[_47]
                tran_tmd[_51] = _52
                _53 = cntrl_ml[0]
                _54 = _int(_53)
                _55 = _54 + -1
                _56 = cntrl_ml[0]
                _57 = _56 + 1
                _58 = _int(_57)
                _59 = _58 + -1
                _60 = msrd_tle[_55]
                msrd_tle[_59] = _60
                _pc = 15
                continue
            case 15:  # L.4
                radmin = _f32(1.00000001504746621987668885504e+30)
                radmax = _f32(0.0)
                ient[0] = 0
                _61 = card1_salb[0]
                emiss = _f32(1.0e+0 - _61)
                vrmin = _f32(0.0)
                vrmax = _f32(0.0)
                ikmx = _int(cntrl_ikmax[0])
                imlt = _int(cntrl_imult[0])
                suma = _f32(0.0)
                sums = _f32(-9.9e+1)
                sumssr[0] = -9.9e+1
                rfls = _f32(-9.9e+1)
                rflsol = _f32(-9.9e+1)
                radsum = _f32(0.0)
                stsol = _f32(0.0)
                ssol = _f32(0.0)
                factor = _f32(5.0e-1)
                _62 = card4_v1[0]
                _63 = _div(_62, 5.0e+0)
                iv1 = _int(_int(_63))
                _64 = card4_v2[0]
                _65 = _div(_64, 5.0e+0)
                _66 = _65 + 9.900000095367431640625e-1
                iv2 = _int(_int(_66))
                iv1 = _int(iv1 * 5)
                iv2 = _int(iv2 * 5)
                _pc = 16 if iv2 > 50000 else 17
                continue
            case 16:  # <D.17737>
                iv2 = _int(50000)
                _pc = 17
                continue
            case 17:  # L.9
                _67 = card4_dv[0]
                _pc = 18 if _67 < 5.0e+0 else 19
                continue
            case 18:  # <D.17740>
                card4_dv[0] = 5.0e+0
                _pc = 19
                continue
            case 19:  # L.10
                _68 = card4_dv[0]
                idv = _int(_int(_68))
                _69 = iv1 - idv
                iv[0] = _69
                cntrl_iklo[0] = 1
                icount = _int(0)
                icll_icall[0] = 0
                iemiss = _int(0)
                iscttr = _int(0)
                _70 = card1_iemsct[0]
                _71 = _70 == 1
                _72 = card1_iemsct[0]
                _73 = _72 == 2
                _74 = _71 | _73
                _pc = 20 if _74 != 0 else 21
                continue
            case 20:  # <D.17743>
                iemiss = _int(1)
                _pc = 21
                continue
            case 21:  # L.11
                _75 = card1_iemsct[0]
                _pc = 22 if _75 == 2 else 23
                continue
            case 22:  # <D.17746>
                iscttr = _int(1)
                _pc = 23
                continue
            case 23:  # L.12
                _76 = cntrl_ikmax[0]
                _77 = _int(_76)
                _78 = _77 + 1019
                _79 = __BLNK___wpath[_78]
                wcrris = _f32(_79 * 2.0e+0)
                tcrris = _f32(1.0e+0)
                _80 = card2_icld[0]
                _pc = 24 if _80 == 20 else 28
                continue
            case 24:  # <D.17749>
                _81 = cnstns_bigexp[0]
                _pc = 25 if wcrris <= _81 else 26
                continue
            case 25:  # <D.17751>
                _82 = -wcrris
                tcrris = _f32(__builtin_expf(_82))
                _pc = 27
                continue
            case 26:  # <D.17752>
                tcrris = _f32(0.0)
                _pc = 27
            case 27:  # L.14
                _pc = 28
                continue
            case 28:  # L.13
                train = _f32(1.0e+0)
                _pc = 29 if iemiss == 0 else 30
                continue
            case 29:  # <D.17755>
                _83 = cntrl_iklo[0]
                cntrl_ikmax[0] = _83
                _pc = 30
                continue
            case 30:  # __label_000933
                _84 = card1_noprnt[0]
                _pc = 31 if _84 == -1 else 34
                continue
            case 31:  # <D.17758>
                _85 = cntrl_imult[0]
                _pc = 32 if _85 == 1 else 33
                continue
            case 32:  # __label_001200
                _pc = 33
                continue
            case 33:  # L.17
                _pc = 34
                continue
            case 34:  # L.16
                indh2o[0] = 1
                indo3[0] = 1
                indco2[0] = 1
                indco[0] = 1
                indch4[0] = 1
                indn2o[0] = 1
                indo2[0] = 1
                indnh3[0] = 1
                indno[0] = 1
                indno2[0] = 1
                indso2[0] = 1
                ipython = _int(1)
                _pc = 35
            case 35:  # __label_000005
                iv_113_86 = iv[0]
                _87 = idv + iv_113_86
                iv[0] = _87
                _88 = cntrl_ml[0]
                ml1 = _int(_88 + -1)
                init = _int(0)
                cntrl_iklo[0] = 1
                _89 = cntrl_imult[0]
                _pc = 36 if _89 == 1 else 37
                continue
            case 36:  # <D.17764>
                _90 = mnlt_imsmx[0]
                cntrl_ikmax[0] = _90
                _pc = 38
                continue
            case 37:  # <D.17765>
                cntrl_ikmax[0] = ikmx
                _pc = 38
            case 38:  # L.18
                _pc = 39 if iemiss == 0 else 40
                continue
            case 39:  # <D.17767>
                _91 = cntrl_iklo[0]
                cntrl_ikmax[0] = _91
                _pc = 40
                continue
            case 40:  # L.19
                itzero[0] = 0
                ipath[0] = 1
                sumv = _f32(0.0)
                tlold = _f32(1.0e+0)
                _pc = 41 if icount == 0 else 42
                continue
            case 41:  # <D.17770>
                _pc = 45
                continue
            case 42:  # L.20
                _pc = 43 if icount == 50 else 44
                continue
            case 43:  # <D.17772>
                _pc = 45
                continue
            case 44:  # L.21
                _pc = 46
                continue
            case 45:  # __label_000015
                icount = _int(0)
                _pc = 46
            case 46:  # __label_000020
                D_7539 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 47
            case 47:  # <D.17774>
                D_7542 = _int(k > D_7539)
                _pc = 51 if D_7542 != 0 else 48
                continue
            case 48:  # <D.17775>
                _92 = _int(k)
                _93 = _92 + -1
                __BLNK___tx[_93] = 0.0
                _pc = 49 if k <= 3 else 50
                continue
            case 49:  # <D.17776>
                _94 = _int(k)
                _95 = _94 + -1
                __BLNK___tx[_95] = 1.0e+0
                _pc = 50
                continue
            case 50:  # L.22
                k = _int(k + 1)
                _pc = 47
                continue
            case 51:  # L.23
                icount = _int(icount + 1)
                iv_114_96 = iv[0]
                _97 = _f32(iv_114_96)
                v[0] = _97
                _ft_cxdta(_state, cp, v, wnlohi_iwlh2o, wnlohi_iwhh2o, h2o_cph2o, indh2o)
                cp_115_98 = cp[0]
                aabbcc_cps[0] = cp_115_98
                _ft_cxdta(_state, cp, v, wnlohi_iwlco2, wnlohi_iwhco2, ufmix1_cpco2, indco2)
                cp_116_99 = cp[0]
                aabbcc_cps[1] = cp_116_99
                _ft_cxdta(_state, cp, v, wnlohi_iwlo3, wnlohi_iwho3, o3_cpo3, indo3)
                cp_117_100 = cp[0]
                aabbcc_cps[2] = cp_117_100
                _ft_cxdta(_state, cp, v, wnlohi_iwln2o, wnlohi_iwhn2o, ufmix2_cpn2o, indn2o)
                cp_118_101 = cp[0]
                aabbcc_cps[3] = cp_118_101
                _ft_cxdta(_state, cp, v, wnlohi_iwlco, wnlohi_iwhco, ufmix2_cpco, indco)
                cp_119_102 = cp[0]
                aabbcc_cps[4] = cp_119_102
                _ft_cxdta(_state, cp, v, wnlohi_iwlch4, wnlohi_iwhch4, ufmix2_cpch4, indch4)
                cp_120_103 = cp[0]
                aabbcc_cps[5] = cp_120_103
                _ft_cxdta(_state, cp, v, wnlohi_iwlo2, wnlohi_iwho2, ufmix2_cpo2, indo2)
                cp_121_104 = cp[0]
                aabbcc_cps[6] = cp_121_104
                _ft_cxdta(_state, cp, v, wnlohi_iwlno, wnlohi_iwhno, traceg_cpno, indno)
                cp_122_105 = cp[0]
                aabbcc_cps[7] = cp_122_105
                _ft_cxdta(_state, cp, v, wnlohi_iwlso2, wnlohi_iwhso2, traceg_cpso2, indso2)
                cp_123_106 = cp[0]
                aabbcc_cps[8] = cp_123_106
                _ft_cxdta(_state, cp, v, wnlohi_iwlno2, wnlohi_iwhno2, traceg_cpno2, indno2)
                cp_124_107 = cp[0]
                aabbcc_cps[9] = cp_124_107
                _ft_cxdta(_state, cp, v, wnlohi_iwlnh3, wnlohi_iwhnh3, traceg_cpnh3, indnh3)
                cp_125_108 = cp[0]
                aabbcc_cps[10] = cp_125_108
                _ft_c4dta(_state, tran_abb[3:], v)
                _ft_abcdta(_state, iv)
                _ft_slf296(_state, v, sh2ot0)
                _ft_slf260(_state, v, sh2ot1)
                _ft_frn296(_state, v, fh2o)
                t0 = _f32(2.96e+2)
                t1 = _f32(2.6e+2)
                sh2ot0_126_109 = sh2ot0[0]
                _pc = 52 if sh2ot0_126_109 > 0.0 else 53
                continue
            case 52:  # <D.17779>
                v_127_110 = v[0]
                _111 = v_127_110 - 1.05e+3
                D_7576 = _f32(_111)
                D_7577 = _f32(D_7576 * D_7576)
                _112 = D_7577 + alpha2
                _113 = _112
                _114 = _div(alpha2, _113)
                _115 = _114
                _116 = _115 * 2.333000004291534423828125e-1
                _117 = 1.0e+0 - _116
                xh2o = _f32(_117)
                sh2ot0_128_118 = sh2ot0[0]
                _119 = xh2o * sh2ot0_128_118
                sh2ot0[0] = _119
                sh2ot1_129_120 = sh2ot1[0]
                _121 = xh2o * sh2ot1_129_120
                sh2ot1[0] = _121
                _pc = 53
                continue
            case 53:  # L.25
                v_130_122 = v[0]
                vtemp = _f32(_div(v_130_122, 6.95200026035308837890625e-1))
                _123 = _div(vtemp, t1)
                _124 = cnstns_bigexp[0]
                _pc = 54 if _123 <= _124 else 55
                continue
            case 54:  # <D.17782>
                v_131_125 = v[0]
                _126 = t0 * 6.95200026035308837890625e-1
                _127 = _126
                _128 = _div(v_131_125, _127)
                _129 = -_128
                xd = _f32(__builtin_expf(_129))
                _130 = 1.0e+0 - xd
                _131 = _130
                v_132_132 = v[0]
                _133 = _131 * v_132_132
                _134 = xd + 1.0e+0
                _135 = _134
                radfn0 = _f32(_div(_133, _135))
                v_133_136 = v[0]
                _137 = t1 * 6.95200026035308837890625e-1
                _138 = _137
                _139 = _div(v_133_136, _138)
                _140 = -_139
                xd = _f32(__builtin_expf(_140))
                _141 = 1.0e+0 - xd
                _142 = _141
                v_134_143 = v[0]
                _144 = _142 * v_134_143
                _145 = xd + 1.0e+0
                _146 = _145
                radfn1 = _f32(_div(_144, _146))
                _pc = 56
                continue
            case 55:  # <D.17783>
                radfn0 = _f32(v[0])
                radfn1 = _f32(v[0])
                _pc = 56
            case 56:  # L.26
                _ft_fudge(_state, v, fdg)
                sh2ot0_135_147 = sh2ot0[0]
                _148 = radfn0 * sh2ot0_135_147
                tran_abb[4] = _148
                _ft_c6dta(_state, tran_abb[5:], v)
                tran_abb[6] = 0.0
                _ft_c8dta(_state, tran_abb[7:], v)
                sh2ot1_136_149 = sh2ot1[0]
                _150 = radfn1 * sh2ot1_136_149
                _151 = _150
                sh2ot0_137_152 = sh2ot0[0]
                _153 = radfn0 * sh2ot0_137_152
                _154 = _153
                _155 = _151 - _154
                tran_abb[8] = _155
                fh2o_138_156 = fh2o[0]
                fdg_139_157 = fdg[0]
                _158 = fh2o_138_156 + fdg_139_157
                _159 = _158
                _160 = radfn0 * _159
                tran_abb[9] = _160
                _ft_hno3(_state, v, tran_abb[10:])
                _ft_aerext(_state, v)
                _ft_hertda(_state, tran_abb[16:], v)
                _ft_o2cont(_state, v, sigo20, sigo2a, sigo2b)
                v_140_161 = v[0]
                _pc = 57 if v_140_161 > 4.96e+4 else 58
                continue
            case 57:  # <D.17785>
                _ft_schrun(_state, v, aabbcc_cps[6:])
                _pc = 58
                continue
            case 58:  # L.27
                abbuv = _f32(0.0)
                v_141_162 = v[0]
                _163 = v_141_162 > 2.437e+4
                v_142_164 = v[0]
                _165 = v_142_164 < 4.08e+4
                _166 = _163 & _165
                _pc = 59 if _166 != 0 else 60
                continue
            case 59:  # <D.17788>
                tran_abb[7] = 0.0
                _ft_o3hht0(_state, v, c0)
                _ft_o3hht1(_state, v, ct1)
                _ft_o3hht2(_state, v, ct2)
                _pc = 60
                continue
            case 60:  # L.28
                v_143_167 = v[0]
                _pc = 61 if v_143_167 >= 4.08e+4 else 62
                continue
            case 61:  # <D.17791>
                _ft_o3uv(_state, v, c0)
                tran_abb[7] = 0.0
                _pc = 62
                continue
            case 62:  # __label_000109
                srad_teb1[0] = -9.9e+1
                ipath[0] = 1
                srad_teb2sv[0] = -9.9e+1
                total = _f32(1.0e+0)
                msrd_dstrn[0] = 1.0e+0
                sum = _f32(0.0)
                summs = _f32(0.0)
                D_7632 = _int(cntrl_iklo[0])
                D_7633 = _int(cntrl_ikmax[0])
                ik[0] = D_7632
                _pc = 63
            case 63:  # <D.17794>
                ik_144_168 = ik[0]
                D_7636 = _int(D_7633 < ik_144_168)
                _pc = 244 if D_7636 != 0 else 64
                continue
            case 64:  # <D.17795>
                _pc = 65 if iemiss == 0 else 66
                continue
            case 65:  # <D.17796>
                _pc = 104
                continue
            case 66:  # L.32
                _pc = 67 if iscttr == 0 else 68
                continue
            case 67:  # <D.17798>
                _pc = 98
                continue
            case 68:  # __label_000111
                ipath_145_169 = ipath[0]
                D_7642 = _int(ipath_145_169 + -2)
                _pc = 69 if D_7642 <= 0 else 98
                continue
            case 69:  # <D.17800>
                _pc = 70 if D_7642 < 0 else 83
                continue
            case 70:  # __label_000112
                D_7645 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 71
            case 71:  # <D.17801>
                D_7648 = _int(k > D_7645)
                _pc = 76 if D_7648 != 0 else 72
                continue
            case 72:  # <D.17802>
                _170 = cntrl_imult[0]
                _171 = _170 == 1
                _172 = init == 0
                _173 = _171 & _172
                _pc = 73 if _173 != 0 else 74
                continue
            case 73:  # <D.17803>
                _174 = _int(k)
                _175 = _174 + -1
                _176 = _175 * 34
                _177 = _int(k)
                _178 = _177 + -1
                _179 = mnlt_wpmss[_176]
                __BLNK___w[_178] = _179
                _pc = 75
                continue
            case 74:  # <D.17804>
                _180 = _int(k)
                _181 = _180 + -1
                _182 = _181 * 68
                _183 = _int(k)
                _184 = _183 + -1
                _185 = sols_wpaths[_182]
                __BLNK___w[_184] = _185
                _pc = 75
            case 75:  # L.34
                k = _int(k + 1)
                _pc = 71
                continue
            case 76:  # L.35
                _186 = __BLNK___w[35]
                _pc = 77 if _186 >= 0.0 else 78
                continue
            case 77:  # <D.17806>
                _pc = 104
                continue
            case 78:  # L.37
                __BLNK___tx[5] = 0.0
                __BLNK___tx[6] = 0.0
                __BLNK___tx[8] = 0.0
                __BLNK___tx[9] = 0.0
                _187 = cntrl_imult[0]
                _188 = _187 == 1
                _189 = init == 0
                _190 = _188 & _189
                _pc = 79 if _190 != 0 else 82
                continue
            case 79:  # <D.17808>
                ik_146_191 = ik[0]
                _pc = 80 if ik_146_191 > 1 else 81
                continue
            case 80:  # <D.17810>
                ik_147_192 = ik[0]
                _193 = ik_147_192 + -1
                _194 = _int(_193)
                _195 = _194 + -1
                msrd_asyik[_195] = 0.0
                ik_148_196 = ik[0]
                _197 = ik_148_196 + -1
                _198 = _int(_197)
                _199 = _198 + -1
                msrd_asydm[_199] = 1.0e+0
                _pc = 81
                continue
            case 81:  # L.39
                _200 = cntrl_ikmax[0]
                _201 = _int(_200)
                _202 = _201 + -1
                _203 = msrd_asyik[0]
                msrd_asyik[_202] = _203
                _204 = cntrl_ikmax[0]
                _205 = _int(_204)
                _206 = _205 + -1
                _207 = msrd_asydm[0]
                msrd_asydm[_206] = _207
                ik_149_208 = ik[0]
                _209 = _int(ik_149_208)
                _210 = _209 + -1
                tran_dcont[_210] = 0.0
                ik_150_211 = ik[0]
                _212 = _int(ik_150_211)
                _213 = _212 + -1
                msrd_dtx7[_213] = 0.0
                ik_151_214 = ik[0]
                _215 = _int(ik_151_214)
                _216 = _215 + -1
                msrd_daers[_216] = 0.0
                ik_152_217 = ik[0]
                _218 = _int(ik_152_217)
                _219 = _218 + -1
                msrd_dmols[_219] = 0.0
                _pc = 194
                continue
            case 82:  # L.38
                _pc = 206
                continue
            case 83:  # __label_000114
                ik_153_220 = ik[0]
                ikp1 = _int(ik_153_220 + 1)
                D_7656 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 84
            case 84:  # <D.17813>
                D_7659 = _int(k > D_7656)
                _pc = 89 if D_7659 != 0 else 85
                continue
            case 85:  # <D.17814>
                _221 = cntrl_imult[0]
                _222 = _221 == 1
                _223 = init == 0
                _224 = _222 & _223
                _pc = 86 if _224 != 0 else 87
                continue
            case 86:  # <D.17815>
                _225 = _int(k)
                _226 = _225 * 34
                _227 = _int(ikp1)
                _228 = _226 + _227
                _229 = _228 + -35
                _230 = _int(k)
                _231 = _230 + -1
                _232 = mnlt_wpmss[_229]
                __BLNK___w[_231] = _232
                _pc = 88
                continue
            case 87:  # <D.17816>
                _233 = _int(k)
                _234 = _233 * 68
                ik_154_235 = ik[0]
                _236 = _int(ik_154_235)
                _237 = _234 + _236
                _238 = _237 + -69
                _239 = __BLNK___wpath[_238]
                _240 = _int(k)
                _241 = _240 * 68
                _242 = _int(ikp1)
                _243 = _241 + _242
                _244 = _243 + -69
                _245 = sols_wpaths[_244]
                _246 = _int(k)
                _247 = _246 + -1
                _248 = _239 + _245
                __BLNK___w[_247] = _248
                _pc = 88
            case 88:  # L.40
                k = _int(k + 1)
                _pc = 84
                continue
            case 89:  # L.41
                _249 = cntrl_imult[0]
                _250 = _249 == 1
                _251 = init == 0
                _252 = _250 & _251
                _pc = 90 if _252 != 0 else 95
                continue
            case 90:  # <D.17818>
                _253 = _int(ikp1)
                _254 = _253 + 1189
                _255 = mnlt_wpmss[_254]
                _pc = 91 if _255 > 0.0 else 92
                continue
            case 91:  # <D.17820>
                _pc = 104
                continue
            case 92:  # L.44
                __BLNK___tx[5] = 0.0
                __BLNK___tx[6] = 0.0
                __BLNK___tx[8] = 0.0
                __BLNK___tx[9] = 0.0
                ik_155_256 = ik[0]
                _pc = 93 if ik_155_256 > 1 else 94
                continue
            case 93:  # <D.17822>
                ik_156_257 = ik[0]
                _258 = ik_156_257 + -1
                _259 = _int(_258)
                _260 = _259 + -1
                msrd_asyik[_260] = 0.0
                ik_157_261 = ik[0]
                _262 = ik_157_261 + -1
                _263 = _int(_262)
                _264 = _263 + -1
                msrd_asydm[_264] = 1.0e+0
                _pc = 94
                continue
            case 94:  # L.45
                _265 = cntrl_ikmax[0]
                _266 = _int(_265)
                _267 = _266 + -1
                _268 = msrd_asyik[0]
                msrd_asyik[_267] = _268
                _269 = cntrl_ikmax[0]
                _270 = _int(_269)
                _271 = _270 + -1
                _272 = msrd_asydm[0]
                msrd_asydm[_271] = _272
                ik_158_273 = ik[0]
                _274 = _int(ik_158_273)
                _275 = _274 + -1
                tran_dcont[_275] = 0.0
                ik_159_276 = ik[0]
                _277 = _int(ik_159_276)
                _278 = _277 + -1
                msrd_dtx7[_278] = 0.0
                ik_160_279 = ik[0]
                _280 = _int(ik_160_279)
                _281 = _280 + -1
                msrd_daers[_281] = 0.0
                ik_161_282 = ik[0]
                _283 = _int(ik_161_282)
                _284 = _283 + -1
                msrd_dmols[_284] = 0.0
                _pc = 194
                continue
            case 95:  # L.43
                _285 = _int(ikp1)
                _286 = _285 + 2379
                _287 = sols_wpaths[_286]
                _pc = 96 if _287 >= 0.0 else 97
                continue
            case 96:  # <D.17825>
                _pc = 104
                continue
            case 97:  # L.46
                __BLNK___tx[5] = 0.0
                __BLNK___tx[6] = 0.0
                __BLNK___tx[8] = 0.0
                __BLNK___tx[9] = 0.0
                _pc = 206
                continue
            case 98:  # __label_000116
                D_7666 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 99
            case 99:  # <D.17827>
                D_7669 = _int(k > D_7666)
                _pc = 104 if D_7669 != 0 else 100
                continue
            case 100:  # <D.17828>
                _288 = cntrl_imult[0]
                _289 = _288 == 1
                _290 = init == 0
                _291 = _289 & _290
                _pc = 101 if _291 != 0 else 102
                continue
            case 101:  # <D.17829>
                _292 = _int(k)
                _293 = _292 * 34
                ik_162_294 = ik[0]
                _295 = _int(ik_162_294)
                _296 = _293 + _295
                _297 = _296 + -35
                _298 = _int(k)
                _299 = _298 + -1
                _300 = mnlt_wpms[_297]
                __BLNK___w[_299] = _300
                _pc = 103
                continue
            case 102:  # <D.17830>
                _301 = _int(k)
                _302 = _301 * 68
                ik_163_303 = ik[0]
                _304 = _int(ik_163_303)
                _305 = _302 + _304
                _306 = _305 + -69
                _307 = _int(k)
                _308 = _307 + -1
                _309 = __BLNK___wpath[_306]
                __BLNK___w[_308] = _309
                _pc = 103
            case 103:  # L.47
                k = _int(k + 1)
                _pc = 99
                continue
            case 104:  # __label_000120
                k = _int(3)
                _pc = 105
            case 105:  # <D.17832>
                D_7674 = _int(k > 16)
                _pc = 108 if D_7674 != 0 else 106
                continue
            case 106:  # __label_000121
                _310 = _int(k)
                _311 = _310 + -1
                __BLNK___tx[_311] = 0.0
                _pc = 107
            case 107:  # L.50
                k = _int(k + 1)
                _pc = 105
                continue
            case 108:  # L.51
                _312 = __BLNK___w[6]
                _313 = aer_xx1[0]
                _314 = _312 * _313
                _315 = __BLNK___w[11]
                _316 = aer_xx2[0]
                _317 = _315 * _316
                _318 = _314 + _317
                _319 = __BLNK___w[12]
                _320 = aer_xx3[0]
                _321 = _319 * _320
                _322 = _318 + _321
                _323 = __BLNK___w[13]
                _324 = aer_xx4[0]
                _325 = _323 * _324
                _326 = _322 + _325
                _327 = __BLNK___w[15]
                _328 = aer_xx5[0]
                _329 = _327 * _328
                ext = _f32(_326 + _329)
                _330 = __BLNK___w[6]
                _331 = aer_yy1[0]
                _332 = _330 * _331
                _333 = __BLNK___w[11]
                _334 = aer_yy2[0]
                _335 = _333 * _334
                _336 = _332 + _335
                _337 = __BLNK___w[12]
                _338 = aer_yy3[0]
                _339 = _337 * _338
                _340 = _336 + _339
                _341 = __BLNK___w[13]
                _342 = aer_yy4[0]
                _343 = _341 * _342
                _344 = _340 + _343
                _345 = __BLNK___w[15]
                _346 = aer_yy5[0]
                _347 = _345 * _346
                abt = _f32(_344 + _347)
                _348 = cntrl_imult[0]
                _349 = _348 == 1
                _350 = init == 0
                _351 = _349 & _350
                _pc = 109 if _351 != 0 else 113
                continue
            case 109:  # <D.17834>
                ik_164_352 = ik[0]
                _pc = 110 if ik_164_352 == 1 else 111
                continue
            case 110:  # <D.17836>
                ik_165_353 = ik[0]
                _354 = _int(ik_165_353)
                _355 = _354 + 203
                w7d = _f32(mnlt_wpms[_355])
                ik_166_356 = ik[0]
                _357 = _int(ik_166_356)
                _358 = _357 + 373
                w12d = _f32(mnlt_wpms[_358])
                ik_167_359 = ik[0]
                _360 = _int(ik_167_359)
                _361 = _360 + 407
                w13d = _f32(mnlt_wpms[_361])
                ik_168_362 = ik[0]
                _363 = _int(ik_168_362)
                _364 = _363 + 441
                w14d = _f32(mnlt_wpms[_364])
                ik_169_365 = ik[0]
                _366 = _int(ik_169_365)
                _367 = _366 + 509
                w16d = _f32(mnlt_wpms[_367])
                _pc = 112
                continue
            case 111:  # <D.17837>
                ik_170_368 = ik[0]
                ikm = _int(ik_170_368 + -1)
                ik_171_369 = ik[0]
                _370 = _int(ik_171_369)
                _371 = _370 + 203
                _372 = mnlt_wpms[_371]
                _373 = _int(ikm)
                _374 = _373 + 203
                _375 = mnlt_wpms[_374]
                w7d = _f32(_372 - _375)
                ik_172_376 = ik[0]
                _377 = _int(ik_172_376)
                _378 = _377 + 373
                _379 = mnlt_wpms[_378]
                _380 = _int(ikm)
                _381 = _380 + 373
                _382 = mnlt_wpms[_381]
                w12d = _f32(_379 - _382)
                ik_173_383 = ik[0]
                _384 = _int(ik_173_383)
                _385 = _384 + 407
                _386 = mnlt_wpms[_385]
                _387 = _int(ikm)
                _388 = _387 + 407
                _389 = mnlt_wpms[_388]
                w13d = _f32(_386 - _389)
                ik_174_390 = ik[0]
                _391 = _int(ik_174_390)
                _392 = _391 + 441
                _393 = mnlt_wpms[_392]
                _394 = _int(ikm)
                _395 = _394 + 441
                _396 = mnlt_wpms[_395]
                w14d = _f32(_393 - _396)
                ik_175_397 = ik[0]
                _398 = _int(ik_175_397)
                _399 = _398 + 509
                _400 = mnlt_wpms[_399]
                _401 = _int(ikm)
                _402 = _401 + 509
                _403 = mnlt_wpms[_402]
                w16d = _f32(_400 - _403)
                _pc = 112
            case 112:  # L.53
                _404 = aer_xx1[0]
                _405 = aer_yy1[0]
                _406 = _404 - _405
                _407 = _406
                _408 = aer_zz1[0]
                _409 = _407 * _408
                _410 = w7d * _409
                _411 = aer_xx2[0]
                _412 = aer_yy2[0]
                _413 = _411 - _412
                _414 = _413
                _415 = aer_zz2[0]
                _416 = _414 * _415
                _417 = w12d * _416
                _418 = _410 + _417
                _419 = aer_xx3[0]
                _420 = aer_yy3[0]
                _421 = _419 - _420
                _422 = _421
                _423 = aer_zz3[0]
                _424 = _422 * _423
                _425 = w13d * _424
                _426 = _418 + _425
                _427 = aer_xx4[0]
                _428 = aer_yy4[0]
                _429 = _427 - _428
                _430 = _429
                _431 = aer_zz4[0]
                _432 = _430 * _431
                _433 = w14d * _432
                _434 = _426 + _433
                _435 = aer_xx5[0]
                _436 = aer_yy5[0]
                _437 = _435 - _436
                _438 = _437
                _439 = aer_zz5[0]
                _440 = _438 * _439
                _441 = w16d * _440
                _442 = _434 + _441
                asy = _f32(_442)
                _pc = 113
                continue
            case 113:  # L.52
                sct = _f32(ext - abt)
                train = _f32(1.0e+0)
                _443 = __BLNK___w[2]
                _pc = 114 if _443 != 0.0 else 124
                continue
            case 114:  # <D.17840>
                _444 = __BLNK___w[60]
                _445 = __BLNK___w[2]
                _446 = _div(_444, _445)
                tmprn[0] = _446
                v_176_447 = v[0]
                tmprn_177_448 = tmprn[0]
                _449 = tmprn_177_448 * 6.95200026035308837890625e-1
                _450 = _449
                _451 = _div(v_176_447, _450)
                _452 = -_451
                xd = _f32(__builtin_expf(_452))
                _453 = 1.0e+0 - xd
                _454 = _453
                v_178_455 = v[0]
                _456 = _454 * v_178_455
                _457 = xd + 1.0e+0
                _458 = _457
                _459 = _div(_456, _458)
                rfd[0] = _459
                _460 = __BLNK___w[2]
                _461 = __BLNK___w[61]
                rain63 = _f32(_div(_460, _461))
                D_7679 = _f32(rain63)
                _462 = __builtin_powf(D_7679, 1.58730161190032958984375e+0)
                rainav[0] = _462
                train = _f32(_ft_tnrain(_state, rainav, v, tmprn, rfd))
                v_179_463 = v[0]
                _pc = 115 if v_179_463 < 2.5e+2 else 120
                continue
            case 115:  # <D.17842>
                _464 = card2_icld[0]
                _pc = 116 if _464 <= 11 else 117
                continue
            case 116:  # <D.17844>
                phase[0] = 1
                _pc = 117
                continue
            case 117:  # L.56
                _465 = card2_icld[0]
                _pc = 118 if _465 > 11 else 119
                continue
            case 118:  # <D.17847>
                phase[0] = 2
                _pc = 119
                continue
            case 119:  # L.57
                dist[0] = 1
                _ft_rnscat(_state, v, rainav, tmprn, phase, dist, ik1, cssa, asymr, ient)
                ient_180_466 = ient[0]
                _467 = ient_180_466 + 1
                ient[0] = _467
                _pc = 121
                continue
            case 120:  # <D.17843>
                cssa[0] = 5.0e-1
                asymr[0] = 8.5000002384185791015625e-1
                _pc = 121
            case 121:  # L.55
                _468 = __BLNK___w[61]
                rnexph = _f32(train * _468)
                cssa_181_469 = cssa[0]
                _470 = rnexph * cssa_181_469
                abt = _f32(abt + _470)
                cssa_182_471 = cssa[0]
                _472 = 1.0e+0 - cssa_182_471
                _473 = _472
                _474 = rnexph * _473
                sct = _f32(sct + _474)
                _475 = cntrl_imult[0]
                _476 = _475 == 1
                _477 = init == 0
                _478 = _476 & _477
                _pc = 122 if _478 != 0 else 123
                continue
            case 122:  # <D.17851>
                traipl = _f32(rnexph)
                cssa_183_479 = cssa[0]
                _480 = 1.0e+0 - cssa_183_479
                _481 = _480
                asymr_184_482 = asymr[0]
                _483 = _481 * asymr_184_482
                _484 = traipl * _483
                asy = _f32(asy + _484)
                _pc = 123
                continue
            case 123:  # L.58
                _pc = 124
                continue
            case 124:  # __label_000130
                _485 = cntrl_imult[0]
                _486 = _485 == 1
                _487 = init == 0
                _488 = _486 & _487
                _pc = 125 if _488 != 0 else 130
                continue
            case 125:  # <D.17855>
                _489 = aer_xx1[0]
                _490 = aer_yy1[0]
                _491 = _489 - _490
                _492 = _491
                _493 = w7d * _492
                _494 = aer_xx2[0]
                _495 = aer_yy2[0]
                _496 = _494 - _495
                _497 = _496
                _498 = w12d * _497
                _499 = _493 + _498
                _500 = aer_xx3[0]
                _501 = aer_yy3[0]
                _502 = _500 - _501
                _503 = _502
                _504 = w13d * _503
                _505 = _499 + _504
                _506 = aer_xx4[0]
                _507 = aer_yy4[0]
                _508 = _506 - _507
                _509 = _508
                _510 = w14d * _509
                _511 = _505 + _510
                _512 = aer_xx5[0]
                _513 = aer_yy5[0]
                _514 = _512 - _513
                _515 = _514
                _516 = w16d * _515
                _517 = _511 + _516
                denom = _f32(_517)
                _518 = __BLNK___w[2]
                _pc = 126 if _518 != 0.0 else 127
                continue
            case 126:  # <D.17857>
                cssa_185_519 = cssa[0]
                _520 = 1.0e+0 - cssa_185_519
                _521 = _520
                _522 = traipl * _521
                denom = _f32(denom + _522)
                _pc = 127
                continue
            case 127:  # L.60
                ik_186_523 = ik[0]
                _pc = 128 if ik_186_523 > 1 else 129
                continue
            case 128:  # <D.17860>
                ik_187_524 = ik[0]
                _525 = ik_187_524 + -1
                _526 = _int(_525)
                _527 = _526 + -1
                msrd_asyik[_527] = asy
                ik_188_528 = ik[0]
                _529 = ik_188_528 + -1
                _530 = _int(_529)
                _531 = _530 + -1
                msrd_asydm[_531] = denom
                _pc = 129
                continue
            case 129:  # L.61
                _532 = cntrl_ikmax[0]
                _533 = _int(_532)
                _534 = _533 + -1
                _535 = msrd_asyik[0]
                msrd_asyik[_534] = _535
                _536 = cntrl_ikmax[0]
                _537 = _int(_536)
                _538 = _537 + -1
                _539 = msrd_asydm[0]
                msrd_asydm[_538] = _539
                _pc = 130
                continue
            case 130:  # L.59
                ext = _f32(sct + abt)
                sum = _f32(0.0)
                _540 = __BLNK___w[7]
                wo3 = _f32(_540 * 2.68999993801116943359375e-1)
                v_189_541 = v[0]
                _542 = v_189_541 > 2.437e+4
                v_190_543 = v[0]
                _544 = v_190_543 < 4.08e+4
                _545 = _542 & _544
                _pc = 131 if _545 != 0 else 132
                continue
            case 131:  # <D.17864>
                w1o3 = _f32(__BLNK___w[58])
                w2o3 = _f32(__BLNK___w[59])
                ct1_191_546 = ct1[0]
                _547 = w1o3 * ct1_191_546
                _548 = wo3 + _547
                ct2_192_549 = ct2[0]
                _550 = w2o3 * ct2_192_549
                _551 = _548 + _550
                _552 = _551
                c0_193_553 = c0[0]
                abbuv = _f32(_552 * c0_193_553)
                _pc = 132
                continue
            case 132:  # L.62
                v_194_554 = v[0]
                _pc = 133 if v_194_554 >= 4.08e+4 else 134
                continue
            case 133:  # <D.17867>
                c0_195_555 = c0[0]
                abbuv = _f32(wo3 * c0_195_555)
                _pc = 134
                continue
            case 134:  # L.63
                sum = _f32(sum + abbuv)
                jk = _int(4)
                _pc = 135
            case 135:  # <D.17870>
                D_7709 = _int(jk > 11)
                _pc = 144 if D_7709 != 0 else 136
                continue
            case 136:  # <D.17871>
                _556 = _int(jk)
                _557 = _556 + -1
                _558 = tran_abb[_557]
                _559 = _int(jk)
                _560 = _559 + -1
                _561 = __BLNK___w[_560]
                _562 = _int(jk)
                _563 = _562 + -1
                _564 = _558 * _561
                __BLNK___tx[_563] = _564
                _pc = 137 if jk == 5 else 138
                continue
            case 137:  # <D.17872>
                _565 = tran_abb[4]
                _566 = __BLNK___w[4]
                _567 = _566 * 9.9999996826552253889678874634872052240552875446155667305e-21
                _568 = _567
                _569 = _565 * _568
                __BLNK___tx[4] = _569
                _pc = 138
                continue
            case 138:  # L.66
                _pc = 139 if jk == 9 else 140
                continue
            case 139:  # <D.17875>
                _570 = tran_abb[8]
                _571 = __BLNK___w[8]
                _572 = _571 * 9.9999996826552253889678874634872052240552875446155667305e-21
                _573 = _572
                _574 = _570 * _573
                __BLNK___tx[8] = _574
                _pc = 140
                continue
            case 140:  # L.67
                _pc = 141 if jk == 10 else 142
                continue
            case 141:  # <D.17878>
                _575 = tran_abb[9]
                _576 = __BLNK___w[9]
                _577 = _576 * 9.9999996826552253889678874634872052240552875446155667305e-21
                _578 = _577
                _579 = _575 * _578
                __BLNK___tx[9] = _579
                _pc = 142
                continue
            case 142:  # __label_000125
                _580 = _int(jk)
                _581 = _580 + -1
                _582 = __BLNK___tx[_581]
                sum = _f32(sum + _582)
                _pc = 143
            case 143:  # L.64
                jk = _int(jk + 1)
                _pc = 135
                continue
            case 144:  # L.65
                _583 = __BLNK___tx[7]
                _584 = abbuv + _583
                __BLNK___tx[7] = _584
                _585 = cntrl_imult[0]
                _586 = _585 == 1
                _587 = init == 0
                _588 = _586 & _587
                _pc = 145 if _588 != 0 else 146
                continue
            case 145:  # <D.17881>
                _589 = __BLNK___tx[3]
                _590 = __BLNK___tx[4]
                _591 = _589 + _590
                _592 = __BLNK___tx[7]
                _593 = _591 + _592
                _594 = __BLNK___tx[8]
                _595 = _593 + _594
                _596 = __BLNK___tx[9]
                _597 = _595 + _596
                _598 = __BLNK___tx[10]
                ik_196_599 = ik[0]
                _600 = _int(ik_196_599)
                _601 = _600 + -1
                _602 = _597 + _598
                tran_dcont[_601] = _602
                _pc = 146
                continue
            case 146:  # L.69
                _603 = __BLNK___tx[4]
                _604 = __BLNK___tx[9]
                _605 = _603 + _604
                _606 = __BLNK___tx[8]
                _607 = _605 + _606
                __BLNK___tx[4] = _607
                __BLNK___tx[9] = abt
                __BLNK___tx[6] = ext
                _608 = cntrl_imult[0]
                _609 = _608 == 1
                _610 = init == 0
                _611 = _609 & _610
                _pc = 147 if _611 != 0 else 148
                continue
            case 147:  # <D.17884>
                ik_197_612 = ik[0]
                _613 = _int(ik_197_612)
                _614 = _613 + -1
                _615 = __BLNK___tx[6]
                msrd_dtx7[_614] = _615
                _616 = __BLNK___tx[6]
                _617 = __BLNK___tx[9]
                ik_198_618 = ik[0]
                _619 = _int(ik_198_618)
                _620 = _619 + -1
                _621 = _616 - _617
                msrd_daers[_620] = _621
                ik_199_622 = ik[0]
                _623 = _int(ik_199_622)
                _624 = _623 + -1
                _625 = __BLNK___tx[5]
                msrd_dmols[_624] = _625
                _pc = 148
                continue
            case 148:  # L.70
                _626 = __BLNK___tx[6]
                sum = _f32(sum + _626)
                _627 = card2_icld[0]
                _pc = 149 if _627 == 20 else 150
                continue
            case 149:  # <D.17887>
                _628 = __BLNK___w[15]
                _629 = _628 * 2.0e+0
                __BLNK___tx[15] = _629
                _630 = __BLNK___tx[15]
                sum = _f32(sum + _630)
                _pc = 150
                continue
            case 150:  # L.71
                _631 = __BLNK___w[0]
                _632 = __BLNK___w[62]
                _633 = _632 * 2.2e+2
                wt2 = _f32(_631 - _633)
                _634 = __BLNK___w[62]
                sigo2a_200_635 = sigo2a[0]
                _636 = wt2 * sigo2a_200_635
                _637 = _634 + _636
                _638 = __BLNK___w[1]
                sigo2b_201_639 = sigo2b[0]
                _640 = _638 * sigo2b_201_639
                _641 = _637 + _640
                _642 = _641
                sigo20_202_643 = sigo20[0]
                _644 = _642 * sigo20_202_643
                __BLNK___tx[57] = _644
                _645 = __BLNK___w[57]
                _646 = tran_abb[16]
                _647 = _645 * _646
                _648 = __BLNK___tx[57]
                _649 = _647 + _648
                __BLNK___tx[57] = _649
                _650 = cntrl_imult[0]
                _651 = _650 == 1
                _652 = init == 0
                _653 = _651 & _652
                _pc = 151 if _653 != 0 else 152
                continue
            case 151:  # <D.17890>
                ik_203_654 = ik[0]
                _655 = _int(ik_203_654)
                _656 = _655 + -1
                _657 = tran_dcont[_656]
                _658 = __BLNK___tx[57]
                ik_204_659 = ik[0]
                _660 = _int(ik_204_659)
                _661 = _660 + -1
                _662 = _657 + _658
                tran_dcont[_661] = _662
                _pc = 152
                continue
            case 152:  # L.72
                _663 = __BLNK___tx[57]
                __BLNK___tx[2] = _663
                __BLNK___tx[8] = sum
                k = _int(3)
                _pc = 153
            case 153:  # <D.17893>
                D_7720 = _int(k > 16)
                _pc = 159 if D_7720 != 0 else 154
                continue
            case 154:  # <D.17894>
                _664 = _int(k)
                _665 = _664 + -1
                _666 = __BLNK___tx[_665]
                _667 = cnstns_bigexp[0]
                _pc = 155 if _666 > _667 else 156
                continue
            case 155:  # <D.17895>
                _pc = 157
                continue
            case 156:  # L.75
                _668 = _int(k)
                _669 = _668 + -1
                _670 = __BLNK___tx[_669]
                _671 = -_670
                _672 = _int(k)
                _673 = _672 + -1
                _674 = __builtin_expf(_671)
                __BLNK___tx[_673] = _674
                _pc = 158
                continue
            case 157:  # __label_000200
                _675 = cnstns_bignum[0]
                _676 = _int(k)
                _677 = _676 + -1
                _678 = _div(1.0e+0, _675)
                __BLNK___tx[_677] = _678
                _pc = 158
            case 158:  # L.73
                k = _int(k + 1)
                _pc = 153
                continue
            case 159:  # L.74
                _679 = __BLNK___tx[2]
                __BLNK___tx[57] = _679
                __BLNK___tx[2] = 1.0e+0
                imol = _int(1)
                temp = _f32(1.0e+0)
                _680 = _int(imol)
                _681 = _680 + -1
                _682 = aabbcc_cps[_681]
                cp[0] = _682
                cp_205_683 = cp[0]
                _pc = 160 if cp_205_683 == -2.0e+1 else 161
                continue
            case 160:  # <D.17897>
                _pc = 162
                continue
            case 161:  # L.76
                _684 = _int(imol)
                _685 = _684 + -1
                ib = _int(aabbcc_ibnd[_685])
                _686 = _int(imol)
                _687 = _686 + -1
                _688 = aabbcc_a[_687:]
                _689 = _int(ib)
                _690 = _689 + -1
                _691 = __BLNK___w[_690:]
                temp = _f32(_ft_dbltx(_state, _691, cp, _688))
                _pc = 162
            case 162:  # __label_001001
                __BLNK___tx[16] = temp
                imol = _int(2)
                temp = _f32(1.0e+0)
                _692 = _int(imol)
                _693 = _692 + -1
                _694 = aabbcc_cps[_693]
                cp[0] = _694
                cp_206_695 = cp[0]
                _pc = 163 if cp_206_695 == -2.0e+1 else 164
                continue
            case 163:  # <D.17899>
                _pc = 165
                continue
            case 164:  # L.77
                _696 = _int(imol)
                _697 = _696 + -1
                ib = _int(aabbcc_ibnd[_697])
                _698 = _int(imol)
                _699 = _698 + -1
                _700 = aabbcc_a[_699:]
                _701 = _int(ib)
                _702 = _701 + -1
                _703 = __BLNK___w[_702:]
                temp = _f32(_ft_dbltx(_state, _703, cp, _700))
                _pc = 165
            case 165:  # __label_001002
                __BLNK___tx[35] = temp
                imol = _int(3)
                temp = _f32(1.0e+0)
                _704 = _int(imol)
                _705 = _704 + -1
                _706 = aabbcc_cps[_705]
                cp[0] = _706
                cp_207_707 = cp[0]
                _pc = 166 if cp_207_707 == -2.0e+1 else 167
                continue
            case 166:  # <D.17901>
                _pc = 168
                continue
            case 167:  # L.78
                _708 = _int(imol)
                _709 = _708 + -1
                ib = _int(aabbcc_ibnd[_709])
                _710 = _int(imol)
                _711 = _710 + -1
                _712 = aabbcc_a[_711:]
                _713 = _int(ib)
                _714 = _713 + -1
                _715 = __BLNK___w[_714:]
                temp = _f32(_ft_dbltx(_state, _715, cp, _712))
                _pc = 168
            case 168:  # __label_001003
                __BLNK___tx[30] = temp
                imol = _int(4)
                temp = _f32(1.0e+0)
                _716 = _int(imol)
                _717 = _716 + -1
                _718 = aabbcc_cps[_717]
                cp[0] = _718
                cp_208_719 = cp[0]
                _pc = 169 if cp_208_719 == -2.0e+1 else 170
                continue
            case 169:  # <D.17903>
                _pc = 171
                continue
            case 170:  # L.79
                _720 = _int(imol)
                _721 = _720 + -1
                ib = _int(aabbcc_ibnd[_721])
                _722 = _int(imol)
                _723 = _722 + -1
                _724 = aabbcc_a[_723:]
                _725 = _int(ib)
                _726 = _725 + -1
                _727 = __BLNK___w[_726:]
                temp = _f32(_ft_dbltx(_state, _727, cp, _724))
                _pc = 171
            case 171:  # __label_001004
                __BLNK___tx[46] = temp
                imol = _int(5)
                temp = _f32(1.0e+0)
                _728 = _int(imol)
                _729 = _728 + -1
                _730 = aabbcc_cps[_729]
                cp[0] = _730
                cp_209_731 = cp[0]
                _pc = 172 if cp_209_731 == -2.0e+1 else 173
                continue
            case 172:  # <D.17905>
                _pc = 174
                continue
            case 173:  # L.80
                _732 = _int(imol)
                _733 = _732 + -1
                ib = _int(aabbcc_ibnd[_733])
                _734 = _int(imol)
                _735 = _734 + -1
                _736 = aabbcc_a[_735:]
                _737 = _int(ib)
                _738 = _737 + -1
                _739 = __BLNK___w[_738:]
                temp = _f32(_ft_dbltx(_state, _739, cp, _736))
                _pc = 174
            case 174:  # __label_001005
                __BLNK___tx[43] = temp
                imol = _int(6)
                temp = _f32(1.0e+0)
                _740 = _int(imol)
                _741 = _740 + -1
                _742 = aabbcc_cps[_741]
                cp[0] = _742
                cp_210_743 = cp[0]
                _pc = 175 if cp_210_743 == -2.0e+1 else 176
                continue
            case 175:  # <D.17907>
                _pc = 177
                continue
            case 176:  # L.81
                _744 = _int(imol)
                _745 = _744 + -1
                ib = _int(aabbcc_ibnd[_745])
                _746 = _int(imol)
                _747 = _746 + -1
                _748 = aabbcc_a[_747:]
                _749 = _int(ib)
                _750 = _749 + -1
                _751 = __BLNK___w[_750:]
                temp = _f32(_ft_dbltx(_state, _751, cp, _748))
                _pc = 177
            case 177:  # __label_001006
                __BLNK___tx[45] = temp
                imol = _int(7)
                temp = _f32(1.0e+0)
                _752 = _int(imol)
                _753 = _752 + -1
                _754 = aabbcc_cps[_753]
                cp[0] = _754
                cp_211_755 = cp[0]
                _pc = 178 if cp_211_755 == -2.0e+1 else 179
                continue
            case 178:  # <D.17909>
                _pc = 180
                continue
            case 179:  # L.82
                _756 = _int(imol)
                _757 = _756 + -1
                ib = _int(aabbcc_ibnd[_757])
                _758 = _int(imol)
                _759 = _758 + -1
                _760 = aabbcc_a[_759:]
                _761 = _int(ib)
                _762 = _761 + -1
                _763 = __BLNK___w[_762:]
                temp = _f32(_ft_dbltx(_state, _763, cp, _760))
                _pc = 180
            case 180:  # __label_001007
                __BLNK___tx[49] = temp
                imol = _int(8)
                temp = _f32(1.0e+0)
                _764 = _int(imol)
                _765 = _764 + -1
                _766 = aabbcc_cps[_765]
                cp[0] = _766
                cp_212_767 = cp[0]
                _pc = 181 if cp_212_767 == -2.0e+1 else 182
                continue
            case 181:  # <D.17911>
                _pc = 183
                continue
            case 182:  # L.83
                _768 = _int(imol)
                _769 = _768 + -1
                ib = _int(aabbcc_ibnd[_769])
                _770 = _int(imol)
                _771 = _770 + -1
                _772 = aabbcc_a[_771:]
                _773 = _int(ib)
                _774 = _773 + -1
                _775 = __BLNK___w[_774:]
                temp = _f32(_ft_dbltx(_state, _775, cp, _772))
                _pc = 183
            case 183:  # __label_001008
                __BLNK___tx[53] = temp
                imol = _int(9)
                temp = _f32(1.0e+0)
                _776 = _int(imol)
                _777 = _776 + -1
                _778 = aabbcc_cps[_777]
                cp[0] = _778
                cp_213_779 = cp[0]
                _pc = 184 if cp_213_779 == -2.0e+1 else 185
                continue
            case 184:  # <D.17913>
                _pc = 186
                continue
            case 185:  # L.84
                _780 = _int(imol)
                _781 = _780 + -1
                ib = _int(aabbcc_ibnd[_781])
                _782 = _int(imol)
                _783 = _782 + -1
                _784 = aabbcc_a[_783:]
                _785 = _int(ib)
                _786 = _785 + -1
                _787 = __BLNK___w[_786:]
                temp = _f32(_ft_dbltx(_state, _787, cp, _784))
                _pc = 186
            case 186:  # __label_001009
                __BLNK___tx[55] = temp
                imol = _int(10)
                temp = _f32(1.0e+0)
                _788 = _int(imol)
                _789 = _788 + -1
                _790 = aabbcc_cps[_789]
                cp[0] = _790
                cp_214_791 = cp[0]
                _pc = 187 if cp_214_791 == -2.0e+1 else 188
                continue
            case 187:  # <D.17915>
                _pc = 189
                continue
            case 188:  # L.85
                _792 = _int(imol)
                _793 = _792 + -1
                ib = _int(aabbcc_ibnd[_793])
                _794 = _int(imol)
                _795 = _794 + -1
                _796 = aabbcc_a[_795:]
                _797 = _int(ib)
                _798 = _797 + -1
                _799 = __BLNK___w[_798:]
                temp = _f32(_ft_dbltx(_state, _799, cp, _796))
                _pc = 189
            case 189:  # __label_001010
                __BLNK___tx[54] = temp
                imol = _int(11)
                temp = _f32(1.0e+0)
                _800 = _int(imol)
                _801 = _800 + -1
                _802 = aabbcc_cps[_801]
                cp[0] = _802
                cp_215_803 = cp[0]
                _pc = 190 if cp_215_803 == -2.0e+1 else 191
                continue
            case 190:  # <D.17917>
                _pc = 192
                continue
            case 191:  # L.86
                _804 = _int(imol)
                _805 = _804 + -1
                ib = _int(aabbcc_ibnd[_805])
                _806 = _int(imol)
                _807 = _806 + -1
                _808 = aabbcc_a[_807:]
                _809 = _int(ib)
                _810 = _809 + -1
                _811 = __BLNK___w[_810:]
                temp = _f32(_ft_dbltx(_state, _811, cp, _808))
                _pc = 192
            case 192:  # __label_001011
                __BLNK___tx[51] = temp
                _812 = __BLNK___tx[35]
                _813 = __BLNK___tx[43]
                _814 = _812 * _813
                _815 = __BLNK___tx[45]
                _816 = _814 * _815
                _817 = __BLNK___tx[46]
                _818 = _816 * _817
                _819 = __BLNK___tx[49]
                _820 = _818 * _819
                _821 = __BLNK___tx[57]
                unif = _f32(_820 * _821)
                _822 = __BLNK___tx[51]
                _823 = __BLNK___tx[53]
                _824 = _822 * _823
                _825 = __BLNK___tx[54]
                _826 = _824 * _825
                _827 = __BLNK___tx[55]
                trace = _f32(_826 * _827)
                _828 = __BLNK___tx[16]
                _829 = unif * _828
                _830 = __BLNK___tx[30]
                _831 = _829 * _830
                _832 = __BLNK___tx[8]
                _833 = _831 * _832
                _834 = trace * _833
                __BLNK___tx[8] = _834
                iv_216_835 = iv[0]
                _pc = 193 if iv_216_835 > 12999 else 194
                continue
            case 193:  # <D.17919>
                _836 = __BLNK___tx[7]
                __BLNK___tx[30] = _836
                _pc = 194
                continue
            case 194:  # __label_001020
                ipath_217_837 = ipath[0]
                _pc = 195 if ipath_217_837 == 1 else 196
                continue
            case 195:  # <D.17922>
                _838 = __BLNK___tx[8]
                msrd_dstrn[0] = _838
                _pc = 196
                continue
            case 196:  # L.88
                _839 = cntrl_imult[0]
                _840 = _839 == 1
                _841 = init == 0
                _842 = _840 & _841
                _pc = 197 if _842 != 0 else 202
                continue
            case 197:  # <D.17925>
                ipath_218_843 = ipath[0]
                _pc = 198 if ipath_218_843 == 2 else 199
                continue
            case 198:  # <D.17927>
                ik_219_844 = ik[0]
                _845 = _int(ik_219_844)
                _846 = __BLNK___tx[8]
                msrd_dstrn[_845] = _846
                _pc = 199
                continue
            case 199:  # L.90
                _847 = card1_iemsct[0]
                _pc = 200 if _847 == 1 else 201
                continue
            case 200:  # <D.17930>
                ik_220_848 = ik[0]
                _849 = _int(ik_220_848)
                msrd_dstrn[_849] = 1.0e+0
                _pc = 201
                continue
            case 201:  # L.91
                _pc = 202
                continue
            case 202:  # L.89
                _pc = 203 if iscttr == 0 else 204
                continue
            case 203:  # <D.17934>
                _pc = 214
                continue
            case 204:  # L.92
                _850 = cntrl_imult[0]
                _851 = _850 == 1
                _852 = init == 0
                _853 = _851 & _852
                _pc = 205 if _853 != 0 else 206
                continue
            case 205:  # <D.17936>
                _pc = 210
                continue
            case 206:  # __label_000206
                ik_221_854 = ik[0]
                _855 = ml1 >= ik_221_854
                _856 = cntrl_imult[0]
                _857 = _856 == 1
                _858 = _855 & _857
                _pc = 207 if _858 != 0 else 208
                continue
            case 207:  # <D.17938>
                _ft_ssrad(_state, iph, ik, itzero, ipath, v, sumssr)
                _pc = 208
                continue
            case 208:  # L.94
                _859 = cntrl_imult[0]
                _pc = 209 if _859 == 0 else 210
                continue
            case 209:  # <D.17941>
                _ft_ssrad(_state, iph, ik, itzero, ipath, v, sumssr)
                _pc = 210
                continue
            case 210:  # __label_000207
                ipath_222_860 = ipath[0]
                _pc = 211 if ipath_222_860 == 3 else 212
                continue
            case 211:  # <D.17944>
                _pc = 213
                continue
            case 212:  # L.96
                ipath_223_861 = ipath[0]
                _862 = ipath_223_861 + 1
                ipath[0] = _862
                _pc = 68
                continue
            case 213:  # __label_000208
                ipath[0] = 2
                _pc = 214
            case 214:  # __label_000209
                iv_224_863 = iv[0]
                _pc = 215 if iv_224_863 > 12999 else 216
                continue
            case 215:  # <D.17946>
                _864 = __BLNK___tx[7]
                __BLNK___tx[2] = _864
                _pc = 216
                continue
            case 216:  # L.97
                alam = _f32(9.999998046875e+3)
                v_225_865 = v[0]
                _pc = 217 if v_225_865 > 0.0 else 218
                continue
            case 217:  # <D.17949>
                v_226_866 = v[0]
                alam = _f32(_div(1.0e+4, v_226_866))
                _pc = 218
                continue
            case 218:  # L.98
                _867 = card1_iemsct[0]
                _868 = _867 == 0
                _869 = card1_iemsct[0]
                _870 = _869 == 3
                _871 = _868 | _870
                _pc = 219 if _871 != 0 else 220
                continue
            case 219:  # <D.17952>
                _pc = 244
                continue
            case 220:  # L.99
                ik_227_872 = ik[0]
                _873 = _int(ik_227_872)
                _874 = _873 + -1
                _875 = __BLNK___tbby[_874:]
                bbik = _f32(_ft_bbfn(_state, _875, v))
                tlnew = _f32(__BLNK___tx[8])
                dtau = _f32(tlold - tlnew)
                _876 = cntrl_imult[0]
                _pc = 221 if _876 == 1 else 222
                continue
            case 221:  # <D.17954>
                _877 = __BLNK___tx[8]
                dtau = _f32(total - _877)
                _pc = 222
                continue
            case 222:  # L.100
                total = _f32(__BLNK___tx[8])
                _pc = 223 if dtau <= 0.0 else 224
                continue
            case 223:  # <D.17957>
                dtau = _f32(0.0)
                _pc = 224
                continue
            case 224:  # L.101
                _878 = cntrl_imult[0]
                _pc = 225 if _878 == 0 else 230
                continue
            case 225:  # <D.17960>
                _879 = card1_noprnt[0]
                _pc = 226 if _879 == -1 else 227
                continue
            case 226:  # __label_001210
                _pc = 227
                continue
            case 227:  # L.103
                _880 = card1_iemsct[0]
                _881 = _880 <= 1
                _882 = dtau < 9.99999974737875163555145263671875e-6
                _883 = _881 & _882
                _884 = tlnew < 9.99999974737875163555145263671875e-6
                _885 = _883 & _884
                _pc = 228 if _885 != 0 else 229
                continue
            case 228:  # __label_001220
                _pc = 244
                continue
            case 229:  # L.104
                _886 = bbik * dtau
                sumv = _f32(sumv + _886)
                _pc = 242
                continue
            case 230:  # <D.17961>
                _pc = 231 if init == 0 else 232
                continue
            case 231:  # <D.17968>
                _pc = 243
                continue
            case 232:  # L.105
                _887 = cntrl_ml[0]
                ik_228_888 = ik[0]
                _889 = _int(ik_228_888)
                _890 = _889 + -1
                _891 = imap[_890]
                _892 = _887 - _891
                n1 = _int(ioff + _892)
                _893 = cntrl_ml[0]
                _pc = 233 if n1 >= _893 else 234
                continue
            case 233:  # <D.17970>
                _894 = cntrl_ml[0]
                n1 = _int(_894 + -1)
                _pc = 234
                continue
            case 234:  # L.106
                _895 = card1_noprnt[0]
                _pc = 235 if _895 == -1 else 236
                continue
            case 235:  # <D.17973>
                n = _int(n1 + 1)
                _pc = 236
                continue
            case 236:  # L.107
                _896 = dtau < 9.99999974737875163555145263671875e-6
                _897 = __BLNK___tx[8]
                _898 = _897 < 9.99999974737875163555145263671875e-6
                _899 = _896 & _898
                _pc = 237 if _899 != 0 else 238
                continue
            case 237:  # <D.17976>
                _pc = 244
                continue
            case 238:  # L.108
                ik_229_900 = ik[0]
                _901 = _int(ik_229_900)
                _902 = _901 + -1
                _903 = path_qtheta[_902]
                _904 = cnstns_pi[0]
                _905 = _div(_904, 2.0e+0)
                _906 = _905
                _pc = 239 if _903 < _906 else 240
                continue
            case 239:  # <D.17978>
                _907 = _int(n1)
                _908 = _907 + -1
                _909 = msrd_omega0[_908]
                _910 = 1.0e+0 - _909
                _911 = _910
                _912 = bbik * _911
                _913 = _int(n1)
                _914 = _913 + -1
                _915 = msrd_omega0[_914]
                _916 = cnstns_pi[0]
                _917 = _div(_915, _916)
                _918 = _int(n1)
                _919 = _918 + -1
                _920 = dmf[_919]
                ik_230_921 = ik[0]
                _922 = _int(ik_230_921)
                _923 = _922 + -1
                _924 = bet[_923]
                _925 = 1.0e+0 - _924
                _926 = _925
                _927 = _920 * _926
                _928 = _int(n1)
                _929 = _928 + -1
                _930 = umf[_929]
                ik_231_931 = ik[0]
                _932 = _int(ik_231_931)
                _933 = _932 + -1
                _934 = bet[_933]
                _935 = _930 * _934
                _936 = _927 + _935
                _937 = _936
                _938 = _917 * _937
                sms = _f32(_912 + _938)
                _939 = _int(n1)
                _940 = _939 + -1
                _941 = msrd_omega0[_940]
                _942 = cnstns_pi[0]
                _943 = _div(_941, _942)
                _944 = _int(n1)
                _945 = _944 + -1
                _946 = dmfs[_945]
                ik_232_947 = ik[0]
                _948 = _int(ik_232_947)
                _949 = _948 + -1
                _950 = bet[_949]
                _951 = 1.0e+0 - _950
                _952 = _951
                _953 = _946 * _952
                _954 = _int(n1)
                _955 = _954 + -1
                _956 = umfs[_955]
                ik_233_957 = ik[0]
                _958 = _int(ik_233_957)
                _959 = _958 + -1
                _960 = bet[_959]
                _961 = _956 * _960
                _962 = _953 + _961
                _963 = _962
                smss = _f32(_943 * _963)
                _pc = 241
                continue
            case 240:  # <D.17979>
                _964 = _int(n1)
                _965 = _964 + -1
                _966 = msrd_omega0[_965]
                _967 = 1.0e+0 - _966
                _968 = _967
                _969 = bbik * _968
                _970 = _int(n1)
                _971 = _970 + -1
                _972 = msrd_omega0[_971]
                _973 = cnstns_pi[0]
                _974 = _div(_972, _973)
                _975 = _int(n1)
                _976 = _975 + -1
                _977 = umf[_976]
                ik_234_978 = ik[0]
                _979 = _int(ik_234_978)
                _980 = _979 + -1
                _981 = bet[_980]
                _982 = 1.0e+0 - _981
                _983 = _982
                _984 = _977 * _983
                _985 = _int(n1)
                _986 = _985 + -1
                _987 = dmf[_986]
                ik_235_988 = ik[0]
                _989 = _int(ik_235_988)
                _990 = _989 + -1
                _991 = bet[_990]
                _992 = _987 * _991
                _993 = _984 + _992
                _994 = _993
                _995 = _974 * _994
                sms = _f32(_969 + _995)
                _996 = _int(n1)
                _997 = _996 + -1
                _998 = msrd_omega0[_997]
                _999 = cnstns_pi[0]
                _1000 = _div(_998, _999)
                _1001 = _int(n1)
                _1002 = _1001 + -1
                _1003 = umfs[_1002]
                ik_236_1004 = ik[0]
                _1005 = _int(ik_236_1004)
                _1006 = _1005 + -1
                _1007 = bet[_1006]
                _1008 = 1.0e+0 - _1007
                _1009 = _1008
                _1010 = _1003 * _1009
                _1011 = _int(n1)
                _1012 = _1011 + -1
                _1013 = dmfs[_1012]
                ik_237_1014 = ik[0]
                _1015 = _int(ik_237_1014)
                _1016 = _1015 + -1
                _1017 = bet[_1016]
                _1018 = _1013 * _1017
                _1019 = _1010 + _1018
                _1020 = _1019
                smss = _f32(_1000 * _1020)
                _pc = 241
            case 241:  # L.109
                _1021 = sms * dtau
                sumv = _f32(sumv + _1021)
                _1022 = smss * dtau
                summs = _f32(summs + _1022)
                _pc = 242
            case 242:  # L.102
                tlold = _f32(tlnew)
                _pc = 243
            case 243:  # L.30
                ik_238_1023 = ik[0]
                _1024 = ik_238_1023 + 1
                ik[0] = _1024
                _pc = 63
                continue
            case 244:  # __label_000220
                _1025 = cntrl_imult[0]
                _pc = 245 if _1025 == 0 else 246
                continue
            case 245:  # <D.17981>
                _pc = 257
                continue
            case 246:  # L.110
                _pc = 247 if init != 0 else 248
                continue
            case 247:  # <D.17983>
                _pc = 257
                continue
            case 248:  # L.111
                _ft_msrad(_state, iv, v, isourc, iday, anglem, ss, dmf, dmfs, umf, umfs)
                _1026 = card1_noprnt[0]
                _pc = 249 if _1026 == -1 else 250
                continue
            case 249:  # __label_001230
                _pc = 250
                continue
            case 250:  # L.112
                _1027 = cntrl_ikmax[0]
                ikmax1 = _int(_1027 + -1)
                _1028 = cntrl_ikmax[0]
                ikmaxp = _int(_1028 + 1)
                _1029 = _int(ikmax1)
                _1030 = _1029 + -1
                _1031 = cntrl_ikmax[0]
                _1032 = _int(_1031)
                _1033 = _1032 + -1
                _1034 = msrd_cosbar[_1030]
                msrd_cosbar[_1033] = _1034
                _1035 = _int(ikmax1)
                _1036 = _1035 + -1
                _1037 = cntrl_ikmax[0]
                _1038 = _int(_1037)
                _1039 = _1038 + -1
                _1040 = msrd_omega0[_1036]
                msrd_omega0[_1039] = _1040
                _1041 = _int(ikmax1)
                _1042 = _1041 + -1
                _1043 = cntrl_ikmax[0]
                _1044 = _int(_1043)
                _1045 = _1044 + -1
                _1046 = umf[_1042]
                umf[_1045] = _1046
                _1047 = _int(ikmax1)
                _1048 = _1047 + -1
                _1049 = cntrl_ikmax[0]
                _1050 = _int(_1049)
                _1051 = _1050 + -1
                _1052 = umfs[_1048]
                umfs[_1051] = _1052
                _1053 = _int(ikmax1)
                _1054 = _1053 + -1
                _1055 = cntrl_ikmax[0]
                _1056 = _int(_1055)
                _1057 = _1056 + -1
                _1058 = dmfs[_1054]
                dmfs[_1057] = _1058
                _1059 = _int(ikmax1)
                _1060 = _1059 + -1
                _1061 = _int(ikmaxp)
                _1062 = _1061 + -1
                _1063 = msrd_cosbar[_1060]
                msrd_cosbar[_1062] = _1063
                _1064 = _int(ikmax1)
                _1065 = _1064 + -1
                _1066 = _int(ikmaxp)
                _1067 = _1066 + -1
                _1068 = msrd_omega0[_1065]
                msrd_omega0[_1067] = _1068
                _1069 = _int(ikmax1)
                _1070 = _1069 + -1
                _1071 = _int(ikmaxp)
                _1072 = _1071 + -1
                _1073 = umf[_1070]
                umf[_1072] = _1073
                _1074 = _int(ikmax1)
                _1075 = _1074 + -1
                _1076 = _int(ikmaxp)
                _1077 = _1076 + -1
                _1078 = umfs[_1075]
                umfs[_1077] = _1078
                _1079 = _int(ikmax1)
                _1080 = _1079 + -1
                _1081 = _int(ikmaxp)
                _1082 = _1081 + -1
                _1083 = dmfs[_1080]
                dmfs[_1082] = _1083
                cntrl_ikmax[0] = ikmx
                init = _int(init + 1)
                D_7814 = _int(cntrl_ikmax[0])
                ik[0] = 1
                _pc = 251
            case 251:  # <D.17988>
                ik_239_1084 = ik[0]
                D_7817 = _int(D_7814 < ik_239_1084)
                _pc = 256 if D_7817 != 0 else 252
                continue
            case 252:  # <D.17989>
                _1085 = cntrl_ml[0]
                ik_240_1086 = ik[0]
                _1087 = _int(ik_240_1086)
                _1088 = _1087 + -1
                _1089 = imap[_1088]
                _1090 = _1085 - _1089
                n = _int(ioff + _1090)
                ik_241_1091 = ik[0]
                _1092 = _int(ik_241_1091)
                _1093 = _1092 + -1
                _1094 = path_qtheta[_1093]
                _1095 = __builtin_cosf(_1094)
                _1096 = abs(_1095)
                cozen[0] = _1096
                _1097 = _int(n)
                _1098 = _1097 + -1
                _1099 = msrd_cosbar[_1098]
                _pc = 253 if _1099 == 0.0 else 254
                continue
            case 253:  # <D.17990>
                ik_242_1100 = ik[0]
                _1101 = _int(ik_242_1100)
                _1102 = _1101 + -1
                bet[_1102] = 5.0e-1
                _pc = 255
                continue
            case 254:  # <D.17991>
                _1103 = _int(n)
                _1104 = _1103 + -1
                _1105 = msrd_cosbar[_1104:]
                ik_243_1106 = ik[0]
                _1107 = _int(ik_243_1106)
                _1108 = _1107 + -1
                _1109 = _ft_betabs(_state, cozen, _1105)
                bet[_1108] = _1109
                _pc = 255
            case 255:  # L.113
                ik_244_1110 = ik[0]
                _1111 = ik_244_1110 + 1
                ik[0] = _1111
                _pc = 251
                continue
            case 256:  # L.114
                _1112 = cntrl_ikmax[0]
                _1113 = _1112 + 1
                _1114 = _int(_1113)
                _1115 = _1114 + -1
                bet[_1115] = 5.0e-1
                _pc = 62
                continue
            case 257:  # __label_000266
                iv_245_1116 = iv[0]
                _pc = 258 if iv1 < iv_245_1116 else 259
                continue
            case 258:  # <D.17993>
                factor = _f32(1.0e+0)
                _pc = 259
                continue
            case 259:  # L.116
                iv_246_1117 = iv[0]
                _pc = 260 if iv2 <= iv_246_1117 else 261
                continue
            case 260:  # <D.17996>
                factor = _f32(5.0e-1)
                _pc = 261
                continue
            case 261:  # L.117
                _1118 = card4_dv[0]
                _1119 = factor * _1118
                _1120 = __BLNK___tx[8]
                _1121 = 1.0e+0 - _1120
                _1122 = _1121
                _1123 = _1119 * _1122
                suma = _f32(suma + _1123)
                _1124 = card1_iemsct[0]
                iiii = _int(_1124 + 1)
                altx9 = _f32(cnstns_bignum[0])
                _1125 = __BLNK___tx[8]
                _pc = 262 if _1125 > 0.0 else 263
                continue
            case 262:  # <D.17999>
                _1126 = __BLNK___tx[8]
                _1127 = __builtin_logf(_1126)
                altx9 = _f32(-_1127)
                _pc = 263
                continue
            case 263:  # L.118
                _pc = {1: 264, 2: 266, 3: 268, 4: 270}.get(iiii, 272)
                continue
            case 264:  # L.121
                _pc = 272
                continue
            case 265:  # continuation_677
                _pc = 272
                continue
            case 266:  # L.122
                _pc = 274
                continue
            case 267:  # continuation_680
                _pc = 272
                continue
            case 268:  # L.123
                _pc = 274
                continue
            case 269:  # continuation_683
                _pc = 272
                continue
            case 270:  # L.124
                _pc = 303
                continue
            case 271:  # continuation_686
                _pc = 272
                continue
            case 272:  # __label_000300
                _1128 = __BLNK___tx[9]
                _1129 = 1.0e+0 - _1128
                __BLNK___tx[9] = _1129
                _1130 = __BLNK___tx[6]
                _1131 = __BLNK___tx[15]
                _1132 = _1130 * _1131
                __BLNK___tx[6] = _1132
                _1133 = __BLNK___tx[49]
                _1134 = __BLNK___tx[57]
                _1135 = _1133 * _1134
                __BLNK___tx[49] = _1135
                _pc = 273
            case 273:  # __label_000907
                _pc = 307
                continue
            case 274:  # __label_000400
                surdtr = _f32(0.0)
                _1136 = imlt == 1
                _1137 = card3_h2[0]
                _1138 = _1137 == 0.0
                _1139 = _1136 & _1138
                _pc = 275 if _1139 != 0 else 276
                continue
            case 275:  # <D.18003>
                _1140 = card1_salb[0]
                _1141 = msrd_fdntrt[0]
                _1142 = _1140 * _1141
                _1143 = __BLNK___tx[8]
                _1144 = _1142 * _1143
                _1145 = cnstns_pi[0]
                surdtr = _f32(_div(_1144, _1145))
                _pc = 276
                continue
            case 276:  # L.125
                _1146 = card1_tbound[0]
                _pc = 277 if _1146 <= 0.0 else 278
                continue
            case 277:  # <D.18006>
                bbg = _f32(0.0)
                _pc = 279
                continue
            case 278:  # <D.18007>
                _1147 = _ft_bbfn(_state, card1_tbound, v)
                _1148 = __BLNK___tx[8]
                _1149 = _1147 * _1148
                _1150 = emiss * _1149
                bbg = _f32(surdtr + _1150)
                _pc = 279
            case 279:  # L.126
                sumv = _f32(sumv + bbg)
                sumvv = _f32(sumv)
                v_247_1151 = v[0]
                _pc = 280 if v_247_1151 > 0.0 else 281
                continue
            case 280:  # <D.18009>
                D_7841 = _f32(v[0])
                D_7842 = _f32(D_7841 * D_7841)
                _1152 = _div(1.0e+4, D_7842)
                _1153 = _1152
                sumv = _f32(sumv * _1153)
                _pc = 281
                continue
            case 281:  # L.127
                _1154 = card1_iemsct[0]
                _pc = 282 if _1154 == 2 else 283
                continue
            case 282:  # <D.18012>
                _pc = 285
                continue
            case 283:  # L.128
                _1155 = card4_dv[0]
                _1156 = factor * _1155
                _1157 = sumv * _1156
                radsum = _f32(radsum + _1157)
                _pc = 284
            case 284:  # __label_000917
                sumt = _f32(sumv)
                sumtt = _f32(sumvv)
                _pc = 307
                continue
            case 285:  # __label_000500
                _ft_source(_state, v, isourc, iday, anglem, ss)
                sumssr_248_1158 = sumssr[0]
                ss_249_1159 = ss[0]
                sumsss = _f32(sumssr_248_1158 * ss_249_1159)
                _1160 = sumsss + summs
                sumssr[0] = _1160
                sums = _f32(0.0)
                sumss = _f32(0.0)
                v_250_1161 = v[0]
                _pc = 286 if v_250_1161 > 0.0 else 287
                continue
            case 286:  # <D.18014>
                D_7854 = _f32(v[0])
                D_7855 = _f32(D_7854 * D_7854)
                _1162 = _div(1.0e+4, D_7855)
                _1163 = _1162
                sumssr_251_1164 = sumssr[0]
                sums = _f32(_1163 * sumssr_251_1164)
                _pc = 287
                continue
            case 287:  # L.129
                v_252_1165 = v[0]
                _pc = 288 if v_252_1165 > 0.0 else 289
                continue
            case 288:  # <D.18017>
                D_7857 = _f32(v[0])
                D_7858 = _f32(D_7857 * D_7857)
                _1166 = _div(1.0e+4, D_7858)
                _1167 = _1166
                sumsss = _f32(sumsss * _1167)
                _pc = 289
                continue
            case 289:  # L.130
                rflsol = _f32(0.0)
                rfls = _f32(0.0)
                rflss = _f32(0.0)
                surdsr = _f32(0.0)
                _1168 = model_zm[0]
                _1169 = card3_h2[0]
                _pc = 290 if _1168 < _1169 else 291
                continue
            case 290:  # <D.18020>
                _pc = 301
                continue
            case 291:  # L.131
                _1170 = srad_teb1[0]
                _pc = 292 if _1170 <= 0.0 else 293
                continue
            case 292:  # <D.18022>
                _pc = 301
                continue
            case 293:  # L.132
                _1171 = sols_angsun[0]
                _pc = 294 if _1171 >= 0.0 else 295
                continue
            case 294:  # <D.18024>
                _1172 = sols_angsun[0]
                _1173 = cnstns_ca[0]
                _1174 = _1172 * _1173
                _1175 = __builtin_cosf(_1174)
                _1176 = card1_salb[0]
                _1177 = _1175 * _1176
                _1178 = cnstns_pi[0]
                rflfac = _f32(_div(_1177, _1178))
                _pc = 295
                continue
            case 295:  # L.133
                _pc = 296 if imlt == 1 else 297
                continue
            case 296:  # <D.18027>
                _1179 = card1_salb[0]
                _1180 = msrd_fdnsrt[0]
                _1181 = _1179 * _1180
                _1182 = __BLNK___tx[8]
                _1183 = _1181 * _1182
                _1184 = cnstns_pi[0]
                surdsr = _f32(_div(_1183, _1184))
                _pc = 297
                continue
            case 297:  # L.134
                _1185 = srad_teb1[0]
                _1186 = rflfac * _1185
                ss_253_1187 = ss[0]
                rflsss = _f32(_1186 * ss_253_1187)
                rflsol = _f32(rflsss + surdsr)
                rfls = _f32(0.0)
                rflss = _f32(0.0)
                v_254_1188 = v[0]
                _pc = 298 if v_254_1188 > 0.0 else 299
                continue
            case 298:  # <D.18030>
                D_7865 = _f32(v[0])
                D_7866 = _f32(D_7865 * D_7865)
                _1189 = _div(1.0e+4, D_7866)
                rfls = _f32(rflsol * _1189)
                _pc = 299
                continue
            case 299:  # L.135
                v_255_1190 = v[0]
                _pc = 300 if v_255_1190 > 0.0 else 301
                continue
            case 300:  # <D.18033>
                D_7868 = _f32(v[0])
                D_7869 = _f32(D_7868 * D_7868)
                _1191 = _div(1.0e+4, D_7869)
                rflss = _f32(rflsss * _1191)
                _pc = 301
                continue
            case 301:  # __label_000510
                _1192 = sumv + sums
                sumt = _f32(rfls + _1192)
                sumssr_256_1193 = sumssr[0]
                _1194 = sumvv + sumssr_256_1193
                sumtt = _f32(rflsol + _1194)
                _1195 = card4_dv[0]
                _1196 = factor * _1195
                _1197 = sumt * _1196
                radsum = _f32(radsum + _1197)
                _pc = 302
            case 302:  # __label_000927
                _pc = 307
                continue
            case 303:  # __label_000600
                _ft_source(_state, v, isourc, iday, anglem, solil)
                soliv = _f32(0.0)
                v_257_1198 = v[0]
                _pc = 304 if v_257_1198 > 0.0 else 305
                continue
            case 304:  # <D.18036>
                D_7873 = _f32(v[0])
                D_7874 = _f32(D_7873 * D_7873)
                solil_258_1199 = solil[0]
                _1200 = solil_258_1199 * 1.0e+4
                soliv = _f32(_div(_1200, D_7874))
                _pc = 305
                continue
            case 305:  # L.138
                _1201 = __BLNK___tx[8]
                tsoliv = _f32(soliv * _1201)
                _1202 = __BLNK___tx[8]
                solil_259_1203 = solil[0]
                tsolil = _f32(_1202 * solil_259_1203)
                _1204 = card4_dv[0]
                _1205 = tsoliv * _1204
                _1206 = factor * _1205
                stsol = _f32(stsol + _1206)
                _1207 = card4_dv[0]
                _1208 = soliv * _1207
                _1209 = factor * _1208
                ssol = _f32(ssol + _1209)
                _pc = 306
            case 306:  # __label_000937
                sumt = _f32(tsoliv)
                radsum = _f32(stsol)
                _pc = 307
            case 307:  # __label_000700
                _1210 = card1_iemsct[0]
                _pc = 308 if _1210 == 0 else 309
                continue
            case 308:  # <D.18039>
                _pc = 317
                continue
            case 309:  # L.139
                _pc = 310 if sumt >= radmax else 311
                continue
            case 310:  # <D.18041>
                vrmax = _f32(v[0])
                _pc = 311
                continue
            case 311:  # L.140
                _pc = 312 if sumt >= radmax else 313
                continue
            case 312:  # <D.18044>
                radmax = _f32(sumt)
                _pc = 313
                continue
            case 313:  # L.141
                _pc = 314 if sumt <= radmin else 315
                continue
            case 314:  # <D.18047>
                vrmin = _f32(v[0])
                _pc = 315
                continue
            case 315:  # L.142
                _pc = 316 if sumt <= radmin else 317
                continue
            case 316:  # <D.18050>
                radmin = _f32(sumt)
                _pc = 317
                continue
            case 317:  # __label_000710
                cntrl_imult[0] = imlt
                D_7882 = _int(offset_6)
                D_7883 = _f32(__BLNK___tx[8])
                D_7884 = _int(_int(ipython))
                D_7886 = _int(stride_5)
                D_7887 = _int(D_7882 + D_7884)
                S_8 = _int(1)
                _pc = 318
            case 318:  # <D.18053>
                _pc = 320 if S_8 > 63 else 319
                continue
            case 319:  # <D.18054>
                _1211 = S_8 * D_7886
                _1212 = D_7887 + _1211
                txpy[_1212] = __BLNK___tx[S_8 - 1]
                S_8 = _int(S_8 + 1)
                _pc = 318
                continue
            case 320:  # L.144
                _1213 = _int(ipython)
                _1214 = _1213 + -1
                v_260_1215 = v[0]
                vpy[_1214] = v_260_1215
                _1216 = _int(ipython)
                _1217 = _1216 + -1
                alampy[_1217] = alam
                _1218 = _int(ipython)
                _1219 = _1218 + -1
                tracepy[_1219] = trace
                _1220 = _int(ipython)
                _1221 = _1220 + -1
                unifpy[_1221] = unif
                _1222 = _int(ipython)
                _1223 = _1222 + -1
                sumapy[_1223] = suma
                _1224 = _int(ipython)
                _1225 = _1224 + -1
                sumvvpy[_1225] = sumvv
                _1226 = offset_2 + stride_1
                _1227 = _int(ipython)
                _1228 = _1226 + _1227
                irradpy[_1228] = tsolil
                _1229 = stride_1 * 2
                _1230 = offset_2 + _1229
                _1231 = _int(ipython)
                _1232 = _1230 + _1231
                solil_261_1233 = solil[0]
                irradpy[_1232] = solil_261_1233
                _1234 = stride_1 * 3
                _1235 = offset_2 + _1234
                _1236 = _int(ipython)
                _1237 = _1235 + _1236
                sumssr_262_1238 = sumssr[0]
                irradpy[_1237] = sumssr_262_1238
                ipython = _int(ipython + 1)
                iv_263_1239 = iv[0]
                _pc = 321 if iv2 > iv_263_1239 else 322
                continue
            case 321:  # <D.18055>
                _pc = 35
                continue
            case 322:  # L.145
                iv_264_1240 = iv[0]
                _1241 = iv_264_1240 - iv1
                _1242 = _f32(_1241)
                _1243 = _div(suma, _1242)
                ab = _f32(1.0e+0 - _1243)
                _1244 = card1_iemsct[0]
                _pc = 323 if _1244 == 0 else 324
                continue
            case 323:  # <D.18057>
                _pc = 324
                continue
            case 324:  # __label_000770
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_source(_state, vv, isourc, iday, angle, ss):
    icll_icall = _state.view(231696, '<i4')
    icll_fphs = _state.view(231700, '<f4')
    icll_falb = _state.view(231704, '<f4')
    icll_forbit = _state.view(231708, '<f4')
    alb = _state.view(172192, '<f4')
    nday = _state.view(172320, '<i4')
    phs = _state.view(172096, '<f4')
    rat = _state.view(172384, '<f4')
    i = 0
    i1 = 0
    ip = 0
    v = _ZERO32
    D_7953 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = vv[0]
                v = _f32(_div(1.0e+4, _1))
                _2 = vv[0]
                _pc = 1 if _2 <= 0.0 else 2
                continue
            case 1:  # <D.18062>
                v = _f32(9.9999996802856924650656260769173209088e+37)
                _pc = 2
                continue
            case 2:  # L.148
                _3 = isourc[0]
                _pc = 3 if _3 != 1 else 4
                continue
            case 3:  # <D.18065>
                _pc = 18
                continue
            case 4:  # L.149
                _4 = icll_icall[0]
                _pc = 5 if _4 == 1 else 6
                continue
            case 5:  # <D.18067>
                _pc = 12
                continue
            case 6:  # L.150
                icll_fphs[0] = 0.0
                _5 = angle[0]
                _pc = 7 if _5 > 1.6e+2 else 8
                continue
            case 7:  # <D.18069>
                _pc = 12
                continue
            case 8:  # L.151
                _6 = angle[0]
                _7 = _div(_6, 1.0e+1)
                ip = _int(_int(_7))
                _8 = ip * 10
                _9 = _f32(_8)
                _10 = angle[0]
                _pc = 9 if _9 == _10 else 10
                continue
            case 9:  # <D.18071>
                _pc = 11
                continue
            case 10:  # L.152
                _11 = ip + 1
                _12 = _int(_11)
                _13 = _12 + -1
                _14 = phs[_13]
                _15 = angle[0]
                _16 = _f32(ip)
                _17 = _16 * 1.0e+1
                _18 = _15 - _17
                _19 = _18
                _20 = ip + 2
                _21 = _int(_20)
                _22 = _21 + -1
                _23 = phs[_22]
                _24 = ip + 1
                _25 = _int(_24)
                _26 = _25 + -1
                _27 = phs[_26]
                _28 = _23 - _27
                _29 = _28
                _30 = _19 * _29
                _31 = _div(_30, 1.0e+1)
                _32 = _14 + _31
                icll_fphs[0] = _32
                _pc = 12
                continue
            case 11:  # __label_000010
                _33 = ip + 1
                _34 = _int(_33)
                _35 = _34 + -1
                _36 = phs[_35]
                icll_fphs[0] = _36
                _pc = 12
            case 12:  # __label_000020
                icll_falb[0] = 4.000000059604644775390625e-1
                _pc = 13 if v >= 5.0e+0 else 14
                continue
            case 13:  # <D.18073>
                _pc = 18
                continue
            case 14:  # L.153
                _pc = 15 if v > 2.7999999523162841796875e+0 else 16
                continue
            case 15:  # <D.18075>
                _pc = 17
                continue
            case 16:  # L.154
                _37 = v * 1.0e+1
                i1 = _int(_int(_37))
                _38 = _int(i1)
                _39 = _38 + -1
                _40 = alb[_39]
                _41 = i1 + 1
                _42 = _int(_41)
                _43 = _42 + -1
                _44 = alb[_43]
                _45 = _int(i1)
                _46 = _45 + -1
                _47 = alb[_46]
                _48 = _44 - _47
                _49 = _48
                _50 = _f32(i1)
                _51 = _50 * 1.00000001490116119384765625e-1
                _52 = v - _51
                _53 = _52
                _54 = _49 * _53
                _55 = _54 * 1.0e+1
                _56 = _40 + _55
                icll_falb[0] = _56
                _pc = 18
                continue
            case 17:  # __label_000030
                _57 = alb[27]
                _58 = alb[28]
                _59 = alb[27]
                _60 = _58 - _59
                _61 = _60
                _62 = v - 2.7999999523162841796875e+0
                _63 = _62
                _64 = _61 * _63
                _65 = _div(_64, 2.2000000476837158203125e+0)
                _66 = _57 + _65
                icll_falb[0] = _66
                _pc = 18
            case 18:  # __label_000050
                _67 = icll_icall[0]
                _pc = 19 if _67 == 1 else 20
                continue
            case 19:  # <D.18077>
                _pc = 32
                continue
            case 20:  # L.155
                icll_forbit[0] = 0.0
                _68 = iday[0]
                _69 = _68 > 0
                _70 = iday[0]
                _71 = _70 <= 366
                _72 = _69 & _71
                _pc = 21 if _72 != 0 else 22
                continue
            case 21:  # <D.18079>
                _pc = 23
                continue
            case 22:  # L.156
                icll_forbit[0] = 1.0e+0
                _pc = 32
                continue
            case 23:  # __label_000055
                i = _int(1)
                _pc = 24
            case 24:  # <D.18081>
                D_7953 = _int(i > 13)
                _pc = 30 if D_7953 != 0 else 25
                continue
            case 25:  # <D.18082>
                _73 = _int(i)
                _74 = _73 + -1
                _75 = nday[_74]
                _76 = iday[0]
                _pc = 26 if _75 == _76 else 27
                continue
            case 26:  # <D.18083>
                _pc = 31
                continue
            case 27:  # L.159
                _77 = _int(i)
                _78 = _77 + -1
                _79 = nday[_78]
                _80 = iday[0]
                _pc = 28 if _79 > _80 else 29
                continue
            case 28:  # <D.18085>
                _pc = 30
                continue
            case 29:  # L.157
                i = _int(i + 1)
                _pc = 24
                continue
            case 30:  # __label_000070
                _81 = i + -1
                _82 = _int(_81)
                _83 = _82 + -1
                _84 = rat[_83]
                _85 = iday[0]
                _86 = i + -1
                _87 = _int(_86)
                _88 = _87 + -1
                _89 = nday[_88]
                _90 = _85 - _89
                _91 = _f32(_90)
                _92 = _int(i)
                _93 = _92 + -1
                _94 = rat[_93]
                _95 = i + -1
                _96 = _int(_95)
                _97 = _96 + -1
                _98 = rat[_97]
                _99 = _94 - _98
                _100 = _99
                _101 = _91 * _100
                _102 = _int(i)
                _103 = _102 + -1
                _104 = nday[_103]
                _105 = i + -1
                _106 = _int(_105)
                _107 = _106 + -1
                _108 = nday[_107]
                _109 = _104 - _108
                _110 = _f32(_109)
                _111 = _div(_101, _110)
                _112 = _84 + _111
                icll_forbit[0] = _112
                _pc = 32
                continue
            case 31:  # __label_000080
                _113 = _int(i)
                _114 = _113 + -1
                _115 = rat[_114]
                icll_forbit[0] = _115
                _pc = 32
            case 32:  # __label_000090
                icll_icall[0] = 1
                _116 = _ft_sun(_state, vv)
                _117 = icll_forbit[0]
                _118 = _116 * _117
                ss[0] = _118
                _119 = isourc[0]
                _pc = 33 if _119 == 1 else 34
                continue
            case 33:  # <D.18087>
                _120 = ss[0]
                _121 = icll_fphs[0]
                _122 = _120 * _121
                _123 = icll_falb[0]
                _124 = _122 * _123
                _125 = _124 * 2.04472001996691687963902950286865234375e-7
                ss[0] = _125
                _pc = 34
                continue
            case 34:  # L.161
                _126 = ss[0]
                _127 = _126 * 9.99999974737875163555145263671875e-5
                ss[0] = _127
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_bbfn(_state, t, v):
    cnstns_bigexp = _state.view(246180, '<f4')
    D_18092 = _ZERO32
    x = _ZERO32
    __result_bbfn = _ZERO32
    D_7979 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                __result_bbfn = _f32(0.0)
                _1 = v[0]
                _pc = 1 if _1 <= 0.0 else 2
                continue
            case 1:  # <D.18090>
                D_18092 = _f32(__result_bbfn)
                return D_18092
            case 2:  # L.162
                _2 = v[0]
                _3 = _2 * 1.43878996372222900390625e+0
                _4 = t[0]
                x = _f32(_div(_3, _4))
                _5 = cnstns_bigexp[0]
                _pc = 3 if x > _5 else 4
                continue
            case 3:  # <D.18093>
                D_18092 = _f32(__result_bbfn)
                return D_18092
            case 4:  # L.163
                D_7979 = _f32(v[0])
                _6 = __builtin_powif(D_7979, 5)
                _7 = _6 * 1.19095598475923004997550913586223941820207983255386352539e-16
                _8 = __builtin_expf(x)
                _9 = _8 - 1.0e+0
                _10 = _9
                _11 = _div(_7, _10)
                __result_bbfn = _f32(_11)
                D_18092 = _f32(__result_bbfn)
                return D_18092
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_betabs(_state, u, g):
    a9 = _state.view(172448, '<f4')
    u8 = _state.view(172672, '<f4')
    D_18125 = _ZERO32
    iq = 0
    iqp1 = 0
    j = 0
    jm1 = 0
    y3 = _ZERO32
    y5 = _ZERO32
    y6 = _ZERO32
    y7 = _ZERO32
    y8 = _ZERO32
    y9 = _ZERO32
    __result_betabs = _ZERO32
    D_8006 = 0
    D_8007 = _ZERO32
    D_8008 = _ZERO32
    D_8009 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                iq = _int(0)
                _1 = u[0]
                _pc = 1 if _1 < 1.00000001490116119384765625e-1 else 2
                continue
            case 1:  # <D.18097>
                iq = _int(1)
                _pc = 2
                continue
            case 2:  # L.164
                _2 = u[0]
                _3 = _2 < 2.0000000298023223876953125e-1
                _4 = u[0]
                _5 = _4 >= 1.00000001490116119384765625e-1
                _6 = _3 & _5
                _pc = 3 if _6 != 0 else 4
                continue
            case 3:  # <D.18100>
                iq = _int(2)
                _pc = 4
                continue
            case 4:  # L.165
                _7 = u[0]
                _8 = _7 < 3.00000011920928955078125e-1
                _9 = u[0]
                _10 = _9 >= 2.0000000298023223876953125e-1
                _11 = _8 & _10
                _pc = 5 if _11 != 0 else 6
                continue
            case 5:  # <D.18103>
                iq = _int(3)
                _pc = 6
                continue
            case 6:  # L.166
                _12 = u[0]
                _13 = _12 < 4.000000059604644775390625e-1
                _14 = u[0]
                _15 = _14 >= 3.00000011920928955078125e-1
                _16 = _13 & _15
                _pc = 7 if _16 != 0 else 8
                continue
            case 7:  # <D.18106>
                iq = _int(4)
                _pc = 8
                continue
            case 8:  # L.167
                _17 = u[0]
                _18 = _17 < 5.0e-1
                _19 = u[0]
                _20 = _19 >= 4.000000059604644775390625e-1
                _21 = _18 & _20
                _pc = 9 if _21 != 0 else 10
                continue
            case 9:  # <D.18109>
                iq = _int(5)
                _pc = 10
                continue
            case 10:  # L.168
                _22 = u[0]
                _23 = _22 < 6.0000002384185791015625e-1
                _24 = u[0]
                _25 = _24 >= 5.0e-1
                _26 = _23 & _25
                _pc = 11 if _26 != 0 else 12
                continue
            case 11:  # <D.18112>
                iq = _int(6)
                _pc = 12
                continue
            case 12:  # L.169
                _27 = u[0]
                _28 = _27 < 8.00000011920928955078125e-1
                _29 = u[0]
                _30 = _29 >= 6.0000002384185791015625e-1
                _31 = _28 & _30
                _pc = 13 if _31 != 0 else 14
                continue
            case 13:  # <D.18115>
                iq = _int(7)
                _pc = 14
                continue
            case 14:  # L.170
                _32 = u[0]
                _33 = _32 <= 1.0e+0
                _34 = u[0]
                _35 = _34 >= 8.00000011920928955078125e-1
                _36 = _33 & _35
                _pc = 15 if _36 != 0 else 16
                continue
            case 15:  # <D.18118>
                iq = _int(8)
                _pc = 16
                continue
            case 16:  # L.171
                _pc = 17 if iq == 0 else 18
                continue
            case 17:  # __label_000105
                _gfortran_stop_string(b" ERROR ***", 10, 0)
                _pc = 18
            case 18:  # L.172
                y5 = _f32(0.0)
                y6 = _f32(0.0)
                y7 = _f32(0.0)
                iqp1 = _int(iq + 1)
                j = _int(1)
                _pc = 19
            case 19:  # <D.18123>
                D_8006 = _int(j > 5)
                _pc = 22 if D_8006 != 0 else 20
                continue
            case 20:  # <D.18124>
                jm1 = _int(j + -1)
                D_8007 = _f32(g[0])
                _37 = _int(j)
                _38 = _37 * 10
                _39 = _int(iq)
                _40 = _38 + _39
                _41 = _40 + -11
                _42 = a9[_41]
                _43 = __builtin_powif(D_8007, jm1)
                y9 = _f32(_42 * _43)
                D_8008 = _f32(g[0])
                _44 = _int(j)
                _45 = _44 * 10
                _46 = _int(iqp1)
                _47 = _45 + _46
                _48 = _47 + -11
                _49 = a9[_48]
                _50 = __builtin_powif(D_8008, jm1)
                y8 = _f32(_49 * _50)
                D_8009 = _f32(g[0])
                _51 = _int(j)
                _52 = _51 * 10
                _53 = _52 + -1
                _54 = a9[_53]
                _55 = __builtin_powif(D_8009, jm1)
                y3 = _f32(_54 * _55)
                y7 = _f32(y7 + y9)
                y6 = _f32(y6 + y8)
                y5 = _f32(y5 + y3)
                _pc = 21
            case 21:  # L.173
                j = _int(j + 1)
                _pc = 19
                continue
            case 22:  # L.174
                _56 = y6 - y7
                _57 = _56
                _58 = u[0]
                _59 = _int(iq)
                _60 = _59 + -1
                _61 = u8[_60]
                _62 = _58 - _61
                _63 = _62
                _64 = _57 * _63
                _65 = _int(iqp1)
                _66 = _65 + -1
                _67 = u8[_66]
                _68 = _int(iq)
                _69 = _68 + -1
                _70 = u8[_69]
                _71 = _67 - _70
                _72 = _71
                _73 = _div(_64, _72)
                _74 = y7 + _73
                __result_betabs = _f32(_74)
                D_18125 = _f32(__result_betabs)
                return D_18125
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_msrad(_state, iv, v, isourc, iday, anglem, ss, dmf, dmfs, umf, umfs):
    card1_iemsct = _state.view(209576, '<i4')
    card2_ihaze = _state.view(231744, '<i4')
    cntrl_ikmax = _state.view(245608, '<i4')
    cntrl_iklo = _state.view(245620, '<i4')
    msrd_tle = _state.view(209760, '<f4')
    msrd_cosbar = _state.view(209896, '<f4')
    msrd_omega0 = _state.view(210032, '<f4')
    msrd_upf = _state.view(210168, '<f4')
    msrd_dnf = _state.view(211528, '<f4')
    msrd_taer = _state.view(212888, '<f4')
    msrd_dtx7 = _state.view(213088, '<f4')
    msrd_daers = _state.view(213224, '<f4')
    msrd_asyik = _state.view(213360, '<f4')
    msrd_asydm = _state.view(213496, '<f4')
    msrd_strn = _state.view(213632, '<f4')
    msrd_dmols = _state.view(213772, '<f4')
    msrd_dstrn = _state.view(213908, '<f4')
    msrd_fdnsrt = _state.view(214052, '<f4')
    msrd_fdntrt = _state.view(214064, '<f4')
    sols_cszen = _state.view(208260, '<f4')
    tran_tmols = _state.view(188868, '<f4')
    tran_taers = _state.view(189004, '<f4')
    tran_tcont = _state.view(189140, '<f4')
    tran_dcont = _state.view(189276, '<f4')
    denom = _ZERO32
    ik = 0
    ikm = 0
    ikmik = 0
    s0 = _zeros(1, '<f4')
    D_8260 = 0
    D_8261 = 0
    D_8264 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = cntrl_ikmax[0]
                _2 = _1 + 1
                cntrl_ikmax[0] = _2
                _3 = cntrl_ikmax[0]
                ikm = _int(_3 + -1)
                D_8260 = _int(cntrl_iklo[0])
                D_8261 = _int(ikm + -1)
                ik = _int(D_8260)
                _pc = 1
            case 1:  # <D.18128>
                D_8264 = _int(ik > D_8261)
                _pc = 18 if D_8264 != 0 else 2
                continue
            case 2:  # <D.18129>
                _4 = cntrl_ikmax[0]
                _5 = _4 - ik
                _6 = _int(_5)
                _7 = ik + -1
                _8 = _int(_7)
                _9 = msrd_dstrn[_6]
                msrd_strn[_8] = _9
                _10 = card2_ihaze[0]
                _pc = 3 if _10 > 0 else 7
                continue
            case 3:  # <D.18130>
                _11 = _int(ik)
                _12 = _11 + -1
                denom = _f32(msrd_asydm[_12])
                _pc = 4 if denom <= 0.0 else 5
                continue
            case 4:  # <D.18132>
                _13 = ikm - ik
                _14 = _int(_13)
                _15 = _14 + -1
                msrd_cosbar[_15] = 0.0
                _pc = 6
                continue
            case 5:  # <D.18133>
                _16 = _int(ik)
                _17 = _16 + -1
                _18 = msrd_asyik[_17]
                _19 = ikm - ik
                _20 = _int(_19)
                _21 = _20 + -1
                _22 = _div(_18, denom)
                msrd_cosbar[_21] = _22
                _pc = 6
            case 6:  # L.178
                _pc = 7
                continue
            case 7:  # L.177
                _23 = ik + 1
                _24 = _int(_23)
                _25 = _24 + -1
                _26 = msrd_dtx7[_25]
                _27 = _int(ik)
                _28 = _27 + -1
                _29 = msrd_dtx7[_28]
                _30 = ikm - ik
                _31 = _int(_30)
                _32 = _31 + -1
                _33 = _26 - _29
                msrd_taer[_32] = _33
                _34 = ik + 1
                _35 = _int(_34)
                _36 = _35 + -1
                _37 = msrd_daers[_36]
                _38 = _int(ik)
                _39 = _38 + -1
                _40 = msrd_daers[_39]
                _41 = ikm - ik
                _42 = _int(_41)
                _43 = _42 + -1
                _44 = _37 - _40
                tran_taers[_43] = _44
                _45 = ik + 1
                _46 = _int(_45)
                _47 = _46 + -1
                _48 = msrd_dmols[_47]
                _49 = _int(ik)
                _50 = _49 + -1
                _51 = msrd_dmols[_50]
                _52 = ikm - ik
                _53 = _int(_52)
                _54 = _53 + -1
                _55 = _48 - _51
                tran_tmols[_54] = _55
                ikmik = _int(ikm - ik)
                _56 = _int(ikmik)
                _57 = _56 + -1
                _58 = msrd_taer[_57]
                _pc = 8 if _58 < 0.0 else 9
                continue
            case 8:  # <D.18136>
                _59 = _int(ikmik)
                _60 = _59 + -1
                msrd_taer[_60] = 0.0
                _pc = 9
                continue
            case 9:  # L.179
                _61 = _int(ikmik)
                _62 = _61 + -1
                _63 = tran_taers[_62]
                _pc = 10 if _63 < 0.0 else 11
                continue
            case 10:  # <D.18139>
                _64 = _int(ikmik)
                _65 = _64 + -1
                tran_taers[_65] = 0.0
                _pc = 11
                continue
            case 11:  # L.180
                _66 = _int(ikmik)
                _67 = _66 + -1
                _68 = tran_tmols[_67]
                _pc = 12 if _68 < 0.0 else 13
                continue
            case 12:  # <D.18142>
                _69 = _int(ikmik)
                _70 = _69 + -1
                tran_tmols[_70] = 0.0
                _pc = 13
                continue
            case 13:  # L.181
                _71 = ikm - ik
                _72 = _int(_71)
                _73 = _72 + -1
                _74 = tran_taers[_73]
                _pc = 14 if _74 <= 0.0 else 15
                continue
            case 14:  # <D.18145>
                _75 = ikm - ik
                _76 = _int(_75)
                _77 = _76 + -1
                msrd_cosbar[_77] = 0.0
                _pc = 16
                continue
            case 15:  # <D.18146>
                _78 = ikm - ik
                _79 = _int(_78)
                _80 = _79 + -1
                _81 = msrd_cosbar[_80]
                _82 = ikm - ik
                _83 = _int(_82)
                _84 = _83 + -1
                _85 = tran_taers[_84]
                _86 = _81 * _85
                _87 = ikm - ik
                _88 = _int(_87)
                _89 = _88 + -1
                _90 = tran_taers[_89]
                _91 = ikm - ik
                _92 = _int(_91)
                _93 = _92 + -1
                _94 = tran_tmols[_93]
                _95 = _90 + _94
                _96 = _95
                _97 = ikm - ik
                _98 = _int(_97)
                _99 = _98 + -1
                _100 = _div(_86, _96)
                msrd_cosbar[_99] = _100
                _pc = 16
            case 16:  # __label_000222
                _101 = ik + 1
                _102 = _int(_101)
                _103 = _102 + -1
                _104 = tran_dcont[_103]
                _105 = _int(ik)
                _106 = _105 + -1
                _107 = tran_dcont[_106]
                _108 = ikm - ik
                _109 = _int(_108)
                _110 = _109 + -1
                _111 = _104 - _107
                tran_tcont[_110] = _111
                _pc = 17
            case 17:  # L.175
                ik = _int(ik + 1)
                _pc = 1
                continue
            case 18:  # L.176
                _112 = card2_ihaze[0]
                _pc = 19 if _112 > 0 else 23
                continue
            case 19:  # <D.18148>
                denom = _f32(msrd_asydm[0])
                _pc = 20 if denom <= 0.0 else 21
                continue
            case 20:  # <D.18150>
                _113 = _int(ikm)
                _114 = _113 + -1
                msrd_cosbar[_114] = 0.0
                _pc = 22
                continue
            case 21:  # <D.18151>
                _115 = _int(ik)
                _116 = _115 + -1
                _117 = msrd_asyik[_116]
                _118 = _int(ikm)
                _119 = _118 + -1
                _120 = _div(_117, denom)
                msrd_cosbar[_119] = _120
                _pc = 22
            case 22:  # L.184
                _pc = 23
                continue
            case 23:  # L.183
                _121 = cntrl_ikmax[0]
                _122 = _121 - ikm
                _123 = _int(_122)
                _124 = ikm + -1
                _125 = _int(_124)
                _126 = msrd_dstrn[_123]
                msrd_strn[_125] = _126
                _127 = _int(ikm)
                _128 = msrd_dstrn[0]
                msrd_strn[_127] = _128
                _129 = _int(ikm)
                _130 = _129 + -1
                _131 = msrd_dtx7[0]
                msrd_taer[_130] = _131
                _132 = _int(ikm)
                _133 = _132 + -1
                _134 = msrd_daers[0]
                tran_taers[_133] = _134
                _135 = _int(ikm)
                _136 = _135 + -1
                _137 = msrd_dmols[0]
                tran_tmols[_136] = _137
                _138 = _int(ikm)
                _139 = _138 + -1
                _140 = tran_taers[_139]
                _pc = 24 if _140 <= 0.0 else 25
                continue
            case 24:  # <D.18154>
                _141 = _int(ikm)
                _142 = _141 + -1
                msrd_cosbar[_142] = 0.0
                _pc = 26
                continue
            case 25:  # <D.18155>
                _143 = _int(ikm)
                _144 = _143 + -1
                _145 = msrd_cosbar[_144]
                _146 = _int(ikm)
                _147 = _146 + -1
                _148 = tran_taers[_147]
                _149 = _145 * _148
                _150 = _int(ikm)
                _151 = _150 + -1
                _152 = tran_taers[_151]
                _153 = _int(ikm)
                _154 = _153 + -1
                _155 = tran_tmols[_154]
                _156 = _152 + _155
                _157 = _156
                _158 = _int(ikm)
                _159 = _158 + -1
                _160 = _div(_149, _157)
                msrd_cosbar[_159] = _160
                _pc = 26
            case 26:  # L.185
                _161 = _int(ikm)
                _162 = _161 + -1
                _163 = tran_dcont[0]
                tran_tcont[_162] = _163
                s0[0] = 0.0
                _164 = card1_iemsct[0]
                _pc = 27 if _164 == 2 else 28
                continue
            case 27:  # <D.18157>
                _ft_source(_state, v, isourc, iday, anglem, s0)
                _pc = 28
                continue
            case 28:  # L.186
                _ft_flxadd(_state, msrd_tle, msrd_cosbar, msrd_taer, msrd_omega0, msrd_upf, msrd_dnf, iv, cntrl_ikmax, sols_cszen, s0, msrd_strn, msrd_fdnsrt, msrd_fdntrt, dmf, dmfs, umf, umfs)
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_flxadd(_state, tle, cosbar, taer, omega0, upf, dnf, iwavn, ikmax, cszen, s0, strn, fdnsrf, fdntrf, dmf, dmfs, umf, umfs):
    __BLNK___w = _state.view(266176, '<f4')
    aabbcc_aa = _state.view(245824, '<f4')
    aabbcc_bb = _state.view(245868, '<f4')
    aabbcc_cc = _state.view(245912, '<f4')
    aabbcc_ibnd = _state.view(245956, '<i4')
    aabbcc_cps = _state.view(246044, '<f4')
    card1_iemsct = _state.view(209576, '<i4')
    card1_salb = _state.view(209604, '<f4')
    cnstns_pi = _state.view(246160, '<f4')
    cnstns_bignum = _state.view(246176, '<f4')
    cnstns_bigexp = _state.view(246180, '<f4')
    cntrl_ml = _state.view(245616, '<i4')
    dirst_sun = _state.view(246208, '<f4')
    dirst_umb = _state.view(246212, '<f4')
    dirst_dmb = _state.view(246348, '<f4')
    dirst_umbs = _state.view(246484, '<f4')
    dirst_dmbs = _state.view(246620, '<f4')
    model_zm = _state.view(231904, '<f4')
    model_densty = _state.view(232448, '<f4')
    path_pl = _state.view(242144, '<f4')
    tran_btop = _state.view(188396, '<f4')
    tran_bmid = _state.view(188596, '<f4')
    tran_tmd = _state.view(188732, '<f4')
    tran_tmols = _state.view(188868, '<f4')
    tran_taers = _state.view(189004, '<f4')
    tran_tcont = _state.view(189140, '<f4')
    dnfs = _state.view(184192, '<f4')
    edns = _state.view(183328, '<f4')
    eups = _state.view(183168, '<f4')
    fac = _state.view(172712, '<f4')
    refs = _state.view(183488, '<f4')
    rupc = _state.view(183808, '<f4')
    rupcs = _state.view(184032, '<f4')
    tdfs = _state.view(183648, '<f4')
    upfs = _state.view(186240, '<f4')
    aer1 = _ZERO64
    aer2 = _ZERO64
    aera = _ZERO64
    aerc = _ZERO64
    aercx = _ZERO64
    aeru = _ZERO64
    aerv = _ZERO64
    asnew = _ZERO32
    asxp = _ZERO32
    b0 = _ZERO32
    bets = _zeros(34, '<f4')
    bsnew = _ZERO32
    cp1s = _zeros(11, '<f4')
    cs = _ZERO32
    deno = _ZERO64
    denom = _ZERO32
    denos = _ZERO32
    dnm1 = _ZERO64
    dnmo = _ZERO64
    dpc = _ZERO32
    dpj = _zeros(102, '<f4')
    dpwj = _zeros(33, '<f4')
    edn = _zeros(50, '<f4')
    edncn = _ZERO32
    edncns = _ZERO32
    ekt = _ZERO32
    ekt2 = _ZERO32
    ektl = _ZERO32
    etmu = _ZERO32
    etmul = _ZERO32
    eup = _zeros(50, '<f4')
    eupc = _zeros(50, '<f4')
    eupcn = _ZERO32
    eupcns = _ZERO32
    eupcs = _zeros(34, '<f4')
    ex1 = _ZERO64
    ex2 = _ZERO64
    fc = _ZERO32
    fupsrf = _ZERO32
    fuptrf = _ZERO32
    g = _ZERO32
    gkwj = _zeros(33, '<f4')
    gm1 = _ZERO32
    gm2 = _ZERO32
    gmmsk = _ZERO32
    gmpsk = _ZERO32
    ib = 0
    iw = 0
    k = 0
    m = 0
    mf = 0
    mol = 0
    n = 0
    ng = 0
    ng1 = 0
    nlayrs = 0
    ome0 = _ZERO32
    omegak = _zeros(34, '<f4')
    pefdn = _ZERO32
    pefdns = _ZERO32
    pefup = _ZERO32
    pefups = _ZERO32
    q = _ZERO32
    rdncn = _ZERO32
    rdncns = _ZERO32
    ref = _zeros(50, '<f4')
    rupcn = _ZERO32
    rupcns = _ZERO32
    sk = _ZERO32
    smdpj = _ZERO32
    smu = _ZERO32
    taum = _zeros(150, '<f4')
    taut = _zeros(34, '<f4')
    tdf = _zeros(50, '<f4')
    twgp = _zeros(102, '<f4')
    v = _zeros(1, '<f4')
    wavn = _ZERO32
    x = _ZERO32
    xcszen = _ZERO32
    xp = _ZERO32
    ys = _ZERO32
    D_8622 = 0
    D_8626 = 0
    D_8629 = 0
    D_8637 = 0
    D_8640 = 0
    D_8647 = 0
    D_8648 = 0
    D_8651 = 0
    D_8654 = 0
    D_8659 = 0
    D_8662 = 0
    D_8665 = 0
    D_8669 = 0
    D_8671 = 0
    D_8674 = 0
    D_8687 = _ZERO32
    D_8688 = _ZERO32
    D_8689 = _ZERO32
    D_8690 = _ZERO32
    D_8691 = _ZERO32
    D_8700 = 0
    D_8703 = 0
    D_8709 = 0
    D_8712 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # __label_000310
                dpc = _f32(3.333333432674407958984375e-1)
                _1 = iwavn[0]
                wavn = _f32(_f32(_1))
                v[0] = wavn
                _pc = 1
            case 1:  # __label_001900
                _2 = cntrl_ml[0]
                nlayrs = _int(_2 + -1)
                ng = _int(nlayrs + 1)
                ng1 = _int(ng + 1)
                m = _int(1)
                _pc = 2
            case 2:  # <D.18160>
                D_8622 = _int(m > 11)
                _pc = 5 if D_8622 != 0 else 3
                continue
            case 3:  # __label_000001
                _3 = _int(m)
                _4 = _3 + -1
                _5 = aabbcc_cps[_4]
                _6 = _int(m)
                _7 = _6 + -1
                _8 = __builtin_powf(1.0e+1, _5)
                cp1s[_7] = _8
                _pc = 4
            case 4:  # L.187
                m = _int(m + 1)
                _pc = 2
                continue
            case 5:  # L.188
                mol = _int(1)
                _pc = 6
            case 6:  # <D.18162>
                D_8626 = _int(mol > 11)
                _pc = 21 if D_8626 != 0 else 7
                continue
            case 7:  # <D.18163>
                k = _int(1)
                _pc = 8
            case 8:  # <D.18164>
                D_8629 = _int(k > 3)
                _pc = 20 if D_8629 != 0 else 9
                continue
            case 9:  # <D.18165>
                _9 = _int(mol)
                _10 = _9 + -1
                iw = _int(aabbcc_ibnd[_10])
                _11 = _int(mol)
                _12 = _11 * 3
                _13 = _int(k)
                _14 = _12 + _13
                _15 = _14 + -4
                gkwj[_15] = 0.0
                _16 = _int(mol)
                _17 = _16 * 3
                _18 = _int(k)
                _19 = _17 + _18
                _20 = _19 + -4
                dpwj[_20] = 0.0
                _pc = 10 if iw <= 0 else 11
                continue
            case 10:  # <D.18166>
                _pc = 19
                continue
            case 11:  # L.193
                _21 = _int(k)
                _22 = _21 + -1
                _23 = fac[_22]
                _24 = _int(mol)
                _25 = _24 + -1
                _26 = aabbcc_cc[_25]
                _27 = _int(mol)
                _28 = _27 * 3
                _29 = _int(k)
                _30 = _28 + _29
                _31 = _30 + -4
                _32 = _23 * _26
                gkwj[_31] = _32
                _pc = 12 if k == 1 else 13
                continue
            case 12:  # <D.18168>
                _33 = _int(mol)
                _34 = _33 + -1
                _35 = _int(mol)
                _36 = _35 * 3
                _37 = _int(k)
                _38 = _36 + _37
                _39 = _38 + -4
                _40 = aabbcc_aa[_34]
                dpwj[_39] = _40
                _pc = 13
                continue
            case 13:  # L.194
                _pc = 14 if k == 2 else 15
                continue
            case 14:  # <D.18171>
                _41 = _int(mol)
                _42 = _41 + -1
                _43 = _int(mol)
                _44 = _43 * 3
                _45 = _int(k)
                _46 = _44 + _45
                _47 = _46 + -4
                _48 = aabbcc_bb[_42]
                dpwj[_47] = _48
                _pc = 15
                continue
            case 15:  # L.195
                _pc = 16 if k == 3 else 17
                continue
            case 16:  # <D.18174>
                _49 = _int(mol)
                _50 = _49 + -1
                _51 = aabbcc_aa[_50]
                _52 = 1.0e+0 - _51
                _53 = _int(mol)
                _54 = _53 + -1
                _55 = aabbcc_bb[_54]
                _56 = _int(mol)
                _57 = _56 * 3
                _58 = _int(k)
                _59 = _57 + _58
                _60 = _59 + -4
                _61 = _52 - _55
                dpwj[_60] = _61
                _pc = 17
                continue
            case 17:  # L.196
                _pc = 18 if k > 1 else 19
                continue
            case 18:  # <D.18177>
                _pc = 19
                continue
            case 19:  # L.191
                k = _int(k + 1)
                _pc = 8
                continue
            case 20:  # L.189
                mol = _int(mol + 1)
                _pc = 6
                continue
            case 21:  # L.190
                _62 = _int(ng)
                _63 = _62 + -1
                _64 = _int(ng1)
                _65 = _64 + -1
                _66 = tle[_63]
                tle[_65] = _66
                D_8637 = _int(ng)
                n = _int(1)
                _pc = 22
            case 22:  # <D.18179>
                D_8640 = _int(n > D_8637)
                _pc = 30 if D_8640 != 0 else 23
                continue
            case 23:  # <D.18180>
                _67 = _int(n)
                _68 = _67 + -1
                _69 = tle[_68:]
                _70 = _ft_bbfn(_state, _69, v)
                _71 = cnstns_pi[0]
                _72 = _int(n)
                _73 = _72 + -1
                _74 = _70 * _71
                tran_btop[_73] = _74
                _75 = _int(n)
                _76 = _75 + -1
                _77 = tran_tmd[_76:]
                _78 = _int(n)
                _79 = _78 + -1
                _80 = _ft_bbfn(_state, _77, v)
                tran_bmid[_79] = _80
                _pc = 24 if n < ng else 29
                continue
            case 24:  # <D.18181>
                _81 = _int(n)
                _82 = _81 + -1
                _83 = cosbar[_82]
                _pc = 25 if _83 == 0.0 else 26
                continue
            case 25:  # <D.18183>
                _84 = _int(n)
                _85 = _84 + -1
                bets[_85] = 5.0e-1
                _pc = 28
                continue
            case 26:  # <D.18184>
                _86 = card1_iemsct[0]
                _87 = _86 == 2
                _88 = card1_iemsct[0]
                _89 = _88 == 3
                _90 = _87 | _89
                _pc = 27 if _90 != 0 else 28
                continue
            case 27:  # <D.18186>
                _91 = _int(n)
                _92 = _91 + -1
                _93 = cosbar[_92:]
                _94 = _int(n)
                _95 = _94 + -1
                _96 = cszen[_95:]
                _97 = _int(n)
                _98 = _97 + -1
                _99 = _ft_betabs(_state, _96, _93)
                bets[_98] = _99
                _pc = 28
                continue
            case 28:  # L.201
                _pc = 29
                continue
            case 29:  # L.198
                n = _int(n + 1)
                _pc = 22
                continue
            case 30:  # L.199
                k = _int(1)
                _pc = 31
            case 31:  # <D.18190>
                D_8647 = _int(k > 3)
                _pc = 44 if D_8647 != 0 else 32
                continue
            case 32:  # <D.18191>
                D_8648 = _int(nlayrs)
                n = _int(1)
                _pc = 33
            case 33:  # <D.18192>
                D_8651 = _int(n > D_8648)
                _pc = 43 if D_8651 != 0 else 34
                continue
            case 34:  # <D.18193>
                _100 = _int(n)
                _101 = _100 * 3
                _102 = _int(k)
                _103 = _101 + _102
                _104 = _103 + -4
                taum[_104] = 0.0
                _105 = _int(n)
                _106 = _105 * 3
                _107 = _int(k)
                _108 = _106 + _107
                _109 = _108 + -4
                twgp[_109] = 0.0
                mol = _int(1)
                _pc = 35
            case 35:  # <D.18194>
                D_8654 = _int(mol > 11)
                _pc = 40 if D_8654 != 0 else 36
                continue
            case 36:  # <D.18195>
                _110 = _int(mol)
                _111 = _110 + -1
                ib = _int(aabbcc_ibnd[_111])
                _pc = 37 if ib < 0 else 38
                continue
            case 37:  # <D.18196>
                _pc = 39
                continue
            case 38:  # L.209
                _112 = ikmax[0]
                _113 = _112 - n
                _114 = _int(_113)
                _115 = _114 * 63
                _116 = _int(ib)
                _117 = _115 + _116
                _118 = _117 + -64
                _119 = model_densty[_118]
                _120 = ikmax[0]
                _121 = _120 - n
                _122 = _int(_121)
                _123 = _122 + -1
                _124 = path_pl[_123]
                _125 = _119 * _124
                _126 = _int(mol)
                _127 = _126 * 3
                _128 = _int(k)
                _129 = _127 + _128
                _130 = _129 + -4
                _131 = gkwj[_130]
                _132 = _int(ib)
                _133 = _132 + -1
                _134 = _125 * _131
                __BLNK___w[_133] = _134
                _135 = _int(n)
                _136 = _135 * 3
                _137 = _int(k)
                _138 = _136 + _137
                _139 = _138 + -4
                _140 = taum[_139]
                _141 = _int(ib)
                _142 = _141 + -1
                _143 = __BLNK___w[_142]
                _144 = _int(mol)
                _145 = _144 + -1
                _146 = cp1s[_145]
                _147 = _143 * _146
                _148 = _int(n)
                _149 = _148 * 3
                _150 = _int(k)
                _151 = _149 + _150
                _152 = _151 + -4
                _153 = _140 + _147
                taum[_152] = _153
                _154 = _int(n)
                _155 = _154 * 3
                _156 = _int(k)
                _157 = _155 + _156
                _158 = _157 + -4
                _159 = twgp[_158]
                _160 = _int(ib)
                _161 = _160 + -1
                _162 = __BLNK___w[_161]
                _163 = _int(mol)
                _164 = _163 + -1
                _165 = cp1s[_164]
                _166 = _162 * _165
                _167 = _int(mol)
                _168 = _167 * 3
                _169 = _int(k)
                _170 = _168 + _169
                _171 = _170 + -4
                _172 = dpwj[_171]
                _173 = _166 * _172
                _174 = _int(n)
                _175 = _174 * 3
                _176 = _int(k)
                _177 = _175 + _176
                _178 = _177 + -4
                _179 = _159 + _173
                twgp[_178] = _179
                _pc = 39
            case 39:  # L.207
                mol = _int(mol + 1)
                _pc = 35
                continue
            case 40:  # L.208
                _180 = _int(n)
                _181 = _180 * 3
                _182 = _int(k)
                _183 = _181 + _182
                _184 = _183 + -4
                dpj[_184] = dpc
                _185 = _int(n)
                _186 = _185 * 3
                _187 = _int(k)
                _188 = _186 + _187
                _189 = _188 + -4
                _190 = taum[_189]
                _pc = 41 if _190 != 0.0 else 42
                continue
            case 41:  # <D.18198>
                _191 = _int(n)
                _192 = _191 * 3
                _193 = _int(k)
                _194 = _192 + _193
                _195 = _194 + -4
                _196 = twgp[_195]
                _197 = _int(n)
                _198 = _197 * 3
                _199 = _int(k)
                _200 = _198 + _199
                _201 = _200 + -4
                _202 = taum[_201]
                _203 = _int(n)
                _204 = _203 * 3
                _205 = _int(k)
                _206 = _204 + _205
                _207 = _206 + -4
                _208 = _div(_196, _202)
                dpj[_207] = _208
                _pc = 42
                continue
            case 42:  # L.205
                n = _int(n + 1)
                _pc = 33
                continue
            case 43:  # L.203
                k = _int(k + 1)
                _pc = 31
                continue
            case 44:  # L.204
                D_8659 = _int(nlayrs)
                n = _int(1)
                _pc = 45
            case 45:  # <D.18201>
                D_8662 = _int(n > D_8659)
                _pc = 51 if D_8662 != 0 else 46
                continue
            case 46:  # <D.18202>
                _209 = _int(n)
                _210 = _209 + -1
                _211 = _210 * 3
                _212 = dpj[_211]
                _213 = _int(n)
                _214 = _213 * 3
                _215 = _214 + -2
                _216 = dpj[_215]
                _217 = _212 + _216
                _218 = _int(n)
                _219 = _218 * 3
                _220 = _219 + -1
                _221 = dpj[_220]
                smdpj = _f32(_217 + _221)
                k = _int(1)
                _pc = 47
            case 47:  # <D.18203>
                D_8665 = _int(k > 3)
                _pc = 50 if D_8665 != 0 else 48
                continue
            case 48:  # <D.18204>
                _222 = _int(n)
                _223 = _222 * 3
                _224 = _int(k)
                _225 = _223 + _224
                _226 = _225 + -4
                _227 = dpj[_226]
                _228 = _int(n)
                _229 = _228 * 3
                _230 = _int(k)
                _231 = _229 + _230
                _232 = _231 + -4
                _233 = _div(_227, smdpj)
                dpj[_232] = _233
                _pc = 49
            case 49:  # L.213
                k = _int(k + 1)
                _pc = 47
                continue
            case 50:  # L.211
                n = _int(n + 1)
                _pc = 45
                continue
            case 51:  # L.212
                k = _int(1)
                _pc = 52
            case 52:  # <D.18205>
                D_8669 = _int(k > 3)
                _pc = 115 if D_8669 != 0 else 53
                continue
            case 53:  # <D.18206>
                rdncn = _f32(0.0)
                rdncns = _f32(0.0)
                rupcn = _f32(card1_salb[0])
                rupcns = _f32(card1_salb[0])
                _234 = _int(ng1)
                _235 = _234 + -1
                _236 = tle[_235:]
                _237 = _ft_bbfn(_state, _236, v)
                _238 = cnstns_pi[0]
                _239 = _int(ng1)
                _240 = _239 + -1
                _241 = _237 * _238
                tran_btop[_240] = _241
                _242 = 1.0e+0 - rupcn
                _243 = _242
                _244 = _int(ng1)
                _245 = _244 + -1
                _246 = tran_btop[_245]
                eupcn = _f32(_243 * _246)
                _247 = _int(ng)
                _248 = _247 + -1
                eup[_248] = eupcn
                _249 = _int(ng)
                _250 = _249 + -1
                eupc[_250] = eupcn
                _251 = card1_iemsct[0]
                _pc = 54 if _251 == 2 else 55
                continue
            case 54:  # <D.18207>
                _252 = cntrl_ml[0]
                mf = _int(_252 + -1)
                _253 = _int(mf)
                _254 = _253 + -1
                _255 = cszen[_254]
                _256 = rupcns * _255
                _257 = _int(mf)
                _258 = strn[_257]
                _259 = _256 * _258
                _260 = s0[0]
                eupcns = _f32(_259 * _260)
                _pc = 56
                continue
            case 55:  # <D.18208>
                eupcns = _f32(0.0)
                _pc = 56
            case 56:  # L.217
                _261 = _int(ng)
                _262 = _261 + -1
                eups[_262] = eupcns
                _263 = _int(ng)
                _264 = _263 + -1
                eupcs[_264] = eupcns
                D_8671 = _int(nlayrs)
                n = _int(D_8671)
                _pc = 57
            case 57:  # <D.18210>
                D_8674 = _int(n <= 0)
                _pc = 95 if D_8674 != 0 else 58
                continue
            case 58:  # <D.18211>
                m = _int(n + -1)
                _pc = 59 if k == 1 else 60
                continue
            case 59:  # <D.18212>
                _265 = _int(n)
                _266 = _265 * 3
                _267 = _int(k)
                _268 = _266 + _267
                _269 = _268 + -4
                _270 = taum[_269]
                _271 = _int(n)
                _272 = _271 * 3
                _273 = _int(k)
                _274 = _272 + _273
                _275 = _274 + -4
                _276 = dpj[_275]
                _277 = _int(n)
                _278 = _277 + -1
                _279 = _270 * _276
                taut[_278] = _279
                _pc = 64
                continue
            case 60:  # <D.18213>
                _280 = _int(n)
                _281 = _280 * 3
                _282 = _int(k)
                _283 = _281 + _282
                _284 = _283 + -4
                _285 = taum[_284]
                _286 = _int(n)
                _287 = _286 * 3
                _288 = _int(k)
                _289 = _287 + _288
                _290 = _289 + -4
                _291 = dpj[_290]
                _292 = _285 * _291
                _293 = _int(n)
                _294 = _293 + -1
                _295 = taut[_294]
                _296 = _int(n)
                _297 = _296 + -1
                _298 = _292 + _295
                taut[_297] = _298
                _299 = _int(n)
                _300 = _299 + -1
                _301 = taut[_300]
                _302 = _int(n)
                _303 = _302 + -1
                _304 = taer[_303]
                _305 = _301 + _304
                _306 = _int(n)
                _307 = _306 + -1
                _308 = tran_tcont[_307]
                _309 = _305 + _308
                _310 = _int(n)
                _311 = _310 + -1
                _312 = tran_tmols[_311]
                _313 = _309 + _312
                denom = _f32(_313)
                _pc = 61 if denom <= 0.0 else 62
                continue
            case 61:  # <D.18215>
                denom = _f32(1.0e+0)
                _pc = 62
                continue
            case 62:  # L.221
                _pc = 63 if k == 3 else 64
                continue
            case 63:  # <D.18218>
                _314 = _int(n)
                _315 = _314 + -1
                _316 = tran_taers[_315]
                _317 = _int(n)
                _318 = _317 + -1
                _319 = tran_tmols[_318]
                _320 = _316 + _319
                _321 = _320
                _322 = _int(n)
                _323 = _322 + -1
                _324 = _div(_321, denom)
                omega0[_323] = _324
                _pc = 64
                continue
            case 64:  # L.220
                _325 = _int(n)
                _326 = _325 * 3
                _327 = _int(k)
                _328 = _326 + _327
                _329 = _328 + -4
                _330 = taum[_329]
                _331 = _int(n)
                _332 = _331 + -1
                _333 = taer[_332]
                _334 = _330 + _333
                _335 = _int(n)
                _336 = _335 + -1
                _337 = tran_tcont[_336]
                _338 = _334 + _337
                _339 = _int(n)
                _340 = _339 + -1
                _341 = tran_tmols[_340]
                xp = _f32(_338 + _341)
                _342 = ikmax[0]
                _343 = _342 - n
                _344 = _343 + 1
                _345 = _int(_344)
                _346 = _345 + -1
                _347 = model_zm[_346]
                _348 = ikmax[0]
                _349 = _348 - n
                _350 = _int(_349)
                _351 = _350 + -1
                _352 = model_zm[_351]
                _353 = _347 - _352
                _354 = _353
                _355 = xp * _354
                _356 = ikmax[0]
                _357 = _356 - n
                _358 = _int(_357)
                _359 = _358 + -1
                _360 = path_pl[_359]
                x = _f32(_div(_355, _360))
                _361 = _int(n)
                _362 = _361 + -1
                _363 = tran_taers[_362]
                _364 = _int(n)
                _365 = _364 + -1
                _366 = tran_tmols[_365]
                _367 = _363 + _366
                _368 = _367
                _369 = _int(n)
                _370 = _369 + -1
                _371 = _div(_368, xp)
                omegak[_370] = _371
                _pc = 65
            case 65:  # __label_000160
                _372 = _int(n)
                _373 = _372 + -1
                _374 = omegak[_373]
                _pc = 66 if _374 > 9.99989986419677734375e-1 else 67
                continue
            case 66:  # <D.18221>
                _pc = 75
                continue
            case 67:  # L.223
                _375 = _int(n)
                _376 = _375 + -1
                _377 = omegak[_376]
                _378 = 1.0e+0 - _377
                aer1 = _f64(_f64(_378))
                _379 = _int(n)
                _380 = _379 + -1
                _381 = omegak[_380]
                _382 = _int(n)
                _383 = _382 + -1
                _384 = cosbar[_383]
                _385 = _381 * _384
                _386 = 1.0e+0 - _385
                aer2 = _f64(_f64(_386))
                _387 = _div(aer1, aer2)
                aera = _f64(__builtin_sqrt(_387))
                _388 = 1.0e+0 - aera
                _389 = _388
                aeru = _f64(_div(_389, 2.0e+0))
                _390 = aera + 1.0e+0
                _391 = _390
                aerv = _f64(_div(_391, 2.0e+0))
                _392 = aer1 * 3.0e+0
                _393 = aer2 * _392
                aerc = _f64(__builtin_sqrt(_393))
                _394 = _f64(x)
                aercx = _f64(aerc * _394)
                _395 = cnstns_bigexp[0]
                _396 = _f64(_395)
                _pc = 68 if aercx < _396 else 69
                continue
            case 68:  # <D.18223>
                _397 = -aercx
                ex1 = _f64(__builtin_exp(_397))
                _pc = 70
                continue
            case 69:  # <D.18224>
                _398 = cnstns_bignum[0]
                _399 = _div(1.0e+0, _398)
                ex1 = _f64(_f64(_399))
                _pc = 70
            case 70:  # L.224
                ex2 = _f64(ex1 * ex1)
                _400 = aerv * aerv
                _401 = aeru * aeru
                _402 = ex2 * _401
                _403 = _400 - _402
                deno = _f64(_403)
                _404 = _int(n)
                _405 = _404 + -1
                _406 = tran_btop[_405]
                _407 = n + 1
                _408 = _int(_407)
                _409 = _408 + -1
                _410 = tran_btop[_409]
                _411 = _406 - _410
                _412 = _411
                _413 = _div(_412, x)
                _414 = _f64(_413)
                _415 = _div(_414, aerc)
                _416 = aeru * ex2
                _417 = aerv - _416
                _418 = aera * ex1
                _419 = _417 - _418
                _420 = _419
                dnmo = _f64(_415 * _420)
                _421 = aeru * ex2
                dnm1 = _f64(aerv + _421)
                _422 = _int(n)
                _423 = _422 + -1
                _424 = tran_btop[_423]
                _425 = _f64(_424)
                _426 = dnm1 * _425
                _427 = _426 - dnmo
                _428 = n + 1
                _429 = _int(_428)
                _430 = _429 + -1
                _431 = tran_btop[_430]
                _432 = _f64(_431)
                _433 = ex1 * _432
                _434 = _427 - _433
                _435 = _434
                _436 = _div(_435, deno)
                _437 = aera * _436
                _438 = _int(n)
                _439 = _438 + -1
                _440 = _f32(_437)
                eup[_439] = _440
                _441 = n + 1
                _442 = _int(_441)
                _443 = _442 + -1
                _444 = tran_btop[_443]
                _445 = _f64(_444)
                _446 = dnm1 * _445
                _447 = dnmo + _446
                _448 = _int(n)
                _449 = _448 + -1
                _450 = tran_btop[_449]
                _451 = _f64(_450)
                _452 = ex1 * _451
                _453 = _447 - _452
                _454 = _453
                _455 = _div(_454, deno)
                _456 = aera * _455
                _457 = _int(n)
                _458 = _457 + -1
                _459 = _f32(_456)
                edn[_458] = _459
                _460 = _int(n)
                _461 = _460 + -1
                _462 = eup[_461]
                _pc = 71 if _462 < 0.0 else 72
                continue
            case 71:  # <D.18226>
                _463 = _int(n)
                _464 = _463 + -1
                eup[_464] = 0.0
                _pc = 72
                continue
            case 72:  # L.225
                _465 = _int(n)
                _466 = _465 + -1
                _467 = edn[_466]
                _pc = 73 if _467 < 0.0 else 74
                continue
            case 73:  # <D.18229>
                _468 = _int(n)
                _469 = _468 + -1
                edn[_469] = 0.0
                _pc = 74
                continue
            case 74:  # L.226
                _470 = aeru * aerv
                _471 = 1.0e+0 - ex2
                _472 = _471
                _473 = _470 * _472
                _474 = _div(_473, deno)
                _475 = _int(n)
                _476 = _475 + -1
                _477 = _f32(_474)
                ref[_476] = _477
                _478 = aerv - aeru
                _479 = _478
                _480 = _div(_479, deno)
                _481 = ex1 * _480
                _482 = _int(n)
                _483 = _482 + -1
                _484 = _f32(_481)
                tdf[_483] = _484
                _pc = 76
                continue
            case 75:  # __label_000115
                _485 = _int(n)
                _486 = _485 + -1
                _487 = cosbar[_486]
                _488 = 1.0e+0 - _487
                _489 = _488
                _490 = _489 * 1.73205077648162841796875e+0
                _491 = _div(_490, 2.0e+0)
                _492 = x * _491
                _493 = _492 + 1.0e+0
                _494 = _493
                _495 = _int(n)
                _496 = _495 + -1
                _497 = _div(1.0e+0, _494)
                tdf[_496] = _497
                _498 = _int(n)
                _499 = _498 + -1
                _500 = tdf[_499]
                _501 = _int(n)
                _502 = _501 + -1
                _503 = 1.0e+0 - _500
                ref[_502] = _503
                _504 = _int(n)
                _505 = _504 + -1
                eup[_505] = 0.0
                _506 = _int(n)
                _507 = _506 + -1
                edn[_507] = 0.0
                _pc = 76
            case 76:  # __label_000114
                _508 = card1_iemsct[0]
                _pc = 77 if _508 == 2 else 91
                continue
            case 77:  # <D.18232>
                _509 = _int(n)
                _510 = _509 + -1
                smu = _f32(cszen[_510])
                _511 = _int(n)
                _512 = _511 + -1
                b0 = _f32(bets[_512])
                _513 = _int(n)
                _514 = _513 + -1
                ome0 = _f32(omegak[_514])
                _pc = 78 if ome0 >= 9.99998986721038818359375e-1 else 79
                continue
            case 78:  # <D.18234>
                ome0 = _f32(9.99998986721038818359375e-1)
                _pc = 79
                continue
            case 79:  # L.228
                _515 = _int(n)
                _516 = _515 + -1
                g = _f32(cosbar[_516])
                D_8687 = _f32(g)
                _517 = __builtin_powf(D_8687, 2.0e+0)
                _518 = 1.0e+0 - smu
                _519 = _518
                _520 = _517 * _519
                _521 = 1.0e+0 - _520
                _522 = _521
                q = _f32(_522 * 4.0e+0)
                D_8688 = _f32(g)
                D_8689 = _f32(g)
                _523 = __builtin_powf(D_8688, 2.0e+0)
                _524 = _523 * 3.0e+0
                _525 = 7.0e+0 - _524
                _526 = g * 3.0e+0
                _527 = _526 + 4.0e+0
                _528 = _527
                _529 = ome0 * _528
                _530 = _525 - _529
                _531 = __builtin_powf(D_8689, 2.0e+0)
                _532 = ome0 * _531
                _533 = b0 * 4.0e+0
                _534 = g * 3.0e+0
                _535 = _533 + _534
                _536 = _535
                _537 = _532 * _536
                _538 = _530 + _537
                _539 = _538
                gm1 = _f32(_div(_539, q))
                D_8690 = _f32(g)
                D_8691 = _f32(g)
                _540 = __builtin_powf(D_8690, 2.0e+0)
                _541 = 1.0e+0 - _540
                _542 = g * 3.0e+0
                _543 = 4.0e+0 - _542
                _544 = _543
                _545 = ome0 * _544
                _546 = _541 - _545
                _547 = __builtin_powf(D_8691, 2.0e+0)
                _548 = ome0 * _547
                _549 = b0 * 4.0e+0
                _550 = g * 3.0e+0
                _551 = _549 + _550
                _552 = _551 - 4.0e+0
                _553 = _552
                _554 = _548 * _553
                _555 = _546 - _554
                _556 = _555
                _557 = _div(_556, q)
                gm2 = _f32(-_557)
                _pc = 80 if gm2 == 0.0 else 81
                continue
            case 80:  # <D.18237>
                gm2 = _f32(1.00000001335143196001808973960578441619873046875e-10)
                _pc = 81
                continue
            case 81:  # L.229
                _558 = gm1 * gm1
                _559 = gm2 * gm2
                _560 = _558 - _559
                sk = _f32(__builtin_sqrtf(_560))
                _561 = _int(n)
                _562 = _561 + -1
                _563 = bets[_562]
                _564 = _div(_563, smu)
                _565 = _int(n)
                _566 = _565 + -1
                _567 = bets[_566]
                _568 = gm1 * _567
                _569 = _564 - _568
                _570 = _int(n)
                _571 = _570 + -1
                _572 = bets[_571]
                _573 = 1.0e+0 - _572
                _574 = _573
                _575 = gm2 * _574
                _576 = _569 - _575
                _577 = _576
                _578 = ome0 * _577
                _579 = smu * smu
                _580 = sk * sk
                _581 = smu * _580
                _582 = smu * _581
                _583 = 1.0e+0 - _582
                _584 = _583
                _585 = _div(_579, _584)
                _586 = _585
                cs = _f32(_578 * _586)
                _587 = _div(1.0e+0, smu)
                _588 = gm1 + _587
                _589 = _588
                _590 = cs * _589
                _591 = _int(n)
                _592 = _591 + -1
                _593 = bets[_592]
                _594 = ome0 * _593
                ys = _f32(_590 - _594)
                ektl = _f32(sk * x)
                _595 = cnstns_bigexp[0]
                _pc = 82 if ektl < _595 else 83
                continue
            case 82:  # <D.18240>
                _596 = -ektl
                ekt = _f32(__builtin_expf(_596))
                _pc = 84
                continue
            case 83:  # <D.18241>
                _597 = cnstns_bignum[0]
                ekt = _f32(_div(1.0e+0, _597))
                _pc = 84
            case 84:  # L.230
                ekt2 = _f32(ekt * ekt)
                etmul = _f32(_div(x, smu))
                _598 = cnstns_bigexp[0]
                _pc = 85 if etmul < _598 else 86
                continue
            case 85:  # <D.18243>
                _599 = -etmul
                etmu = _f32(__builtin_expf(_599))
                _pc = 87
                continue
            case 86:  # <D.18244>
                _600 = cnstns_bignum[0]
                etmu = _f32(_div(1.0e+0, _600))
                _pc = 87
            case 87:  # L.231
                gmpsk = _f32(gm1 + sk)
                gmmsk = _f32(gm1 - sk)
                _601 = ekt2 * gmmsk
                _602 = _601
                denom = _f32(_602 - gmpsk)
                _603 = ys * ekt
                _604 = gmpsk * cs
                _605 = etmu * _604
                _606 = _603 - _605
                _607 = _606
                _608 = gmmsk * _607
                _609 = _div(_608, denom)
                asxp = _f32(-_609)
                _610 = ys * ekt2
                _611 = gmpsk * cs
                _612 = etmu * _611
                _613 = ekt * _612
                _614 = _610 - _613
                _615 = _614
                _616 = _div(_615, denom)
                asnew = _f32(-_616)
                _617 = cs * etmu
                _618 = ekt * _617
                _619 = gmmsk * _618
                _620 = _619
                _621 = ys - _620
                _622 = _621
                bsnew = _f32(_div(_622, denom))
                _623 = asnew + bsnew
                _624 = _int(n)
                _625 = _624 + -1
                _626 = cs + _623
                eups[_625] = _626
                _627 = gmpsk
                _628 = bsnew * _627
                _629 = ekt * _628
                _630 = asxp + _629
                _631 = ys * etmu
                _632 = _630 + _631
                _633 = _632
                _634 = _int(n)
                _635 = _634 + -1
                _636 = _div(_633, gm2)
                edns[_635] = _636
                _637 = _int(n)
                _638 = _637 + -1
                _639 = cszen[_638]
                _640 = _639
                fc = _f32(_div(1.0e+0, _640))
                _641 = _int(n)
                _642 = _641 + -1
                _643 = eups[_642]
                _644 = _int(n)
                _645 = _644 + -1
                _646 = fc * _643
                refs[_645] = _646
                _647 = _int(n)
                _648 = _647 + -1
                _649 = cszen[_648]
                xcszen = _f32(_div(x, _649))
                _650 = cnstns_bigexp[0]
                _pc = 88 if xcszen < _650 else 89
                continue
            case 88:  # <D.18246>
                _651 = _int(n)
                _652 = _651 + -1
                _653 = edns[_652]
                _654 = fc * _653
                _655 = -xcszen
                _656 = __builtin_expf(_655)
                _657 = _int(n)
                _658 = _657 + -1
                _659 = _654 + _656
                tdfs[_658] = _659
                _pc = 90
                continue
            case 89:  # <D.18247>
                _660 = _int(n)
                _661 = _660 + -1
                _662 = edns[_661]
                _663 = _int(n)
                _664 = _663 + -1
                _665 = fc * _662
                tdfs[_664] = _665
                _pc = 90
            case 90:  # L.232
                _666 = _int(n)
                _667 = _666 + -1
                _668 = eups[_667]
                _669 = s0[0]
                _670 = _668 * _669
                _671 = _int(m)
                _672 = strn[_671]
                _673 = _int(n)
                _674 = _673 + -1
                _675 = _670 * _672
                eups[_674] = _675
                _676 = _int(n)
                _677 = _676 + -1
                _678 = edns[_677]
                _679 = s0[0]
                _680 = _678 * _679
                _681 = _int(m)
                _682 = strn[_681]
                _683 = _int(n)
                _684 = _683 + -1
                _685 = _680 * _682
                edns[_684] = _685
                _pc = 91
                continue
            case 91:  # L.227
                _686 = _int(n)
                _687 = _686 + -1
                _688 = ref[_687]
                _689 = rupcn * _688
                _690 = 1.0e+0 - _689
                deno = _f64(_f64(_690))
                _691 = _int(n)
                _692 = _691 + -1
                _693 = refs[_692]
                _694 = rupcns * _693
                denos = _f32(1.0e+0 - _694)
                _pc = 92
            case 92:  # __label_000125
                _695 = _int(n)
                _696 = _695 + -1
                _697 = eup[_696]
                _698 = _f64(_697)
                _699 = _int(n)
                _700 = _699 + -1
                _701 = edn[_700]
                _702 = rupcn * _701
                _703 = eupcn + _702
                _704 = _703
                _705 = _int(n)
                _706 = _705 + -1
                _707 = tdf[_706]
                _708 = _704 * _707
                _709 = _f64(_708)
                _710 = _div(_709, deno)
                _711 = _698 + _710
                eupcn = _f32(_f32(_711))
                _712 = _int(n)
                _713 = _712 + -1
                _714 = eups[_713]
                _715 = _int(n)
                _716 = _715 + -1
                _717 = edns[_716]
                _718 = rupcns * _717
                _719 = eupcns + _718
                _720 = _719
                _721 = _int(n)
                _722 = _721 + -1
                _723 = tdfs[_722]
                _724 = _720 * _723
                _725 = _div(_724, denos)
                eupcns = _f32(_714 + _725)
                _726 = _int(n)
                _727 = _726 + -1
                _728 = refs[_727]
                _729 = _int(n)
                _730 = _729 + -1
                _731 = tdfs[_730]
                _732 = rupcns * _731
                _733 = _int(n)
                _734 = _733 + -1
                _735 = tdfs[_734]
                _736 = _732 * _735
                _737 = _div(_736, denos)
                rupcns = _f32(_728 + _737)
                _pc = 93
            case 93:  # __label_000140
                _738 = _int(n)
                _739 = _738 + -1
                _740 = ref[_739]
                _741 = _f64(_740)
                _742 = _int(n)
                _743 = _742 + -1
                _744 = tdf[_743]
                _745 = rupcn * _744
                _746 = _int(n)
                _747 = _746 + -1
                _748 = tdf[_747]
                _749 = _745 * _748
                _750 = _f64(_749)
                _751 = _div(_750, deno)
                _752 = _741 + _751
                rupcn = _f32(_f32(_752))
                _753 = _int(n)
                _754 = _753 + -1
                eupc[_754] = eupcn
                _755 = _int(n)
                _756 = _755 + -1
                eupcs[_756] = eupcns
                _757 = _int(n)
                _758 = _757 + -1
                rupc[_758] = rupcn
                _759 = _int(n)
                _760 = _759 + -1
                rupcs[_760] = rupcns
                _pc = 94
            case 94:  # L.218
                n = _int(n + -1)
                _pc = 57
                continue
            case 95:  # L.219
                edncn = _f32(0.0)
                edncns = _f32(0.0)
                _761 = _int(k)
                _762 = _761 + -1
                dnf[_762] = edncn
                _763 = _int(k)
                _764 = _763 + -1
                _765 = eupc[0]
                upf[_764] = _765
                _766 = card1_iemsct[0]
                _pc = 96 if _766 == 2 else 97
                continue
            case 96:  # <D.18250>
                _767 = _int(k)
                _768 = _767 + -1
                dnfs[_768] = edncns
                _769 = _int(k)
                _770 = _769 + -1
                _771 = eupcs[0]
                upfs[_770] = _771
                _pc = 97
                continue
            case 97:  # L.233
                rdncn = _f32(0.0)
                rdncns = _f32(0.0)
                D_8700 = _int(ng)
                n = _int(2)
                _pc = 98
            case 98:  # <D.18253>
                D_8703 = _int(n > D_8700)
                _pc = 105 if D_8703 != 0 else 99
                continue
            case 99:  # <D.18254>
                m = _int(n + -1)
                _772 = _int(m)
                _773 = _772 + -1
                _774 = ref[_773]
                _775 = rdncn * _774
                _776 = 1.0e+0 - _775
                deno = _f64(_f64(_776))
                _777 = _int(m)
                _778 = _777 + -1
                _779 = refs[_778]
                _780 = rdncns * _779
                denos = _f32(1.0e+0 - _780)
                _pc = 100
            case 100:  # __label_000121
                _781 = _int(m)
                _782 = _781 + -1
                _783 = edn[_782]
                _784 = _f64(_783)
                _785 = _int(m)
                _786 = _785 + -1
                _787 = eup[_786]
                _788 = rdncn * _787
                _789 = edncn + _788
                _790 = _789
                _791 = _int(m)
                _792 = _791 + -1
                _793 = tdf[_792]
                _794 = _790 * _793
                _795 = _f64(_794)
                _796 = _div(_795, deno)
                _797 = _784 + _796
                edncn = _f32(_f32(_797))
                _798 = _int(m)
                _799 = _798 + -1
                _800 = ref[_799]
                _801 = _f64(_800)
                _802 = _int(m)
                _803 = _802 + -1
                _804 = tdf[_803]
                _805 = _int(m)
                _806 = _805 + -1
                _807 = tdf[_806]
                _808 = _804 * _807
                _809 = rdncn * _808
                _810 = _f64(_809)
                _811 = _div(_810, deno)
                _812 = _801 + _811
                rdncn = _f32(_f32(_812))
                _pc = 101
            case 101:  # __label_000132
                _813 = _int(n)
                _814 = _813 + -1
                _815 = eupc[_814]
                _816 = _int(n)
                _817 = _816 + -1
                _818 = rupc[_817]
                _819 = edncn * _818
                _820 = _815 + _819
                _821 = _820
                _822 = _f64(_821)
                _823 = _div(_822, deno)
                pefup = _f32(_f32(_823))
                _824 = _int(n)
                _825 = _824 + -1
                _826 = eupc[_825]
                _827 = rdncn * _826
                _828 = edncn + _827
                _829 = _828
                _830 = _f64(_829)
                _831 = _div(_830, deno)
                pefdn = _f32(_f32(_831))
                _832 = card1_iemsct[0]
                _pc = 102 if _832 == 2 else 103
                continue
            case 102:  # <D.18255>
                _833 = _int(m)
                _834 = _833 + -1
                _835 = edns[_834]
                _836 = _int(m)
                _837 = _836 + -1
                _838 = eups[_837]
                _839 = rdncns * _838
                _840 = edncns + _839
                _841 = _840
                _842 = _int(m)
                _843 = _842 + -1
                _844 = tdfs[_843]
                _845 = _841 * _844
                _846 = _div(_845, denos)
                edncns = _f32(_835 + _846)
                _847 = _int(m)
                _848 = _847 + -1
                _849 = refs[_848]
                _850 = _int(m)
                _851 = _850 + -1
                _852 = tdfs[_851]
                _853 = _int(m)
                _854 = _853 + -1
                _855 = tdfs[_854]
                _856 = _852 * _855
                _857 = rdncns * _856
                _858 = _div(_857, denos)
                rdncns = _f32(_849 + _858)
                _859 = _int(n)
                _860 = _859 + -1
                _861 = eupcs[_860]
                _862 = _int(n)
                _863 = _862 + -1
                _864 = rupcs[_863]
                _865 = edncns * _864
                _866 = _861 + _865
                _867 = _866
                pefups = _f32(_div(_867, denos))
                _868 = _int(n)
                _869 = _868 + -1
                _870 = eupcs[_869]
                _871 = rdncns * _870
                _872 = edncns + _871
                _873 = _872
                pefdns = _f32(_div(_873, denos))
                _874 = _int(n)
                _875 = _874 * 15
                _876 = _int(k)
                _877 = _875 + _876
                _878 = _877 + -16
                upfs[_878] = pefups
                _879 = _int(n)
                _880 = _879 * 15
                _881 = _int(k)
                _882 = _880 + _881
                _883 = _882 + -16
                dnfs[_883] = pefdns
                _pc = 103
                continue
            case 103:  # __label_000120
                _884 = _int(n)
                _885 = _884 * 10
                _886 = _int(k)
                _887 = _885 + _886
                _888 = _887 + -11
                upf[_888] = pefup
                _889 = _int(n)
                _890 = _889 * 10
                _891 = _int(k)
                _892 = _890 + _891
                _893 = _892 + -11
                dnf[_893] = pefdn
                _pc = 104
            case 104:  # L.234
                n = _int(n + 1)
                _pc = 98
                continue
            case 105:  # L.235
                _894 = ng + -1
                _895 = _int(_894)
                _896 = _895 * 3
                _897 = _int(k)
                _898 = _896 + _897
                _899 = _898 + -4
                _900 = _int(ng)
                _901 = _900 * 3
                _902 = _int(k)
                _903 = _901 + _902
                _904 = _903 + -4
                _905 = dpj[_899]
                dpj[_904] = _905
                D_8709 = _int(ng)
                n = _int(2)
                _pc = 106
            case 106:  # <D.18258>
                D_8712 = _int(n > D_8709)
                _pc = 111 if D_8712 != 0 else 107
                continue
            case 107:  # <D.18259>
                m = _int(n + -1)
                _pc = 108 if k == 1 else 109
                continue
            case 108:  # <D.18260>
                _906 = _int(m)
                _907 = _906 * 10
                _908 = _int(k)
                _909 = _907 + _908
                _910 = _909 + -11
                _911 = upf[_910]
                _912 = _int(n)
                _913 = _912 * 10
                _914 = _int(k)
                _915 = _913 + _914
                _916 = _915 + -11
                _917 = upf[_916]
                _918 = _911 + _917
                _919 = _918
                _920 = _919 * 5.0e-1
                _921 = _int(m)
                _922 = _921 * 3
                _923 = _int(k)
                _924 = _922 + _923
                _925 = _924 + -4
                _926 = dpj[_925]
                _927 = _int(m)
                _928 = _927 + -1
                _929 = _920 * _926
                umf[_928] = _929
                _930 = _int(m)
                _931 = _930 * 15
                _932 = _int(k)
                _933 = _931 + _932
                _934 = _933 + -16
                _935 = upfs[_934]
                _936 = _int(n)
                _937 = _936 * 15
                _938 = _int(k)
                _939 = _937 + _938
                _940 = _939 + -16
                _941 = upfs[_940]
                _942 = _935 + _941
                _943 = _942
                _944 = _943 * 5.0e-1
                _945 = _int(m)
                _946 = _945 * 3
                _947 = _int(k)
                _948 = _946 + _947
                _949 = _948 + -4
                _950 = dpj[_949]
                _951 = _int(m)
                _952 = _951 + -1
                _953 = _944 * _950
                umfs[_952] = _953
                _954 = _int(m)
                _955 = _954 * 10
                _956 = _int(k)
                _957 = _955 + _956
                _958 = _957 + -11
                _959 = dnf[_958]
                _960 = _int(n)
                _961 = _960 * 10
                _962 = _int(k)
                _963 = _961 + _962
                _964 = _963 + -11
                _965 = dnf[_964]
                _966 = _959 + _965
                _967 = _966
                _968 = _967 * 5.0e-1
                _969 = _int(m)
                _970 = _969 * 3
                _971 = _int(k)
                _972 = _970 + _971
                _973 = _972 + -4
                _974 = dpj[_973]
                _975 = _int(m)
                _976 = _975 + -1
                _977 = _968 * _974
                dmf[_976] = _977
                _978 = _int(m)
                _979 = _978 * 15
                _980 = _int(k)
                _981 = _979 + _980
                _982 = _981 + -16
                _983 = dnfs[_982]
                _984 = _int(n)
                _985 = _984 * 15
                _986 = _int(k)
                _987 = _985 + _986
                _988 = _987 + -16
                _989 = dnfs[_988]
                _990 = _983 + _989
                _991 = _990
                _992 = _991 * 5.0e-1
                _993 = _int(m)
                _994 = _993 * 3
                _995 = _int(k)
                _996 = _994 + _995
                _997 = _996 + -4
                _998 = dpj[_997]
                _999 = _int(m)
                _1000 = _999 + -1
                _1001 = _992 * _998
                dmfs[_1000] = _1001
                _1002 = _int(n)
                _1003 = _1002 * 10
                _1004 = _int(k)
                _1005 = _1003 + _1004
                _1006 = _1005 + -11
                _1007 = upf[_1006]
                _1008 = _int(n)
                _1009 = _1008 * 3
                _1010 = _int(k)
                _1011 = _1009 + _1010
                _1012 = _1011 + -4
                _1013 = dpj[_1012]
                _1014 = _int(n)
                _1015 = _1014 + -1
                _1016 = _1007 * _1013
                dirst_umb[_1015] = _1016
                _1017 = _int(n)
                _1018 = _1017 * 15
                _1019 = _int(k)
                _1020 = _1018 + _1019
                _1021 = _1020 + -16
                _1022 = upfs[_1021]
                _1023 = _int(n)
                _1024 = _1023 * 3
                _1025 = _int(k)
                _1026 = _1024 + _1025
                _1027 = _1026 + -4
                _1028 = dpj[_1027]
                _1029 = _int(n)
                _1030 = _1029 + -1
                _1031 = _1022 * _1028
                dirst_umbs[_1030] = _1031
                _1032 = _int(m)
                _1033 = _1032 * 10
                _1034 = _int(k)
                _1035 = _1033 + _1034
                _1036 = _1035 + -11
                _1037 = dnf[_1036]
                _1038 = _int(m)
                _1039 = _1038 * 3
                _1040 = _int(k)
                _1041 = _1039 + _1040
                _1042 = _1041 + -4
                _1043 = dpj[_1042]
                _1044 = _int(m)
                _1045 = _1044 + -1
                _1046 = _1037 * _1043
                dirst_dmb[_1045] = _1046
                _1047 = _int(m)
                _1048 = _1047 * 15
                _1049 = _int(k)
                _1050 = _1048 + _1049
                _1051 = _1050 + -16
                _1052 = dnfs[_1051]
                _1053 = _int(m)
                _1054 = _1053 * 3
                _1055 = _int(k)
                _1056 = _1054 + _1055
                _1057 = _1056 + -4
                _1058 = dpj[_1057]
                _1059 = _int(m)
                _1060 = _1059 + -1
                _1061 = _1052 * _1058
                dirst_dmbs[_1060] = _1061
                _pc = 110
                continue
            case 109:  # <D.18261>
                _1062 = _int(m)
                _1063 = _1062 + -1
                _1064 = umf[_1063]
                _1065 = _int(m)
                _1066 = _1065 * 10
                _1067 = _int(k)
                _1068 = _1066 + _1067
                _1069 = _1068 + -11
                _1070 = upf[_1069]
                _1071 = _int(n)
                _1072 = _1071 * 10
                _1073 = _int(k)
                _1074 = _1072 + _1073
                _1075 = _1074 + -11
                _1076 = upf[_1075]
                _1077 = _1070 + _1076
                _1078 = _1077
                _1079 = _1078 * 5.0e-1
                _1080 = _int(m)
                _1081 = _1080 * 3
                _1082 = _int(k)
                _1083 = _1081 + _1082
                _1084 = _1083 + -4
                _1085 = dpj[_1084]
                _1086 = _1079 * _1085
                _1087 = _int(m)
                _1088 = _1087 + -1
                _1089 = _1064 + _1086
                umf[_1088] = _1089
                _1090 = _int(m)
                _1091 = _1090 + -1
                _1092 = umfs[_1091]
                _1093 = _int(m)
                _1094 = _1093 * 15
                _1095 = _int(k)
                _1096 = _1094 + _1095
                _1097 = _1096 + -16
                _1098 = upfs[_1097]
                _1099 = _int(n)
                _1100 = _1099 * 15
                _1101 = _int(k)
                _1102 = _1100 + _1101
                _1103 = _1102 + -16
                _1104 = upfs[_1103]
                _1105 = _1098 + _1104
                _1106 = _1105
                _1107 = _1106 * 5.0e-1
                _1108 = _int(m)
                _1109 = _1108 * 3
                _1110 = _int(k)
                _1111 = _1109 + _1110
                _1112 = _1111 + -4
                _1113 = dpj[_1112]
                _1114 = _1107 * _1113
                _1115 = _int(m)
                _1116 = _1115 + -1
                _1117 = _1092 + _1114
                umfs[_1116] = _1117
                _1118 = _int(m)
                _1119 = _1118 + -1
                _1120 = dmf[_1119]
                _1121 = _int(m)
                _1122 = _1121 * 10
                _1123 = _int(k)
                _1124 = _1122 + _1123
                _1125 = _1124 + -11
                _1126 = dnf[_1125]
                _1127 = _int(n)
                _1128 = _1127 * 10
                _1129 = _int(k)
                _1130 = _1128 + _1129
                _1131 = _1130 + -11
                _1132 = dnf[_1131]
                _1133 = _1126 + _1132
                _1134 = _1133
                _1135 = _1134 * 5.0e-1
                _1136 = _int(m)
                _1137 = _1136 * 3
                _1138 = _int(k)
                _1139 = _1137 + _1138
                _1140 = _1139 + -4
                _1141 = dpj[_1140]
                _1142 = _1135 * _1141
                _1143 = _int(m)
                _1144 = _1143 + -1
                _1145 = _1120 + _1142
                dmf[_1144] = _1145
                _1146 = _int(m)
                _1147 = _1146 + -1
                _1148 = dmfs[_1147]
                _1149 = _int(m)
                _1150 = _1149 * 15
                _1151 = _int(k)
                _1152 = _1150 + _1151
                _1153 = _1152 + -16
                _1154 = dnfs[_1153]
                _1155 = _int(n)
                _1156 = _1155 * 15
                _1157 = _int(k)
                _1158 = _1156 + _1157
                _1159 = _1158 + -16
                _1160 = dnfs[_1159]
                _1161 = _1154 + _1160
                _1162 = _1161
                _1163 = _1162 * 5.0e-1
                _1164 = _int(m)
                _1165 = _1164 * 3
                _1166 = _int(k)
                _1167 = _1165 + _1166
                _1168 = _1167 + -4
                _1169 = dpj[_1168]
                _1170 = _1163 * _1169
                _1171 = _int(m)
                _1172 = _1171 + -1
                _1173 = _1148 + _1170
                dmfs[_1172] = _1173
                _1174 = _int(n)
                _1175 = _1174 + -1
                _1176 = dirst_umb[_1175]
                _1177 = _int(n)
                _1178 = _1177 * 10
                _1179 = _int(k)
                _1180 = _1178 + _1179
                _1181 = _1180 + -11
                _1182 = upf[_1181]
                _1183 = _int(n)
                _1184 = _1183 * 3
                _1185 = _int(k)
                _1186 = _1184 + _1185
                _1187 = _1186 + -4
                _1188 = dpj[_1187]
                _1189 = _1182 * _1188
                _1190 = _int(n)
                _1191 = _1190 + -1
                _1192 = _1176 + _1189
                dirst_umb[_1191] = _1192
                _1193 = _int(n)
                _1194 = _1193 + -1
                _1195 = dirst_umbs[_1194]
                _1196 = _int(n)
                _1197 = _1196 * 15
                _1198 = _int(k)
                _1199 = _1197 + _1198
                _1200 = _1199 + -16
                _1201 = upfs[_1200]
                _1202 = _int(n)
                _1203 = _1202 * 3
                _1204 = _int(k)
                _1205 = _1203 + _1204
                _1206 = _1205 + -4
                _1207 = dpj[_1206]
                _1208 = _1201 * _1207
                _1209 = _int(n)
                _1210 = _1209 + -1
                _1211 = _1195 + _1208
                dirst_umbs[_1210] = _1211
                _1212 = _int(m)
                _1213 = _1212 + -1
                _1214 = dirst_dmb[_1213]
                _1215 = _int(m)
                _1216 = _1215 * 10
                _1217 = _int(k)
                _1218 = _1216 + _1217
                _1219 = _1218 + -11
                _1220 = dnf[_1219]
                _1221 = _int(m)
                _1222 = _1221 * 3
                _1223 = _int(k)
                _1224 = _1222 + _1223
                _1225 = _1224 + -4
                _1226 = dpj[_1225]
                _1227 = _1220 * _1226
                _1228 = _int(m)
                _1229 = _1228 + -1
                _1230 = _1214 + _1227
                dirst_dmb[_1229] = _1230
                _1231 = _int(m)
                _1232 = _1231 + -1
                _1233 = dirst_dmbs[_1232]
                _1234 = _int(m)
                _1235 = _1234 * 15
                _1236 = _int(k)
                _1237 = _1235 + _1236
                _1238 = _1237 + -16
                _1239 = dnfs[_1238]
                _1240 = _int(m)
                _1241 = _1240 * 3
                _1242 = _int(k)
                _1243 = _1241 + _1242
                _1244 = _1243 + -4
                _1245 = dpj[_1244]
                _1246 = _1239 * _1245
                _1247 = _int(m)
                _1248 = _1247 + -1
                _1249 = _1233 + _1246
                dirst_dmbs[_1248] = _1249
                _pc = 110
            case 110:  # L.237
                n = _int(n + 1)
                _pc = 106
                continue
            case 111:  # L.238
                _pc = 112 if k == 1 else 113
                continue
            case 112:  # <D.18263>
                _1250 = _int(ng)
                _1251 = _1250 * 15
                _1252 = _int(k)
                _1253 = _1251 + _1252
                _1254 = _1253 + -16
                _1255 = dnfs[_1254]
                _1256 = _int(nlayrs)
                _1257 = _1256 * 3
                _1258 = _int(k)
                _1259 = _1257 + _1258
                _1260 = _1259 + -4
                _1261 = dpj[_1260]
                _1262 = _1255 * _1261
                fdnsrf[0] = _1262
                _1263 = _int(ng)
                _1264 = _1263 * 10
                _1265 = _int(k)
                _1266 = _1264 + _1265
                _1267 = _1266 + -11
                _1268 = dnf[_1267]
                _1269 = _int(nlayrs)
                _1270 = _1269 * 3
                _1271 = _int(k)
                _1272 = _1270 + _1271
                _1273 = _1272 + -4
                _1274 = dpj[_1273]
                _1275 = _1268 * _1274
                fdntrf[0] = _1275
                _1276 = _int(k)
                _1277 = _1276 + -1
                _1278 = upfs[_1277]
                _1279 = _int(k)
                _1280 = _1279 + -1
                _1281 = dpj[_1280]
                fupsrf = _f32(_1278 * _1281)
                _1282 = _int(k)
                _1283 = _1282 + -1
                _1284 = upf[_1283]
                _1285 = _int(k)
                _1286 = _1285 + -1
                _1287 = dpj[_1286]
                fuptrf = _f32(_1284 * _1287)
                _pc = 114
                continue
            case 113:  # <D.18264>
                _1288 = fdnsrf[0]
                _1289 = _int(ng)
                _1290 = _1289 * 15
                _1291 = _int(k)
                _1292 = _1290 + _1291
                _1293 = _1292 + -16
                _1294 = dnfs[_1293]
                _1295 = _int(nlayrs)
                _1296 = _1295 * 3
                _1297 = _int(k)
                _1298 = _1296 + _1297
                _1299 = _1298 + -4
                _1300 = dpj[_1299]
                _1301 = _1294 * _1300
                _1302 = _1288 + _1301
                fdnsrf[0] = _1302
                _1303 = fdntrf[0]
                _1304 = _int(ng)
                _1305 = _1304 * 10
                _1306 = _int(k)
                _1307 = _1305 + _1306
                _1308 = _1307 + -11
                _1309 = dnf[_1308]
                _1310 = _int(nlayrs)
                _1311 = _1310 * 3
                _1312 = _int(k)
                _1313 = _1311 + _1312
                _1314 = _1313 + -4
                _1315 = dpj[_1314]
                _1316 = _1309 * _1315
                _1317 = _1303 + _1316
                fdntrf[0] = _1317
                _1318 = _int(k)
                _1319 = _1318 + -1
                _1320 = upfs[_1319]
                _1321 = _int(k)
                _1322 = _1321 + -1
                _1323 = dpj[_1322]
                _1324 = _1320 * _1323
                fupsrf = _f32(fupsrf + _1324)
                _1325 = _int(k)
                _1326 = _1325 + -1
                _1327 = upf[_1326]
                _1328 = _int(k)
                _1329 = _1328 + -1
                _1330 = dpj[_1329]
                _1331 = _1327 * _1330
                fuptrf = _f32(fuptrf + _1331)
                _pc = 114
            case 114:  # L.215
                k = _int(k + 1)
                _pc = 52
                continue
            case 115:  # L.216
                dirst_umb[0] = fuptrf
                dirst_umbs[0] = fupsrf
                _1332 = _int(ng)
                _1333 = _1332 + -1
                _1334 = fdntrf[0]
                dirst_dmb[_1333] = _1334
                _1335 = _int(ng)
                _1336 = _1335 + -1
                _1337 = fdnsrf[0]
                dirst_dmbs[_1336] = _1337
                _1338 = s0[0]
                dirst_sun[0] = _1338
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_sun(_state, v):
    sundat_solara = _state.view(41984, '<f4')
    sundat_solarb = _state.view(47744, '<f4')
    a = _state.view(172728, '<f4')
    b = _state.view(172724, '<f4')
    D_18268 = _ZERO32
    i = 0
    p = _ZERO32
    __result_sun = _ZERO32
    D_8731 = _ZERO32
    p_9 = _ZERO32
    D_8733 = _ZERO32
    D_8734 = _ZERO32
    p_10 = _ZERO32
    p_11 = _ZERO32
    D_8737 = _ZERO32
    D_8738 = _ZERO32
    p_12 = _ZERO32
    p_13 = _ZERO32
    D_8741 = _ZERO32
    D_8742 = _ZERO32
    p_14 = _ZERO32
    p_15 = _ZERO32
    D_8745 = _ZERO32
    D_8746 = _ZERO32
    p_16 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = v[0]
                _pc = 1 if _1 < 0.0 else 2
                continue
            case 1:  # <D.18266>
                __result_sun = _f32(0.0)
                D_18268 = _f32(__result_sun)
                return D_18268
            case 2:  # <D.18267>
                _2 = v[0]
                _3 = _2 >= 0.0
                _4 = v[0]
                _5 = _4 < 1.0e+2
                _6 = _3 & _5
                _pc = 3 if _6 != 0 else 4
                continue
            case 3:  # <D.18269>
                D_8731 = _f32(v[0])
                b_265_7 = b[0]
                _8 = __builtin_powf(D_8731, b_265_7)
                a_266_9 = a[0]
                _10 = _8 * a_266_9
                __result_sun = _f32(_10)
                D_18268 = _f32(__result_sun)
                return D_18268
            case 4:  # <D.18270>
                _11 = v[0]
                _12 = _11 >= 1.0e+2
                _13 = v[0]
                _14 = _13 < 2.842e+4
                _15 = _12 & _14
                _pc = 5 if _15 != 0 else 6
                continue
            case 5:  # <D.18271>
                _16 = v[0]
                _17 = _div(_16, 2.0e+1)
                _18 = _int(_17)
                i = _int(_18 + 1)
                _19 = v[0]
                _20 = __builtin_fmodf(_19, 2.0e+1)
                p = _f32(_div(_20, 2.0e+1))
                p_9 = _f32(p)
                D_8733 = _f32(p_9)
                D_8734 = _f32(D_8733 * D_8733)
                p_10 = _f32(p)
                p_11 = _f32(p)
                D_8737 = _f32(p_11)
                D_8738 = _f32(D_8737 * D_8737)
                p_12 = _f32(p)
                _21 = D_8734 - 1.0e+0
                _22 = _21
                _23 = p_9 * _22
                _24 = i + 2
                _25 = _int(_24)
                _26 = _25 + -1
                _27 = sundat_solara[_26]
                _28 = _23 * _27
                _29 = p_10 * 3.0e+0
                _30 = p_10 + 1.0e+0
                _31 = _30
                _32 = _29 * _31
                _33 = p_10 - 2.0e+0
                _34 = _33
                _35 = _32 * _34
                _36 = i + 1
                _37 = _int(_36)
                _38 = _37 + -1
                _39 = sundat_solara[_38]
                _40 = _35 * _39
                _41 = _28 - _40
                _42 = D_8738 - 1.0e+0
                _43 = _42
                _44 = _43 * 3.0e+0
                _45 = p_11 - 2.0e+0
                _46 = _45
                _47 = _44 * _46
                _48 = _int(i)
                _49 = _48 + -1
                _50 = sundat_solara[_49]
                _51 = _47 * _50
                _52 = _41 + _51
                _53 = p_12 - 1.0e+0
                _54 = _53
                _55 = p_12 * _54
                _56 = p_12 - 2.0e+0
                _57 = _56
                _58 = _55 * _57
                _59 = i + -1
                _60 = _int(_59)
                _61 = _60 + -1
                _62 = sundat_solara[_61]
                _63 = _58 * _62
                _64 = _52 - _63
                _65 = _64
                _66 = _div(_65, 6.0e+0)
                __result_sun = _f32(_66)
                D_18268 = _f32(__result_sun)
                return D_18268
            case 6:  # <D.18272>
                _67 = v[0]
                _68 = _67 >= 2.842e+4
                _69 = v[0]
                _70 = _69 <= 5.747e+4
                _71 = _68 & _70
                _pc = 7 if _71 != 0 else 8
                continue
            case 7:  # <D.18273>
                _72 = v[0]
                _73 = _div(_72, 1.0e+1)
                _74 = _int(_73)
                i = _int(_74 + -2839)
                _75 = v[0]
                _76 = __builtin_fmodf(_75, 1.0e+1)
                p = _f32(_div(_76, 1.0e+1))
                p_13 = _f32(p)
                D_8741 = _f32(p_13)
                D_8742 = _f32(D_8741 * D_8741)
                p_14 = _f32(p)
                p_15 = _f32(p)
                D_8745 = _f32(p_15)
                D_8746 = _f32(D_8745 * D_8745)
                p_16 = _f32(p)
                _77 = D_8742 - 1.0e+0
                _78 = _77
                _79 = p_13 * _78
                _80 = i + 2
                _81 = _int(_80)
                _82 = _81 + -1
                _83 = sundat_solarb[_82]
                _84 = _79 * _83
                _85 = p_14 * 3.0e+0
                _86 = p_14 + 1.0e+0
                _87 = _86
                _88 = _85 * _87
                _89 = p_14 - 2.0e+0
                _90 = _89
                _91 = _88 * _90
                _92 = i + 1
                _93 = _int(_92)
                _94 = _93 + -1
                _95 = sundat_solarb[_94]
                _96 = _91 * _95
                _97 = _84 - _96
                _98 = D_8746 - 1.0e+0
                _99 = _98
                _100 = _99 * 3.0e+0
                _101 = p_15 - 2.0e+0
                _102 = _101
                _103 = _100 * _102
                _104 = _int(i)
                _105 = _104 + -1
                _106 = sundat_solarb[_105]
                _107 = _103 * _106
                _108 = _97 + _107
                _109 = p_16 - 1.0e+0
                _110 = _109
                _111 = p_16 * _110
                _112 = p_16 - 2.0e+0
                _113 = _112
                _114 = _111 * _113
                _115 = i + -1
                _116 = _int(_115)
                _117 = _116 + -1
                _118 = sundat_solarb[_117]
                _119 = _114 * _118
                _120 = _108 - _119
                _121 = _120
                _122 = _div(_121, 6.0e+0)
                __result_sun = _f32(_122)
                D_18268 = _f32(__result_sun)
                return D_18268
            case 8:  # <D.18274>
                _123 = v[0]
                _pc = 9 if _123 > 5.747e+4 else 10
                continue
            case 9:  # <D.18275>
                __result_sun = _f32(0.0)
                D_18268 = _f32(__result_sun)
                return D_18268
            case 10:  # L.241
                D_18268 = _f32(__result_sun)
                return D_18268
            case 11:  # __label_000900
                D_18268 = _f32(__result_sun)
                return D_18268
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_ssrad(_state, iph, ik, itzero, ipath, v, sumssr):
    __BLNK___tx = _state.view(265924, '<f4')
    sols_ah1 = _state.view(189472, '<f4')
    sols_arh = _state.view(189744, '<f4')
    sols_pa = _state.view(207152, '<f4')
    sols_pr = _state.view(207424, '<f4')
    srad_teb1 = _state.view(242976, '<f4')
    srad_teb2 = _state.view(242980, '<f4')
    srad_tasp1 = _state.view(242984, '<f4')
    srad_tasp2 = _state.view(242988, '<f4')
    srad_tmsp1 = _state.view(242992, '<f4')
    srad_tmsp2 = _state.view(242996, '<f4')
    srad_teb2sv = _state.view(243000, '<f4')
    srads_pmol1 = _state.view(231712, '<f4')
    srads_pmol2 = _state.view(231716, '<f4')
    srads_paer1 = _state.view(231720, '<f4')
    srads_paer2 = _state.view(231724, '<f4')
    dtasp = _ZERO32
    dtmsp = _ZERO32
    ikk = _zeros(1, '<i4')
    tx10 = _ZERO32
    tx6 = _ZERO32
    tx7 = _ZERO32
    tx9 = _ZERO32
    xa1 = _ZERO32
    xa2 = _ZERO32
    xm1 = _ZERO32
    xm2 = _ZERO32
    D_8909 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = itzero[0]
                _pc = 1 if _1 == 1 else 2
                continue
            case 1:  # <D.18279>
                _pc = -1
                continue
            case 2:  # L.242
                tx6 = _f32(__BLNK___tx[5])
                tx7 = _f32(__BLNK___tx[6])
                tx9 = _f32(__BLNK___tx[8])
                tx10 = _f32(__BLNK___tx[9])
                _2 = ipath[0]
                D_8909 = _int(_2 + -2)
                _pc = 3 if D_8909 <= 0 else 10
                continue
            case 3:  # <D.18281>
                _pc = 4 if D_8909 < 0 else 7
                continue
            case 4:  # __label_000010
                sumssr[0] = 0.0
                srad_tasp2[0] = 1.0e+0
                srad_tmsp2[0] = 1.0e+0
                srad_teb2[0] = tx9
                _3 = ik[0]
                _4 = _int(_3)
                _5 = _4 + -1
                _6 = sols_pr[_5]
                srads_pmol2[0] = _6
                _7 = ik[0]
                _8 = _int(_7)
                _9 = _8 + -1
                _10 = sols_pa[_9]
                srads_paer2[0] = _10
                _11 = iph[0]
                _pc = 5 if _11 == 2 else 6
                continue
            case 5:  # <D.18282>
                _12 = ik[0]
                _13 = _int(_12)
                _14 = _13 + -1
                _15 = sols_arh[_14:]
                _16 = ik[0]
                _17 = _int(_16)
                _18 = _17 + -1
                _19 = sols_pa[_18:]
                _20 = ik[0]
                _21 = _int(_20)
                _22 = _21 + -1
                _23 = sols_ah1[_22:]
                _ft_phasef(_state, v, ik, _23, _19, _15, srads_paer2)
                _pc = 6
                continue
            case 6:  # L.243
                return
            case 7:  # __label_000020
                srad_teb1[0] = tx9
                _24 = ik[0]
                _25 = _24 + 1
                _26 = _int(_25)
                _27 = _26 + -1
                _28 = sols_pr[_27]
                srads_pmol1[0] = _28
                _29 = ik[0]
                _30 = _29 + 1
                _31 = _int(_30)
                _32 = _31 + -1
                _33 = sols_pa[_32]
                srads_paer1[0] = _33
                _34 = ik[0]
                _35 = _34 + 1
                ikk[0] = _35
                _36 = iph[0]
                _pc = 8 if _36 == 2 else 9
                continue
            case 8:  # <D.18285>
                ikk_267_37 = ikk[0]
                _38 = _int(ikk_267_37)
                _39 = _38 + -1
                _40 = sols_arh[_39:]
                ikk_268_41 = ikk[0]
                _42 = _int(ikk_268_41)
                _43 = _42 + -1
                _44 = sols_pa[_43:]
                ikk_269_45 = ikk[0]
                _46 = _int(ikk_269_45)
                _47 = _46 + -1
                _48 = sols_ah1[_47:]
                _ft_phasef(_state, v, ikk, _48, _44, _40, srads_paer1)
                _pc = 9
                continue
            case 9:  # L.244
                return
            case 10:  # __label_000030
                _49 = _div(tx7, tx10)
                srad_tasp1[0] = _49
                srad_tmsp1[0] = tx6
                _50 = srad_tasp1[0]
                _51 = _50 == 0.0
                _52 = srad_tmsp1[0]
                _53 = _52 == 0.0
                _54 = _51 | _53
                _55 = srad_tmsp2[0]
                _56 = _55 == 0.0
                _57 = _54 | _56
                _58 = srad_tasp2[0]
                _59 = _58 == 0.0
                _60 = _57 | _59
                _pc = 11 if _60 != 0 else 12
                continue
            case 11:  # <D.18288>
                _pc = 13
                continue
            case 12:  # L.245
                _61 = srads_paer1[0]
                _62 = srad_teb1[0]
                _63 = _61 * _62
                _64 = srad_tasp1[0]
                xa1 = _f32(_div(_63, _64))
                _65 = srads_paer2[0]
                _66 = srad_teb2[0]
                _67 = _65 * _66
                _68 = srad_tasp2[0]
                xa2 = _f32(_div(_67, _68))
                _69 = srads_pmol1[0]
                _70 = srad_teb1[0]
                _71 = _69 * _70
                _72 = srad_tmsp1[0]
                xm1 = _f32(_div(_71, _72))
                _73 = srads_pmol2[0]
                _74 = srad_teb2[0]
                _75 = _73 * _74
                _76 = srad_tmsp2[0]
                xm2 = _f32(_div(_75, _76))
                _77 = srad_tasp2[0]
                _78 = srad_tasp1[0]
                dtasp = _f32(_77 - _78)
                _79 = srad_tmsp2[0]
                _80 = srad_tmsp1[0]
                dtmsp = _f32(_79 - _80)
                _81 = sumssr[0]
                _82 = xa1 + xa2
                _83 = _82
                _84 = dtasp * _83
                _85 = xm1 + xm2
                _86 = _85
                _87 = dtmsp * _86
                _88 = _84 + _87
                _89 = _88
                _90 = _89 * 5.0e-1
                _91 = _81 + _90
                sumssr[0] = _91
                _pc = 13
            case 13:  # __label_000050
                _92 = srad_tasp1[0]
                srad_tasp2[0] = _92
                _93 = srad_teb2[0]
                srad_teb2sv[0] = _93
                _94 = srad_tmsp1[0]
                srad_tmsp2[0] = _94
                _95 = srad_teb1[0]
                srad_teb2[0] = _95
                _96 = srads_paer1[0]
                srads_paer2[0] = _96
                _97 = srads_pmol1[0]
                srads_pmol2[0] = _97
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_phasef(_state, v, ik, alt, sangle, rh, phfa):
    aer_zz1 = _state.view(231880, '<f4')
    aer_zz2 = _state.view(231884, '<f4')
    card2_ihaze = _state.view(231744, '<i4')
    card2_ivulcn = _state.view(231752, '<i4')
    card2_icld = _state.view(231760, '<i4')
    card2d_altb = _state.view(214096, '<f4')
    cnstns_ca = _state.view(246164, '<f4')
    ang = _state.view(172864, '<f4')
    rhpts = _state.view(172848, '<f4')
    wave = _state.view(172736, '<f4')
    alam = _zeros(1, '<f4')
    cosang = _zeros(1, '<f4')
    i = 0
    i1 = 0
    iang1 = _zeros(1, '<i4')
    iang2 = _zeros(1, '<i4')
    irh = 0
    irhhi = 0
    irhlo = 0
    iwav1 = _zeros(1, '<i4')
    iwav2 = _zeros(1, '<i4')
    nn = _zeros(1, '<i4')
    nn0 = 0
    pf11 = _zeros(1, '<f4')
    pf12 = _zeros(1, '<f4')
    pf21 = _zeros(1, '<f4')
    pf22 = _zeros(1, '<f4')
    phfa1 = _zeros(1, '<f4')
    phfa2 = _zeros(1, '<f4')
    y = _zeros(1, '<f4')
    yang1 = _zeros(1, '<f4')
    yang2 = _zeros(1, '<f4')
    D_9109 = 0
    D_9135 = 0
    D_9144 = 0
    C_9160 = _array([2], '<i4')
    C_9170 = _array([2], '<i4')
    C_9171 = _array([2], '<i4')
    C_9173 = _array([2], '<i4')
    C_9176 = _array([2], '<i4')
    C_9180 = _array([1], '<i4')
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                phfa[0] = 0.0
                _1 = v[0]
                _2 = _div(1.0e+4, _1)
                alam[0] = _2
                _3 = v[0]
                _pc = 1 if _3 < 9.99999974737875163555145263671875e-6 else 2
                continue
            case 1:  # <D.18293>
                alam[0] = 1.0e+9
                _pc = 2
                continue
            case 2:  # L.246
                _4 = sangle[0]
                _5 = _4 < 0.0
                _6 = sangle[0]
                _7 = _6 > 1.8e+2
                _8 = _5 | _7
                _pc = 3 if _8 != 0 else 4
                continue
            case 3:  # <D.18296>
                _pc = 94
                continue
            case 4:  # L.247
                alam_270_9 = alam[0]
                _10 = wave[0]
                _11 = alam_270_9 - _10
                _12 = _11
                _pc = 5 if _12 < -9.999999974752427078783512115478515625e-7 else 6
                continue
            case 5:  # <D.18298>
                _pc = 95
                continue
            case 6:  # L.248
                _13 = wave[26]
                alam_271_14 = alam[0]
                _pc = 7 if _13 < alam_271_14 else 8
                continue
            case 7:  # <D.18300>
                _15 = sangle[0]
                _16 = cnstns_ca[0]
                _17 = _15 * _16
                _18 = __builtin_cosf(_17)
                cosang[0] = _18
                _ft_hengns(_state, aer_zz1, cosang, phfa)
                return
            case 8:  # L.249
                _19 = alt[0]
                _20 = card2d_altb[0]
                _pc = 9 if _19 > _20 else 10
                continue
            case 9:  # <D.18302>
                _pc = 41
                continue
            case 10:  # L.250
                _21 = card2_ihaze[0]
                _pc = 11 if _21 == 0 else 12
                continue
            case 11:  # <D.18304>
                _pc = 93
                continue
            case 12:  # L.251
                _22 = card2_ihaze[0]
                _pc = 13 if _22 == 10 else 14
                continue
            case 13:  # <D.18306>
                _23 = sangle[0]
                _24 = cnstns_ca[0]
                _25 = _23 * _24
                _26 = __builtin_cosf(_25)
                cosang[0] = _26
                _ft_hengns(_state, aer_zz1, cosang, phfa)
                return
            case 14:  # L.252
                _27 = card2_icld[0]
                _28 = _27 > 0
                _29 = card2_ihaze[0]
                _30 = _29 == 7
                _31 = _28 | _30
                _pc = 15 if _31 != 0 else 16
                continue
            case 15:  # <D.18308>
                _32 = sangle[0]
                _33 = cnstns_ca[0]
                _34 = _32 * _33
                _35 = __builtin_cosf(_34)
                cosang[0] = _35
                _ft_hengns(_state, aer_zz1, cosang, phfa)
                return
            case 16:  # L.253
                _36 = card2_ihaze[0]
                _pc = 17 if _36 > 7 else 18
                continue
            case 17:  # <D.18310>
                _pc = 36
                continue
            case 18:  # L.254
                i1 = _int(1)
                _pc = 19
            case 19:  # <D.18312>
                D_9109 = _int(i1 > 4)
                _pc = 25 if D_9109 != 0 else 20
                continue
            case 20:  # <D.18313>
                i = _int(i1)
                _37 = _int(i)
                _38 = _37 + -1
                _39 = rhpts[_38]
                _40 = rh[0]
                _pc = 21 if _39 == _40 else 22
                continue
            case 21:  # <D.18314>
                _pc = 26
                continue
            case 22:  # L.257
                _41 = _int(i)
                _42 = _41 + -1
                _43 = rhpts[_42]
                _44 = rh[0]
                _pc = 23 if _43 > _44 else 24
                continue
            case 23:  # <D.18316>
                _pc = 25
                continue
            case 24:  # L.255
                i1 = _int(i1 + 1)
                _pc = 19
                continue
            case 25:  # __label_000060
                irhlo = _int(i + -1)
                irhhi = _int(i)
                _pc = 27
                continue
            case 26:  # __label_000070
                irhlo = _int(i)
                irhhi = _int(i)
                _pc = 27
            case 27:  # __label_000080
                _45 = card2_ihaze[0]
                _46 = _45 == 1
                _47 = card2_ihaze[0]
                _48 = _47 == 2
                _49 = _46 | _48
                _pc = 28 if _49 != 0 else 29
                continue
            case 28:  # <D.18318>
                nn0 = _int(0)
                _pc = 29
                continue
            case 29:  # L.259
                _50 = card2_ihaze[0]
                _51 = _50 == 3
                _52 = card2_ihaze[0]
                _53 = _52 == 4
                _54 = _51 | _53
                _pc = 30 if _54 != 0 else 31
                continue
            case 30:  # <D.18321>
                nn0 = _int(4)
                _pc = 31
                continue
            case 31:  # L.260
                _55 = card2_ihaze[0]
                _pc = 32 if _55 == 5 else 33
                continue
            case 32:  # <D.18324>
                nn0 = _int(8)
                _pc = 33
                continue
            case 33:  # L.261
                _56 = card2_ihaze[0]
                _pc = 34 if _56 == 6 else 35
                continue
            case 34:  # <D.18327>
                nn0 = _int(16)
                _pc = 35
                continue
            case 35:  # L.262
                _57 = nn0 + irhlo
                nn[0] = _57
                _pc = 58
                continue
            case 36:  # __label_000090
                _58 = card2_ihaze[0]
                _pc = 37 if _58 == 8 else 38
                continue
            case 37:  # <D.18330>
                nn[0] = 24
                _pc = 38
                continue
            case 38:  # L.263
                _59 = card2_ihaze[0]
                _pc = 39 if _59 == 9 else 40
                continue
            case 39:  # <D.18333>
                nn[0] = 25
                _pc = 40
                continue
            case 40:  # L.264
                _pc = 58
                continue
            case 41:  # __label_000095
                _60 = alt[0]
                _61 = card2d_altb[1]
                _pc = 42 if _60 > _61 else 43
                continue
            case 42:  # <D.18336>
                _pc = 46
                continue
            case 43:  # L.265
                _62 = card2_icld[0]
                _63 = _62 > 0
                _64 = card2_ihaze[0]
                _65 = _64 == 7
                _66 = _63 | _65
                _pc = 44 if _66 != 0 else 45
                continue
            case 44:  # <D.18338>
                _67 = sangle[0]
                _68 = cnstns_ca[0]
                _69 = _67 * _68
                _70 = __builtin_cosf(_69)
                cosang[0] = _70
                _ft_hengns(_state, aer_zz2, cosang, phfa)
                return
            case 45:  # L.266
                nn[0] = 18
                _pc = 58
                continue
            case 46:  # __label_000110
                _71 = alt[0]
                _72 = card2d_altb[2]
                _pc = 47 if _71 > _72 else 48
                continue
            case 47:  # <D.18340>
                _pc = 57
                continue
            case 48:  # L.267
                _73 = card2_ivulcn[0]
                _74 = _73 == 0
                _75 = card2_ivulcn[0]
                _76 = _75 == 1
                _77 = _74 | _76
                _pc = 49 if _77 != 0 else 50
                continue
            case 49:  # <D.18342>
                nn[0] = 21
                _pc = 50
                continue
            case 50:  # L.268
                _78 = card2_ivulcn[0]
                _79 = _78 == 2
                _80 = card2_ivulcn[0]
                _81 = _80 == 4
                _82 = _79 | _81
                _pc = 51 if _82 != 0 else 52
                continue
            case 51:  # <D.18345>
                nn[0] = 22
                _pc = 52
                continue
            case 52:  # L.269
                _83 = card2_ivulcn[0]
                _84 = _83 == 3
                _85 = card2_ivulcn[0]
                _86 = _85 == 5
                _87 = _84 | _86
                _88 = card2_ivulcn[0]
                _89 = _88 == 8
                _90 = _87 | _89
                _pc = 53 if _90 != 0 else 54
                continue
            case 53:  # <D.18348>
                nn[0] = 23
                _pc = 54
                continue
            case 54:  # L.270
                _91 = card2_ivulcn[0]
                _92 = _91 == 6
                _93 = card2_ivulcn[0]
                _94 = _93 == 7
                _95 = _92 | _94
                _pc = 55 if _95 != 0 else 56
                continue
            case 55:  # <D.18351>
                nn[0] = 21
                _pc = 56
                continue
            case 56:  # L.271
                _pc = 58
                continue
            case 57:  # __label_000120
                nn[0] = 26
                _pc = 58
            case 58:  # __label_000130
                irh = _int(0)
                _pc = 59
            case 59:  # __label_000140
                i1 = _int(1)
                _pc = 60
            case 60:  # <D.18354>
                D_9135 = _int(i1 > 34)
                _pc = 66 if D_9135 != 0 else 61
                continue
            case 61:  # <D.18355>
                i = _int(i1)
                _96 = _int(i)
                _97 = _96 + -1
                _98 = ang[_97]
                _99 = sangle[0]
                _pc = 62 if _98 == _99 else 63
                continue
            case 62:  # <D.18356>
                _pc = 67
                continue
            case 63:  # L.274
                _100 = _int(i)
                _101 = _100 + -1
                _102 = ang[_101]
                _103 = sangle[0]
                _pc = 64 if _102 > _103 else 65
                continue
            case 64:  # <D.18358>
                _pc = 66
                continue
            case 65:  # L.272
                i1 = _int(i1 + 1)
                _pc = 60
                continue
            case 66:  # __label_000220
                _104 = i + -1
                iang1[0] = _104
                iang2[0] = i
                _pc = 68
                continue
            case 67:  # __label_000230
                iang1[0] = i
                iang2[0] = i
                _pc = 68
            case 68:  # __label_000240
                i1 = _int(1)
                _pc = 69
            case 69:  # <D.18360>
                D_9144 = _int(i1 > 27)
                _pc = 75 if D_9144 != 0 else 70
                continue
            case 70:  # <D.18361>
                i = _int(i1)
                _105 = _int(i)
                _106 = _105 + -1
                _107 = wave[_106]
                alam_272_108 = alam[0]
                _pc = 71 if _107 == alam_272_108 else 72
                continue
            case 71:  # <D.18362>
                _pc = 76
                continue
            case 72:  # L.278
                _109 = _int(i)
                _110 = _109 + -1
                _111 = wave[_110]
                alam_273_112 = alam[0]
                _pc = 73 if _111 > alam_273_112 else 74
                continue
            case 73:  # <D.18364>
                _pc = 75
                continue
            case 74:  # L.276
                i1 = _int(i1 + 1)
                _pc = 69
                continue
            case 75:  # __label_000260
                _113 = i + -1
                iwav1[0] = _113
                iwav2[0] = i
                _pc = 77
                continue
            case 76:  # __label_000270
                iwav1[0] = i
                iwav2[0] = i
                _pc = 77
            case 77:  # __label_000280
                _114 = _ft_pf(_state, nn, iwav1, iang1)
                pf11[0] = _114
                _115 = _ft_pf(_state, nn, iwav2, iang1)
                pf21[0] = _115
                _116 = _ft_pf(_state, nn, iwav1, iang2)
                pf12[0] = _116
                _117 = _ft_pf(_state, nn, iwav2, iang2)
                pf22[0] = _117
                iwav1_274_118 = iwav1[0]
                iwav2_275_119 = iwav2[0]
                _pc = 78 if iwav1_274_118 == iwav2_275_119 else 79
                continue
            case 78:  # <D.18366>
                _pc = 83
                continue
            case 79:  # L.280
                iang1_276_120 = iang1[0]
                iang2_277_121 = iang2[0]
                _pc = 80 if iang1_276_120 == iang2_277_121 else 81
                continue
            case 80:  # <D.18368>
                _pc = 82
                continue
            case 81:  # L.281
                iwav2_278_122 = iwav2[0]
                _123 = _int(iwav2_278_122)
                _124 = _123 + -1
                _125 = wave[_124:]
                iwav1_279_126 = iwav1[0]
                _127 = _int(iwav1_279_126)
                _128 = _127 + -1
                _129 = wave[_128:]
                _ft_interp(_state, C_9160, alam, _129, _125, yang1, pf11, pf21)
                iwav2_280_130 = iwav2[0]
                _131 = _int(iwav2_280_130)
                _132 = _131 + -1
                _133 = wave[_132:]
                iwav1_281_134 = iwav1[0]
                _135 = _int(iwav1_281_134)
                _136 = _135 + -1
                _137 = wave[_136:]
                _ft_interp(_state, C_9170, alam, _137, _133, yang2, pf12, pf22)
                iang2_282_138 = iang2[0]
                _139 = _int(iang2_282_138)
                _140 = _139 + -1
                _141 = ang[_140:]
                iang1_283_142 = iang1[0]
                _143 = _int(iang1_283_142)
                _144 = _143 + -1
                _145 = ang[_144:]
                _ft_interp(_state, C_9171, sangle, _145, _141, y, yang1, yang2)
                _pc = 87
                continue
            case 82:  # __label_000290
                iwav2_284_146 = iwav2[0]
                _147 = _int(iwav2_284_146)
                _148 = _147 + -1
                _149 = wave[_148:]
                iwav1_285_150 = iwav1[0]
                _151 = _int(iwav1_285_150)
                _152 = _151 + -1
                _153 = wave[_152:]
                _ft_interp(_state, C_9173, alam, _153, _149, y, pf11, pf21)
                _pc = 87
                continue
            case 83:  # __label_000310
                iang1_286_154 = iang1[0]
                iang2_287_155 = iang2[0]
                _pc = 84 if iang1_286_154 == iang2_287_155 else 85
                continue
            case 84:  # <D.18370>
                _pc = 86
                continue
            case 85:  # L.282
                iang2_288_156 = iang2[0]
                _157 = _int(iang2_288_156)
                _158 = _157 + -1
                _159 = ang[_158:]
                iang1_289_160 = iang1[0]
                _161 = _int(iang1_289_160)
                _162 = _161 + -1
                _163 = ang[_162:]
                _ft_interp(_state, C_9176, sangle, _163, _159, y, pf11, pf12)
                _pc = 87
                continue
            case 86:  # __label_000320
                _164 = _ft_pf(_state, nn, iwav1, iang1)
                y[0] = _164
                _pc = 87
            case 87:  # __label_000330
                y_290_165 = y[0]
                phfa[0] = y_290_165
                _166 = alt[0]
                _167 = card2d_altb[0]
                _168 = _166 > _167
                nn_291_169 = nn[0]
                _170 = nn_291_169 > 16
                _171 = _168 | _170
                _172 = irhlo == irhhi
                _173 = _171 | _172
                _pc = 88 if _173 != 0 else 89
                continue
            case 88:  # <D.18372>
                _pc = 93
                continue
            case 89:  # L.283
                _pc = 90 if irh == 1 else 91
                continue
            case 90:  # <D.18374>
                _pc = 92
                continue
            case 91:  # L.284
                _174 = nn0 + irhhi
                nn[0] = _174
                _175 = phfa[0]
                phfa1[0] = _175
                irh = _int(1)
                _pc = 77
                continue
            case 92:  # __label_000340
                _176 = phfa[0]
                phfa2[0] = _176
                _177 = _int(irhhi)
                _178 = _177 + -1
                _179 = rhpts[_178:]
                _180 = _int(irhlo)
                _181 = _180 + -1
                _182 = rhpts[_181:]
                _ft_interp(_state, C_9180, rh, _182, _179, phfa, phfa1, phfa2)
                _pc = 93
            case 93:  # __label_000400
                return
            case 94:  # __label_000901
                _gfortran_stop_string(0, 0, 0)
                _pc = 95
            case 95:  # __label_000911
                _gfortran_stop_string(0, 0, 0)
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_interp(_state, intype, x, x1, x2, f, f1, f2):
    a = _ZERO32
    a1 = _ZERO32
    a2 = _ZERO32
    itype = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                itype = _int(intype[0])
                _1 = f1[0]
                _2 = _1 <= 0.0
                _3 = f2[0]
                _4 = _3 <= 0.0
                _5 = _2 | _4
                _pc = 1 if _5 != 0 else 2
                continue
            case 1:  # <D.18378>
                itype = _int(1)
                _pc = 2
                continue
            case 2:  # L.285
                _pc = 3 if itype == 2 else 4
                continue
            case 3:  # <D.18381>
                _pc = 5
                continue
            case 4:  # L.286
                _6 = f1[0]
                _7 = x[0]
                _8 = x1[0]
                _9 = _7 - _8
                _10 = _9
                _11 = f2[0]
                _12 = f1[0]
                _13 = _11 - _12
                _14 = _13
                _15 = _10 * _14
                _16 = x2[0]
                _17 = x1[0]
                _18 = _16 - _17
                _19 = _18
                _20 = _div(_15, _19)
                _21 = _6 + _20
                f[0] = _21
                return
            case 5:  # __label_000100
                _22 = f1[0]
                a1 = _f32(__builtin_logf(_22))
                _23 = f2[0]
                a2 = _f32(__builtin_logf(_23))
                _24 = x[0]
                _25 = x1[0]
                _26 = _24 - _25
                _27 = _26
                _28 = a2 - a1
                _29 = _28
                _30 = _27 * _29
                _31 = x2[0]
                _32 = x1[0]
                _33 = _31 - _32
                _34 = _33
                _35 = _div(_30, _34)
                a = _f32(a1 + _35)
                _36 = __builtin_expf(a)
                f[0] = _36
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_pf(_state, nn, i, j):
    mnmphs_mnum = _state.view(104928, '<i4')
    mnmphs_phsfnc = _state.view(107736, '<f4')
    D_18384 = _ZERO32
    m = 0
    __result_pf = _ZERO32
    _1 = nn[0]
    _2 = _int(_1)
    _3 = _2 * 27
    _4 = i[0]
    _5 = _int(_4)
    _6 = _3 + _5
    _7 = _6 + -28
    m = _int(mnmphs_mnum[_7])
    _8 = _int(m)
    _9 = _8 * 34
    _10 = j[0]
    _11 = _int(_10)
    _12 = _9 + _11
    _13 = _12 + -35
    _14 = mnmphs_phsfnc[_13]
    __result_pf = _f32(_14)
    D_18384 = _f32(__result_pf)
    return D_18384


def _ft_hengns(_state, zz, sangle, phfa):
    cnstns_pi = _state.view(246160, '<f4')
    gg_17 = _ZERO32
    x_18 = _ZERO32
    D_9214 = _ZERO32
    D_9215 = _ZERO32
    D_9216 = _ZERO32
    D_9217 = _ZERO32
    D_9218 = _ZERO32
    gg_17 = _f32(zz[0])
    x_18 = _f32(sangle[0])
    D_9214 = _f32(gg_17)
    D_9215 = _f32(D_9214 * D_9214)
    D_9216 = _f32(gg_17)
    D_9217 = _f32(D_9216 * D_9216)
    _1 = D_9217 + 1.0e+0
    _2 = gg_17 * 2.0e+0
    _3 = x_18 * _2
    _4 = _1 - _3
    D_9218 = _f32(_4)
    _5 = 1.0e+0 - D_9215
    _6 = _5
    _7 = cnstns_pi[0]
    _8 = _7 * 4.0e+0
    _9 = __builtin_powf(D_9218, 1.5e+0)
    _10 = _8 * _9
    _11 = _10
    _12 = _div(_6, _11)
    phfa[0] = _12


def _ft_dbltx(_state, w, cprime, qa):
    D_18389 = _ZERO32
    qaws = _ZERO32
    ws = _ZERO32
    __result_dbltx = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                __result_dbltx = _f32(1.0e+0)
                _1 = w[0]
                _pc = 1 if _1 < 9.9999996826552253889678874634872052240552875446155667305e-21 else 2
                continue
            case 1:  # <D.18387>
                D_18389 = _f32(__result_dbltx)
                return D_18389
            case 2:  # L.287
                _2 = cprime[0]
                _pc = 3 if _2 < -2.0e+1 else 4
                continue
            case 3:  # <D.18390>
                D_18389 = _f32(__result_dbltx)
                return D_18389
            case 4:  # L.288
                _3 = w[0]
                _4 = __builtin_log10f(_3)
                _5 = cprime[0]
                ws = _f32(_4 + _5)
                _6 = qa[0]
                qaws = _f32(ws * _6)
                _pc = 5 if qaws < 2.0e+0 else 6
                continue
            case 5:  # <D.18392>
                _pc = 7
                continue
            case 6:  # L.289
                __result_dbltx = _f32(0.0)
                D_18389 = _f32(__result_dbltx)
                return D_18389
            case 7:  # __label_000100
                _pc = 8 if qaws > -6.0e+0 else 9
                continue
            case 8:  # <D.18394>
                _pc = 10
                continue
            case 9:  # L.290
                __result_dbltx = _f32(1.0e+0)
                D_18389 = _f32(__result_dbltx)
                return D_18389
            case 10:  # __label_000200
                _7 = __builtin_powf(1.0e+1, qaws)
                _8 = -_7
                _9 = __builtin_expf(_8)
                __result_dbltx = _f32(_9)
                D_18389 = _f32(__result_dbltx)
                return D_18389
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_rnscat(_state, v, r, tt, phase, dist, ik, cssa, asymr, ient):
    c7500 = _state.view(173092, '<f4')
    cmt0 = _state.view(173088, '<f4')
    fr = _state.view(173024, '<f4')
    g0 = _state.view(188280, '<f4')
    g7500 = _state.view(173096, '<f4')
    maxi = _state.view(173084, '<i4')
    nf = _state.view(173060, '<i4')
    nsc = _state.view(173080, '<i4')
    nt = _state.view(173076, '<i4')
    temp = _state.view(173064, '<f4')
    tk = _state.view(173000, '<f4')
    aamt = _ZERO32
    al = _ZERO32
    am = _ZERO32
    atot = _ZERO32
    camt = _ZERO32
    cl = _ZERO32
    cm = _ZERO32
    ctot = _ZERO32
    f = _zeros(1, '<f4')
    fdif = _ZERO32
    fl = _ZERO32
    fm = _ZERO32
    fsav = _ZERO32
    ftot = _ZERO32
    i = _zeros(1, '<i4')
    v_int = 0
    isc = 0
    j = _zeros(1, '<i4')
    k = _zeros(1, '<i4')
    ki = 0
    nopr = 0
    rsav = _ZERO32
    s1 = _ZERO32
    s2 = _ZERO32
    s3 = _ZERO32
    s4 = _ZERO32
    sc = _zeros(12, '<f4')
    sf = _zeros(1, '<f4')
    st = _zeros(1, '<f4')
    t = _zeros(1, '<f4')
    tsav = _ZERO32
    wc = _zeros(1, '<f4')
    D_9292 = 0
    D_9295 = 0
    D_9298 = _ZERO32
    D_9299 = _ZERO32
    D_9301 = 0
    D_9304 = 0
    D_9312 = _zeros(1, '<i4')
    D_9313 = _zeros(1, '<i4')
    D_9314 = _zeros(1, '<i4')
    D_9315 = _zeros(1, '<i4')
    D_9317 = 0
    D_9320 = 0
    D_9322 = _zeros(1, '<i4')
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                nopr = _int(0)
                _1 = ik[0]
                _pc = 1 if _1 == 1 else 2
                continue
            case 1:  # <D.18398>
                nopr = _int(1)
                _pc = 2
                continue
            case 2:  # L.291
                _2 = ient[0]
                _pc = 3 if _2 > 1 else 4
                continue
            case 3:  # <D.18401>
                nopr = _int(0)
                _pc = 4
                continue
            case 4:  # L.292
                _3 = v[0]
                _4 = _3 * 2.99792499542236328125e+1
                f[0] = _4
                fsav = _f32(f[0])
                rsav = _f32(r[0])
                tsav = _f32(t[0])
                v_int = _int(0)
                _5 = tt[0]
                tk_292_6 = tk[0]
                _7 = _5 - tk_292_6
                t[0] = _7
                _8 = fr[0]
                f_293_9 = f[0]
                _pc = 5 if _8 > f_293_9 else 6
                continue
            case 5:  # <D.18404>
                fl = _f32(0.0)
                fm = _f32(fr[0])
                v_int = _int(1)
                _pc = 6
                continue
            case 6:  # L.293
                nf_294_10 = nf[0]
                _11 = _int(nf_294_10)
                _12 = _11 + -1
                _13 = fr[_12]
                f_295_14 = f[0]
                _pc = 7 if _13 < f_295_14 else 8
                continue
            case 7:  # <D.18407>
                nf_296_15 = nf[0]
                _16 = _int(nf_296_15)
                _17 = _16 + -1
                fl = _f32(fr[_17])
                fm = _f32(7.5e+3)
                v_int = _int(2)
                _pc = 8
                continue
            case 8:  # L.294
                _18 = temp[0]
                t_297_19 = t[0]
                _pc = 9 if _18 > t_297_19 else 10
                continue
            case 9:  # <D.18410>
                _20 = temp[0]
                t[0] = _20
                _pc = 10
                continue
            case 10:  # L.295
                _21 = temp[2]
                t_298_22 = t[0]
                _pc = 11 if _21 < t_298_22 else 12
                continue
            case 11:  # <D.18413>
                _23 = temp[2]
                t[0] = _23
                _pc = 12
                continue
            case 12:  # L.296
                _24 = r[0]
                _pc = 13 if _24 > 5.0e+1 else 14
                continue
            case 13:  # <D.18416>
                r[0] = 5.0e+1
                _pc = 14
                continue
            case 14:  # L.297
                ki = _int(1)
                _pc = 15
            case 15:  # __label_000010
                _25 = phase[0]
                _26 = dist[0]
                _27 = _26 * 2
                _28 = _25 + _27
                j[0] = _28
                _ft_bs(_state, j, t, temp, nt, st)
                _ft_bs(_state, k, f, fr, nf, sf)
                D_9292 = _int(nsc[0])
                i[0] = 1
                _pc = 16
            case 16:  # <D.18419>
                i_299_29 = i[0]
                D_9295 = _int(D_9292 < i_299_29)
                _pc = 19 if D_9295 != 0 else 17
                continue
            case 17:  # <D.18420>
                i_300_30 = i[0]
                _31 = _int(i_300_30)
                _32 = _31 * 3
                _33 = _int(ki)
                _34 = _32 + _33
                _35 = _34 + -4
                sc[_35] = 0.0
                _pc = 18
            case 18:  # L.298
                i_301_36 = i[0]
                _37 = i_301_36 + 1
                i[0] = _37
                _pc = 16
                continue
            case 19:  # L.299
                _38 = _int(ki)
                _39 = _38 + 5
                sc[_39] = 1.0e+0
                _40 = dist[0]
                _pc = 20 if _40 == 1 else 21
                continue
            case 20:  # <D.18421>
                D_9298 = _f32(r[0])
                _41 = __builtin_powf(D_9298, 8.39999973773956298828125e-1)
                _42 = _41 * 8.88999998569488525390625e-2
                wc[0] = _42
                _pc = 22
                continue
            case 21:  # <D.18422>
                D_9299 = _f32(r[0])
                _43 = __builtin_powf(D_9299, 8.46000015735626220703125e-1)
                _44 = _43 * 6.70000016689300537109375e-2
                wc[0] = _44
                _pc = 22
            case 22:  # L.300
                j_302_45 = j[0]
                _pc = 23 if j_302_45 <= 2 else 31
                continue
            case 23:  # <D.18424>
                sf_303_46 = sf[0]
                _47 = 1.0e+0 - sf_303_46
                _48 = _47
                st_304_49 = st[0]
                _50 = 1.0e+0 - st_304_49
                _51 = _50
                s1 = _f32(_48 * _51)
                sf_305_52 = sf[0]
                _53 = 1.0e+0 - sf_305_52
                _54 = _53
                st_306_55 = st[0]
                s2 = _f32(_54 * st_306_55)
                st_307_56 = st[0]
                _57 = 1.0e+0 - st_307_56
                _58 = _57
                sf_308_59 = sf[0]
                s3 = _f32(_58 * sf_308_59)
                sf_309_60 = sf[0]
                st_310_61 = st[0]
                s4 = _f32(sf_309_60 * st_310_61)
                D_9301 = _int(maxi[0])
                i[0] = 1
                _pc = 24
            case 24:  # <D.18426>
                i_311_62 = i[0]
                D_9304 = _int(D_9301 < i_311_62)
                _pc = 30 if D_9304 != 0 else 25
                continue
            case 25:  # <D.18427>
                i_312_63 = i[0]
                _pc = 26 if i_312_63 <= 2 else 27
                continue
            case 26:  # <D.18428>
                isc = _int(i[0])
                _pc = 28
                continue
            case 27:  # <D.18429>
                i_313_64 = i[0]
                isc = _int(i_313_64 + 1)
                _pc = 28
            case 28:  # L.304
                j_314_65 = j[0]
                _66 = j_314_65 + 1
                D_9312[0] = _66
                k_315_67 = k[0]
                _68 = k_315_67 + 1
                D_9313[0] = _68
                j_316_69 = j[0]
                _70 = j_316_69 + 1
                D_9314[0] = _70
                k_317_71 = k[0]
                _72 = k_317_71 + 1
                D_9315[0] = _72
                _73 = _ft_tab(_state, i, j, k, wc)
                _74 = s1 * _73
                _75 = _ft_tab(_state, i, D_9312, k, wc)
                _76 = s2 * _75
                _77 = _74 + _76
                _78 = _ft_tab(_state, i, j, D_9313, wc)
                _79 = s3 * _78
                _80 = _77 + _79
                _81 = _ft_tab(_state, i, D_9314, D_9315, wc)
                _82 = s4 * _81
                _83 = _int(isc)
                _84 = _83 * 3
                _85 = _int(ki)
                _86 = _84 + _85
                _87 = _86 + -4
                _88 = _80 + _82
                sc[_87] = _88
                _pc = 29
            case 29:  # L.302
                i_318_89 = i[0]
                _90 = i_318_89 + 1
                i[0] = _90
                _pc = 24
                continue
            case 30:  # L.303
                _pc = 38
                continue
            case 31:  # <D.18425>
                sf_319_91 = sf[0]
                s1 = _f32(1.0e+0 - sf_319_91)
                s2 = _f32(sf[0])
                D_9317 = _int(maxi[0])
                i[0] = 1
                _pc = 32
            case 32:  # <D.18432>
                i_320_92 = i[0]
                D_9320 = _int(D_9317 < i_320_92)
                _pc = 38 if D_9320 != 0 else 33
                continue
            case 33:  # <D.18433>
                i_321_93 = i[0]
                _pc = 34 if i_321_93 <= 2 else 35
                continue
            case 34:  # <D.18434>
                isc = _int(i[0])
                _pc = 36
                continue
            case 35:  # <D.18435>
                i_322_94 = i[0]
                isc = _int(i_322_94 + 1)
                _pc = 36
            case 36:  # L.307
                k_323_95 = k[0]
                _96 = k_323_95 + 1
                D_9322[0] = _96
                _97 = _ft_tab(_state, i, j, k, wc)
                _98 = s1 * _97
                _99 = _ft_tab(_state, i, j, D_9322, wc)
                _100 = s2 * _99
                _101 = _int(isc)
                _102 = _101 * 3
                _103 = _int(ki)
                _104 = _102 + _103
                _105 = _104 + -4
                _106 = _98 + _100
                sc[_105] = _106
                _pc = 37
            case 37:  # L.305
                i_324_107 = i[0]
                _108 = i_324_107 + 1
                i[0] = _108
                _pc = 32
                continue
            case 38:  # L.301
                f[0] = fsav
                _pc = 39 if v_int == 3 else 40
                continue
            case 39:  # <D.18437>
                _pc = 51
                continue
            case 40:  # L.308
                _pc = 41 if v_int == 4 else 42
                continue
            case 41:  # <D.18439>
                _pc = 54
                continue
            case 42:  # L.309
                _pc = 43 if v_int == 0 else 46
                continue
            case 43:  # <D.18441>
                _109 = _int(ki)
                _110 = _109 + -1
                _111 = sc[_110]
                _112 = _int(ki)
                _113 = _112 + 2
                _114 = sc[_113]
                _115 = _div(_111, _114)
                cssa[0] = _115
                _116 = cssa[0]
                _pc = 44 if _116 > 1.0e+0 else 45
                continue
            case 44:  # <D.18443>
                cssa[0] = 1.0e+0
                _pc = 45
                continue
            case 45:  # L.311
                _117 = _int(ki)
                _118 = _117 + 8
                _119 = sc[_118]
                _120 = _div(_119, 3.0e+0)
                asymr[0] = _120
                f[0] = fsav
                r[0] = rsav
                t[0] = tsav
                return
            case 46:  # L.310
                _pc = 47 if v_int == 1 else 48
                continue
            case 47:  # <D.18446>
                v_int = _int(3)
                f[0] = fm
                ki = _int(2)
                _pc = 48
                continue
            case 48:  # L.312
                _pc = 49 if v_int == 2 else 50
                continue
            case 49:  # <D.18449>
                v_int = _int(4)
                f[0] = fl
                ki = _int(3)
                _pc = 50
                continue
            case 50:  # L.313
                _pc = 15
                continue
            case 51:  # __label_000020
                f_325_121 = f[0]
                fdif = _f32(fm - f_325_121)
                ftot = _f32(fm - fl)
                _122 = _int(ki)
                _123 = _122 + -1
                _124 = sc[_123]
                _125 = _int(ki)
                _126 = _125 + 2
                _127 = sc[_126]
                cm = _f32(_div(_124, _127))
                _pc = 52 if cm > 1.0e+0 else 53
                continue
            case 52:  # <D.18452>
                cm = _f32(1.0e+0)
                _pc = 53
                continue
            case 53:  # L.314
                cl = _f32(cmt0[0])
                _128 = _int(ki)
                _129 = _128 + 8
                _130 = sc[_129]
                am = _f32(_div(_130, 3.0e+0))
                al = _f32(g0[0])
                _pc = 57
                continue
            case 54:  # __label_000030
                f_326_131 = f[0]
                fdif = _f32(fm - f_326_131)
                ftot = _f32(fm - fl)
                cm = _f32(c7500[0])
                _132 = _int(ki)
                _133 = _132 + -1
                _134 = sc[_133]
                _135 = _int(ki)
                _136 = _135 + 2
                _137 = sc[_136]
                cl = _f32(_div(_134, _137))
                _pc = 55 if cl > 1.0e+0 else 56
                continue
            case 55:  # <D.18455>
                cl = _f32(1.0e+0)
                _pc = 56
                continue
            case 56:  # L.315
                am = _f32(g7500[0])
                _138 = _int(ki)
                _139 = _138 + 8
                _140 = sc[_139]
                al = _f32(_div(_140, 3.0e+0))
                _pc = 57
            case 57:  # __label_000040
                ctot = _f32(cm - cl)
                _141 = fdif * ctot
                camt = _f32(_div(_141, ftot))
                _142 = cm - camt
                cssa[0] = _142
                atot = _f32(am - al)
                _143 = fdif * atot
                aamt = _f32(_div(_143, ftot))
                _144 = am - aamt
                asymr[0] = _144
                f[0] = fsav
                r[0] = rsav
                t[0] = tsav
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_tab(_state, i, j, k, wc):
    a = _state.view(173344, '<f4')
    a1 = _state.view(177248, '<f4')
    a2 = _state.view(177312, '<f4')
    alpha = _state.view(175296, '<f4')
    alpha1 = _state.view(177280, '<f4')
    maxi = _state.view(173120, '<i4')
    D_18463 = _ZERO32
    l = 0
    __result_tab = _ZERO32
    D_9354 = _ZERO32
    D_9355 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = i[0]
                _2 = k[0]
                _3 = _int(_2)
                _4 = _3 * 6
                _5 = j[0]
                _6 = _int(_5)
                _7 = _4 + _6
                _8 = _7 + -7
                _9 = maxi[_8]
                _pc = 1 if _1 > _9 else 2
                continue
            case 1:  # <D.18461>
                __result_tab = _f32(0.0)
                D_18463 = _f32(__result_tab)
                return D_18463
            case 2:  # L.316
                _10 = k[0]
                _11 = _int(_10)
                _12 = _11 * 54
                _13 = j[0]
                _14 = _int(_13)
                _15 = _14 * 9
                _16 = _12 + _15
                _17 = i[0]
                _18 = _int(_17)
                _19 = _16 + _18
                _20 = _19 + -64
                _21 = a[_20]
                _22 = abs(_21)
                _pc = 3 if _22 > 9.99999993922529029077850282192230224609375e-9 else 4
                continue
            case 3:  # <D.18464>
                D_9354 = _f32(wc[0])
                _23 = k[0]
                _24 = _int(_23)
                _25 = _24 * 54
                _26 = j[0]
                _27 = _int(_26)
                _28 = _27 * 9
                _29 = _25 + _28
                _30 = i[0]
                _31 = _int(_30)
                _32 = _29 + _31
                _33 = _32 + -64
                _34 = a[_33]
                _35 = k[0]
                _36 = _int(_35)
                _37 = _36 * 54
                _38 = j[0]
                _39 = _int(_38)
                _40 = _39 * 9
                _41 = _37 + _40
                _42 = i[0]
                _43 = _int(_42)
                _44 = _41 + _43
                _45 = _44 + -64
                _46 = alpha[_45]
                _47 = __builtin_powf(D_9354, _46)
                _48 = _34 * _47
                __result_tab = _f32(_48)
                _pc = 5
                continue
            case 4:  # <D.18465>
                _49 = k[0]
                _50 = _int(_49)
                _51 = _50 * 54
                _52 = j[0]
                _53 = _int(_52)
                _54 = _53 * 9
                _55 = _51 + _54
                _56 = i[0]
                _57 = _int(_56)
                _58 = _55 + _57
                _59 = _58 + -64
                _60 = alpha[_59]
                l = _int(_int(_60))
                D_9355 = _f32(wc[0])
                _61 = _int(l)
                _62 = _61 + -1
                _63 = a1[_62]
                _64 = _int(l)
                _65 = _64 + -1
                _66 = alpha1[_65]
                _67 = __builtin_powf(D_9355, _66)
                _68 = _63 * _67
                _69 = _int(l)
                _70 = _69 + -1
                _71 = a2[_70]
                _72 = wc[0]
                _73 = _71 * _72
                _74 = _68 + _73
                __result_tab = _f32(_74)
                _pc = 5
            case 5:  # L.317
                D_18463 = _f32(__result_tab)
                return D_18463
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_bs(_state, i, a, b, n, s):
    j = 0
    m = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                i[0] = 1
                j = _int(n[0])
                _pc = 1
            case 1:  # __label_000010
                _1 = i[0]
                _2 = j + _1
                m = _int(_div(_2, 2))
                _3 = a[0]
                _4 = _int(m)
                _5 = _4 + -1
                _6 = b[_5]
                _pc = 2 if _3 <= _6 else 3
                continue
            case 2:  # <D.18469>
                j = _int(m)
                _pc = 4
                continue
            case 3:  # <D.18470>
                i[0] = m
                _pc = 4
            case 4:  # L.318
                _7 = i[0]
                _8 = _7 + 1
                _pc = 5 if j > _8 else 6
                continue
            case 5:  # <D.18472>
                _pc = 1
                continue
            case 6:  # L.319
                _9 = a[0]
                _10 = i[0]
                _11 = _int(_10)
                _12 = _11 + -1
                _13 = b[_12]
                _14 = _9 - _13
                _15 = _14
                _16 = i[0]
                _17 = _16 + 1
                _18 = _int(_17)
                _19 = _18 + -1
                _20 = b[_19]
                _21 = i[0]
                _22 = _int(_21)
                _23 = _22 + -1
                _24 = b[_23]
                _25 = _20 - _24
                _26 = _25
                _27 = _div(_15, _26)
                s[0] = _27
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_tnrain(_state, rr, v, tm, radfld):
    cnstns_pi = _state.view(246160, '<f4')
    nzero = _state.view(177332, '<f4')
    D_18479 = _ZERO32
    a = _ZERO32
    __result_tnrain = _ZERO32
    D_9389 = _ZERO32
    D_9394 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                D_9389 = _f32(rr[0])
                _1 = __builtin_powf(D_9389, 2.0999999344348907470703125e-1)
                a = _f32(_div(4.1e+1, _1))
                _2 = rr[0]
                _pc = 1 if _2 <= 0.0 else 2
                continue
            case 1:  # <D.18474>
                __result_tnrain = _f32(1.0e+0)
                _pc = 2
                continue
            case 2:  # L.320
                _3 = rr[0]
                _pc = 3 if _3 <= 0.0 else 4
                continue
            case 3:  # <D.18477>
                D_18479 = _f32(__result_tnrain)
                return D_18479
            case 4:  # L.321
                _4 = v[0]
                _pc = 5 if _4 >= 3.5e+2 else 6
                continue
            case 5:  # <D.18480>
                D_9394 = _f32(a)
                _5 = cnstns_pi[0]
                nzero_327_6 = nzero[0]
                _7 = _5 * nzero_327_6
                _8 = __builtin_powif(D_9394, 3)
                _9 = _div(_7, _8)
                __result_tnrain = _f32(_9)
                _pc = 7
                continue
            case 6:  # <D.18481>
                _10 = _ft_gmrain(_state, v, tm, rr)
                __result_tnrain = _f32(_10)
                _11 = radfld[0]
                __result_tnrain_328_12 = __result_tnrain
                _13 = _11 * __result_tnrain_328_12
                __result_tnrain = _f32(_13)
                _pc = 7
            case 7:  # L.322
                D_18479 = _f32(__result_tnrain)
                return D_18479
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_gmrain(_state, freq, t, rate):
    _pc = 0
    while True:
        match _pc:
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_aitk(_state, arg, val, x, ndim):
    D_18521 = _ZERO32
    ubound_21 = 0
    size_22 = 0
    h = _ZERO32
    i = 0
    iend = 0
    ier = 0
    j = 0
    ubound_23 = 0
    size_24 = 0
    __result_aitk = _ZERO32
    D_9581 = 0
    D_9582 = 0
    D_9583 = 0
    D_9584 = 0
    D_9585 = 0
    D_9586 = 0
    D_9563 = 0
    D_9567 = 0
    D_9570 = 0
    D_9571 = 0
    D_9574 = 0
    D_9575 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = ndim[0]
                ubound_21 = _int(_int(_1))
                size_22 = _int(ubound_21)
                size_22 = _int(max(size_22, 0))
                D_9584 = _int(size_22 + -1)
                size_330_2 = _int(size_22)
                _3 = _int(size_330_2)
                D_9585 = _int(_3 * 32)
                size_331_4 = _int(size_22)
                D_9586 = _int(size_331_4 * 4)
                _5 = ndim[0]
                ubound_23 = _int(_int(_5))
                size_24 = _int(ubound_23)
                size_24 = _int(max(size_24, 0))
                D_9581 = _int(size_24 + -1)
                size_332_6 = _int(size_24)
                _7 = _int(size_332_6)
                D_9582 = _int(_7 * 32)
                size_333_8 = _int(size_24)
                D_9583 = _int(size_333_8 * 4)
                _9 = ndim[0]
                D_9563 = _int(_9 + -1)
                _pc = 1 if D_9563 <= 0 else 2
                continue
            case 1:  # <D.18516>
                _pc = 12 if D_9563 < 0 else 10
                continue
            case 2:  # __label_000001
                D_9567 = _int(ndim[0])
                j = _int(2)
                _pc = 3
            case 3:  # <D.18517>
                D_9570 = _int(j > D_9567)
                _pc = 10 if D_9570 != 0 else 4
                continue
            case 4:  # <D.18518>
                iend = _int(j + -1)
                D_9571 = _int(iend)
                i = _int(1)
                _pc = 5
            case 5:  # <D.18519>
                D_9574 = _int(i > D_9571)
                _pc = 9 if D_9574 != 0 else 6
                continue
            case 6:  # <D.18520>
                _10 = _int(i)
                _11 = _10 + -1
                _12 = arg[_11]
                _13 = _int(j)
                _14 = _13 + -1
                _15 = arg[_14]
                h = _f32(_12 - _15)
                D_9575 = _f32(h)
                _pc = 7 if D_9575 != 0.0 else 13
                continue
            case 7:  # __label_000002
                _16 = _int(i)
                _17 = _16 + -1
                _18 = val[_17]
                _19 = x[0]
                _20 = _int(j)
                _21 = _20 + -1
                _22 = arg[_21]
                _23 = _19 - _22
                _24 = _23
                _25 = _18 * _24
                _26 = _int(j)
                _27 = _26 + -1
                _28 = val[_27]
                _29 = x[0]
                _30 = _int(i)
                _31 = _30 + -1
                _32 = arg[_31]
                _33 = _29 - _32
                _34 = _33
                _35 = _28 * _34
                _36 = _25 - _35
                _37 = _36
                _38 = _int(j)
                _39 = _38 + -1
                _40 = _div(_37, h)
                val[_39] = _40
                _pc = 8
            case 8:  # L.348
                i = _int(i + 1)
                _pc = 5
                continue
            case 9:  # L.346
                j = _int(j + 1)
                _pc = 3
                continue
            case 10:  # __label_000007
                j = _int(ndim[0])
                _pc = 11
            case 11:  # __label_000008
                _41 = _int(j)
                _42 = _41 + -1
                _43 = val[_42]
                __result_aitk = _f32(_43)
                _pc = 12
            case 12:  # __label_000009
                D_18521 = _f32(__result_aitk)
                return D_18521
            case 13:  # __label_000013
                ier = _int(3)
                j = _int(iend)
                _pc = 11
                continue
            case 14:  # continuation_25
                D_18521 = _f32(__result_aitk)
                return D_18521
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_o3uv(_state, v, c):
    o3uvf_v1 = _state.view(35872, '<f4')
    o3uvf_dv = _state.view(35880, '<f4')
    o3uvf_npt = _state.view(35884, '<i4')
    o3uvf_s = _state.view(35888, '<f4')
    am = _ZERO32
    c0 = _ZERO32
    i = 0
    vr = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                c[0] = 0.0
                _1 = v[0]
                _2 = o3uvf_v1[0]
                _3 = _1 - _2
                _4 = _3
                _5 = o3uvf_dv[0]
                _6 = _div(_4, _5)
                _7 = _6 + 1.000010013580322265625e+0
                i = _int(_int(_7))
                _pc = 1 if i <= 0 else 2
                continue
            case 1:  # <D.18524>
                _pc = -1
                continue
            case 2:  # L.350
                _8 = o3uvf_npt[0]
                _pc = 3 if i > _8 else 4
                continue
            case 3:  # <D.18526>
                _pc = -1
                continue
            case 4:  # L.351
                _9 = _f32(i)
                _10 = o3uvf_dv[0]
                _11 = _9 * _10
                _12 = o3uvf_v1[0]
                vr = _f32(_11 + _12)
                _13 = v[0]
                _14 = _13 + 1.00000001490116119384765625e-1
                _15 = _14
                _16 = vr <= _15
                _17 = v[0]
                _18 = _17 - 1.00000001490116119384765625e-1
                _19 = _18
                _20 = vr >= _19
                _21 = _16 & _20
                _pc = 5 if _21 != 0 else 6
                continue
            case 5:  # <D.18528>
                _pc = 9
                continue
            case 6:  # L.352
                _22 = o3uvf_npt[0]
                _pc = 7 if i == _22 else 8
                continue
            case 7:  # <D.18530>
                _23 = o3uvf_npt[0]
                i = _int(_23 + -1)
                _pc = 8
                continue
            case 8:  # L.353
                _24 = i + 1
                _25 = _int(_24)
                _26 = _25 + -1
                _27 = o3uvf_s[_26]
                _28 = _int(i)
                _29 = _28 + -1
                _30 = o3uvf_s[_29]
                _31 = _27 - _30
                _32 = _31
                _33 = o3uvf_dv[0]
                am = _f32(_div(_32, _33))
                _34 = _int(i)
                _35 = _34 + -1
                _36 = o3uvf_s[_35]
                _37 = am * vr
                c0 = _f32(_36 - _37)
                _38 = v[0]
                _39 = am * _38
                _40 = c0 + _39
                c[0] = _40
                _pc = -1
                continue
            case 9:  # __label_000005
                _41 = _int(i)
                _42 = _41 + -1
                _43 = o3uvf_s[_42]
                c[0] = _43
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_o3hht2(_state, v, c):
    o3hh2_v1s = _state.view(25088, '<f4')
    o3hh2_dvs = _state.view(25096, '<f4')
    o3hh2_npts = _state.view(25100, '<i4')
    o3hh2_s = _state.view(25104, '<f4')
    _ft_o3int(_state, v, o3hh2_v1s, o3hh2_dvs, o3hh2_npts, o3hh2_s, c)


def _ft_o3int(_state, v1c, v1, dv, npt, conti, conto):
    i = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                conto[0] = 0.0
                _1 = v1c[0]
                _2 = v1[0]
                _3 = _1 - _2
                _4 = _3
                _5 = dv[0]
                _6 = _div(_4, _5)
                _7 = _6 + 1.000010013580322265625e+0
                i = _int(_int(_7))
                _pc = 1 if i <= 0 else 2
                continue
            case 1:  # <D.18533>
                _pc = -1
                continue
            case 2:  # L.354
                _8 = npt[0]
                _pc = 3 if i > _8 else 4
                continue
            case 3:  # <D.18535>
                _pc = -1
                continue
            case 4:  # L.355
                _9 = _int(i)
                _10 = _9 + -1
                _11 = conti[_10]
                conto[0] = _11
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_o3hht1(_state, v, c):
    o3hh1_v1s = _state.view(14304, '<f4')
    o3hh1_dvs = _state.view(14312, '<f4')
    o3hh1_npts = _state.view(14316, '<i4')
    o3hh1_s = _state.view(14320, '<f4')
    _ft_o3int(_state, v, o3hh1_v1s, o3hh1_dvs, o3hh1_npts, o3hh1_s, c)


def _ft_o3hht0(_state, v, c):
    o3hh0_v1s = _state.view(3520, '<f4')
    o3hh0_dvs = _state.view(3528, '<f4')
    o3hh0_npts = _state.view(3532, '<i4')
    o3hh0_s = _state.view(3536, '<f4')
    _ft_o3int(_state, v, o3hh0_v1s, o3hh0_dvs, o3hh0_npts, o3hh0_s, c)


def _ft_schrun(_state, v, cprun):
    shur_shn = _state.view(170368, '<f4')
    dv = _state.view(179856, '<f4')
    inum = _state.view(179860, '<i4')
    v1 = _state.view(179848, '<f4')
    v2 = _state.view(179852, '<f4')
    ind = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                cprun[0] = -2.0e+1
                _1 = v[0]
                v1_334_2 = v1[0]
                _pc = 1 if _1 < v1_334_2 else 2
                continue
            case 1:  # <D.18537>
                _pc = 7
                continue
            case 2:  # L.356
                _3 = v[0]
                v2_335_4 = v2[0]
                _pc = 3 if _3 > v2_335_4 else 4
                continue
            case 3:  # <D.18539>
                _pc = 7
                continue
            case 4:  # L.357
                _5 = v[0]
                v1_336_6 = v1[0]
                _7 = _5 - v1_336_6
                _8 = _7
                dv_337_9 = dv[0]
                _10 = _div(_8, dv_337_9)
                _11 = _10 + 1.00010001659393310546875e+0
                ind = _int(_int(_11))
                inum_338_12 = inum[0]
                _pc = 5 if ind > inum_338_12 else 6
                continue
            case 5:  # <D.18541>
                _pc = 7
                continue
            case 6:  # L.358
                _13 = _int(ind)
                _14 = _13 + -1
                _15 = shur_shn[_14]
                cprun[0] = _15
                _pc = 7
            case 7:  # __label_000020
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_o2cont(_state, v, sigma, alpha, beta):
    o2c_o2s0 = _state.view(37040, '<f4')
    o2c_o2a = _state.view(37336, '<f4')
    o2c_o2b = _state.view(37632, '<f4')
    o2c_v1o2 = _state.view(37928, '<f4')
    o2c_dvo2 = _state.view(37936, '<f4')
    o2c_npto2 = _state.view(37940, '<i4')
    a = _zeros(1, '<f4')
    b = _zeros(1, '<f4')
    c = _zeros(1, '<f4')
    D_9710 = _ZERO32
    D_9711 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                sigma[0] = 0.0
                alpha[0] = 0.0
                beta[0] = 0.0
                _1 = v[0]
                _pc = 1 if _1 < 1.395e+3 else 2
                continue
            case 1:  # <D.18544>
                _pc = 5
                continue
            case 2:  # L.359
                _2 = v[0]
                _pc = 3 if _2 > 1.76e+3 else 4
                continue
            case 3:  # <D.18546>
                _pc = 5
                continue
            case 4:  # L.360
                _ft_o2int(_state, v, o2c_v1o2, o2c_dvo2, o2c_npto2, c, o2c_o2s0, a, o2c_o2a, b, o2c_o2b)
                a_339_3 = a[0]
                alpha[0] = a_339_3
                D_9710 = _f32(a[0])
                D_9711 = _f32(D_9710 * D_9710)
                _4 = _div(D_9711, 2.0e+0)
                b_340_5 = b[0]
                _6 = _4 + b_340_5
                beta[0] = _6
                c_341_7 = c[0]
                _8 = _div(c_341_7, 2.0946000516414642333984375e-1)
                sigma[0] = _8
                _pc = 5
            case 5:  # __label_000030
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_o2int(_state, v1c, v1, dv, npt, c, carray, a, aarray, b, barray):
    i = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                c[0] = 0.0
                a[0] = 0.0
                b[0] = 0.0
                _1 = v1c[0]
                _2 = v1[0]
                _3 = _1 - _2
                _4 = _3
                _5 = dv[0]
                _6 = _div(_4, _5)
                _7 = _6 + 1.000010013580322265625e+0
                i = _int(_int(_7))
                _pc = 1 if i <= 0 else 2
                continue
            case 1:  # <D.18550>
                _pc = -1
                continue
            case 2:  # L.361
                _8 = npt[0]
                _pc = 3 if i > _8 else 4
                continue
            case 3:  # <D.18552>
                _pc = -1
                continue
            case 4:  # L.362
                _9 = _int(i)
                _10 = _9 + -1
                _11 = carray[_10]
                c[0] = _11
                _12 = _int(i)
                _13 = _12 + -1
                _14 = aarray[_13]
                a[0] = _14
                _15 = _int(i)
                _16 = _15 + -1
                _17 = barray[_16]
                b[0] = _17
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_hertda(_state, herz, v):
    corr = _ZERO32
    rlosch = _ZERO32
    yratio = _ZERO32
    D_9733 = _ZERO32
    D_9734 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                herz[0] = 0.0
                _1 = v[0]
                _pc = 1 if _1 <= 3.6e+4 else 2
                continue
            case 1:  # <D.18554>
                return
            case 2:  # L.363
                corr = _f32(0.0)
                _2 = v[0]
                _pc = 3 if _2 <= 4.0e+4 else 4
                continue
            case 3:  # <D.18556>
                _3 = v[0]
                _4 = 4.0e+4 - _3
                _5 = _4
                _6 = _div(_5, 4.0e+3)
                _7 = _6
                corr = _f32(_7 * 7.91700034107829693016869565726627226129102563034756201432e-27)
                _pc = 4
                continue
            case 4:  # L.364
                rlosch = _f32(2.6867998188845924352e+19)
                _8 = v[0]
                yratio = _f32(_div(_8, 4.8811e+4))
                _9 = __builtin_logf(yratio)
                D_9733 = _f32(_9)
                D_9734 = _f32(D_9733 * D_9733)
                _10 = yratio
                _11 = _10 * 6.88400021143749606700808720704019101274684366842393501429e-24
                _12 = D_9734 * 6.973799896240234375e+1
                _13 = -_12
                _14 = __builtin_expf(_13)
                _15 = _11 * _14
                _16 = _15 - corr
                herz[0] = _16
                _17 = herz[0]
                _18 = rlosch * _17
                herz[0] = _18
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_aerext(_state, v):
    __BLNK___absc = _state.view(283836, '<f4')
    __BLNK___extc = _state.view(284776, '<f4')
    __BLNK___asyc = _state.view(285716, '<f4')
    __BLNK___vx2 = _state.view(286656, '<f4')
    __BLNK___awccon = _state.view(286844, '<f4')
    aer_extv = _state.view(231840, '<f4')
    aer_absv = _state.view(231860, '<f4')
    aer_asyv = _state.view(231880, '<f4')
    aertm_taer = _state.view(246096, '<f4')
    alam = _ZERO32
    i = _zeros(1, '<i4')
    mr = _zeros(1, '<i4')
    n = 0
    v0 = _ZERO32
    vxd = _ZERO32
    xd = _ZERO32
    D_9899 = 0
    D_9908 = 0
    C_9909 = _array([3.333300018310546875e+1], '<f4')
    D_9919 = 0
    D_9920 = _ZERO32
    D_9925 = 0
    D_9929 = 0
    D_9933 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                i[0] = 1
                _pc = 1
            case 1:  # <D.18560>
                i_342_1 = i[0]
                D_9899 = _int(i_342_1 > 5)
                _pc = 4 if D_9899 != 0 else 2
                continue
            case 2:  # <D.18561>
                i_343_2 = i[0]
                _3 = _int(i_343_2)
                _4 = _3 + -1
                aer_extv[_4] = 0.0
                i_344_5 = i[0]
                _6 = _int(i_344_5)
                _7 = _6 + -1
                aer_absv[_7] = 0.0
                i_345_8 = i[0]
                _9 = _int(i_345_8)
                _10 = _9 + -1
                aer_asyv[_10] = 0.0
                _pc = 3
            case 3:  # L.365
                i_346_11 = i[0]
                _12 = i_346_11 + 1
                i[0] = _12
                _pc = 1
                continue
            case 4:  # L.366
                _13 = v[0]
                _pc = 5 if _13 <= 9.99999974737875163555145263671875e-6 else 6
                continue
            case 5:  # <D.18562>
                _pc = 29
                continue
            case 6:  # L.367
                _14 = v[0]
                _pc = 7 if _14 <= 3.333300018310546875e+1 else 8
                continue
            case 7:  # <D.18564>
                _pc = 24
                continue
            case 8:  # L.368
                _15 = v[0]
                _pc = 9 if _15 <= 5.0e+1 else 14
                continue
            case 9:  # <D.18566>
                mr[0] = 1
                _pc = 10
            case 10:  # <D.18568>
                mr_347_16 = mr[0]
                D_9908 = _int(mr_347_16 > 5)
                _pc = 13 if D_9908 != 0 else 11
                continue
            case 11:  # <D.18569>
                mr_348_17 = mr[0]
                _18 = _int(mr_348_17)
                _19 = _18 + -1
                _20 = __BLNK___awccon[_19:]
                mr_349_21 = mr[0]
                _22 = _int(mr_349_21)
                _23 = _22 + -1
                _24 = aertm_taer[_23:]
                mr_350_25 = mr[0]
                _26 = _int(mr_350_25)
                _27 = _26 + 229
                _28 = _ft_gamfog(_state, mr, C_9909, _24, _20)
                __BLNK___extc[_27] = _28
                mr_351_29 = mr[0]
                _30 = _int(mr_351_29)
                _31 = _30 + 229
                mr_352_32 = mr[0]
                _33 = _int(mr_352_32)
                _34 = _33 + 229
                _35 = __BLNK___extc[_31]
                __BLNK___absc[_34] = _35
                mr_353_36 = mr[0]
                _37 = _int(mr_353_36)
                _38 = _37 + 229
                __BLNK___asyc[_38] = 0.0
                _pc = 12
            case 12:  # L.370
                mr_354_39 = mr[0]
                _40 = mr_354_39 + 1
                mr[0] = _40
                _pc = 10
                continue
            case 13:  # L.371
                _pc = 14
                continue
            case 14:  # L.369
                v0 = _f32(v[0])
                alam = _f32(_div(1.0e+4, v0))
                n = _int(2)
                _pc = 15
            case 15:  # <D.18571>
                D_9919 = _int(n > 47)
                _pc = 18 if D_9919 != 0 else 16
                continue
            case 16:  # <D.18572>
                _41 = _int(n)
                _42 = _41 + -1
                _43 = __BLNK___vx2[_42]
                xd = _f32(alam - _43)
                D_9920 = _f32(xd)
                _pc = 19 if D_9920 < 0.0 else 17
                continue
            case 17:  # L.372
                n = _int(n + 1)
                _pc = 15
                continue
            case 18:  # L.373
                n = _int(47)
                _pc = 19
            case 19:  # __label_000015
                _44 = _int(n)
                _45 = _44 + -1
                _46 = __BLNK___vx2[_45]
                _47 = n + -1
                _48 = _int(_47)
                _49 = _48 + -1
                _50 = __BLNK___vx2[_49]
                vxd = _f32(_46 - _50)
                i[0] = 1
                _pc = 20
            case 20:  # <D.18573>
                i_355_51 = i[0]
                D_9925 = _int(i_355_51 > 5)
                _pc = 23 if D_9925 != 0 else 21
                continue
            case 21:  # <D.18574>
                _52 = _int(n)
                _53 = _52 * 5
                i_356_54 = i[0]
                _55 = _int(i_356_54)
                _56 = _53 + _55
                _57 = _56 + -6
                _58 = __BLNK___extc[_57]
                _59 = n + -1
                _60 = _int(_59)
                _61 = _60 * 5
                i_357_62 = i[0]
                _63 = _int(i_357_62)
                _64 = _61 + _63
                _65 = _64 + -6
                _66 = __BLNK___extc[_65]
                _67 = _58 - _66
                _68 = _67
                _69 = xd * _68
                _70 = _div(_69, vxd)
                _71 = _int(n)
                _72 = _71 * 5
                i_358_73 = i[0]
                _74 = _int(i_358_73)
                _75 = _72 + _74
                _76 = _75 + -6
                _77 = __BLNK___extc[_76]
                i_359_78 = i[0]
                _79 = _int(i_359_78)
                _80 = _79 + -1
                _81 = _70 + _77
                aer_extv[_80] = _81
                _82 = _int(n)
                _83 = _82 * 5
                i_360_84 = i[0]
                _85 = _int(i_360_84)
                _86 = _83 + _85
                _87 = _86 + -6
                _88 = __BLNK___absc[_87]
                _89 = n + -1
                _90 = _int(_89)
                _91 = _90 * 5
                i_361_92 = i[0]
                _93 = _int(i_361_92)
                _94 = _91 + _93
                _95 = _94 + -6
                _96 = __BLNK___absc[_95]
                _97 = _88 - _96
                _98 = _97
                _99 = xd * _98
                _100 = _div(_99, vxd)
                _101 = _int(n)
                _102 = _101 * 5
                i_362_103 = i[0]
                _104 = _int(i_362_103)
                _105 = _102 + _104
                _106 = _105 + -6
                _107 = __BLNK___absc[_106]
                i_363_108 = i[0]
                _109 = _int(i_363_108)
                _110 = _109 + -1
                _111 = _100 + _107
                aer_absv[_110] = _111
                _112 = _int(n)
                _113 = _112 * 5
                i_364_114 = i[0]
                _115 = _int(i_364_114)
                _116 = _113 + _115
                _117 = _116 + -6
                _118 = __BLNK___asyc[_117]
                _119 = n + -1
                _120 = _int(_119)
                _121 = _120 * 5
                i_365_122 = i[0]
                _123 = _int(i_365_122)
                _124 = _121 + _123
                _125 = _124 + -6
                _126 = __BLNK___asyc[_125]
                _127 = _118 - _126
                _128 = _127
                _129 = xd * _128
                _130 = _div(_129, vxd)
                _131 = _int(n)
                _132 = _131 * 5
                i_366_133 = i[0]
                _134 = _int(i_366_133)
                _135 = _132 + _134
                _136 = _135 + -6
                _137 = __BLNK___asyc[_136]
                i_367_138 = i[0]
                _139 = _int(i_367_138)
                _140 = _139 + -1
                _141 = _130 + _137
                aer_asyv[_140] = _141
                _pc = 22
            case 22:  # L.374
                i_368_142 = i[0]
                _143 = i_368_142 + 1
                i[0] = _143
                _pc = 20
                continue
            case 23:  # L.375
                return
            case 24:  # __label_000030
                i[0] = 1
                _pc = 25
            case 25:  # <D.18575>
                i_369_144 = i[0]
                D_9929 = _int(i_369_144 > 5)
                _pc = 28 if D_9929 != 0 else 26
                continue
            case 26:  # <D.18576>
                i_370_145 = i[0]
                _146 = _int(i_370_145)
                _147 = _146 + -1
                _148 = __BLNK___awccon[_147:]
                i_371_149 = i[0]
                _150 = _int(i_371_149)
                _151 = _150 + -1
                _152 = aertm_taer[_151:]
                i_372_153 = i[0]
                _154 = _int(i_372_153)
                _155 = _154 + -1
                _156 = _ft_gamfog(_state, i, v, _152, _148)
                aer_extv[_155] = _156
                i_373_157 = i[0]
                _158 = _int(i_373_157)
                _159 = _158 + -1
                i_374_160 = i[0]
                _161 = _int(i_374_160)
                _162 = _161 + -1
                _163 = aer_extv[_159]
                aer_absv[_162] = _163
                i_375_164 = i[0]
                _165 = _int(i_375_164)
                _166 = _165 + -1
                aer_asyv[_166] = 0.0
                _pc = 27
            case 27:  # L.376
                i_376_167 = i[0]
                _168 = i_376_167 + 1
                i[0] = _168
                _pc = 25
                continue
            case 28:  # L.377
                return
            case 29:  # __label_000050
                i[0] = 1
                _pc = 30
            case 30:  # <D.18577>
                i_377_169 = i[0]
                D_9933 = _int(i_377_169 > 5)
                _pc = -1 if D_9933 != 0 else 31
                continue
            case 31:  # <D.18578>
                i_378_170 = i[0]
                _171 = _int(i_378_170)
                _172 = _171 + -1
                aer_extv[_172] = 0.0
                i_379_173 = i[0]
                _174 = _int(i_379_173)
                _175 = _174 + -1
                aer_absv[_175] = 0.0
                i_380_176 = i[0]
                _177 = _int(i_380_176)
                _178 = _177 + -1
                aer_asyv[_178] = 0.0
                _pc = 32
            case 32:  # L.378
                i_381_179 = i[0]
                _180 = i_381_179 + 1
                i[0] = _180
                _pc = 30
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_gamfog(_state, mr, freq, t, rho):
    D_18584 = _ZERO32
    aimak = _zeros(1, '<f4')
    cindex = _c64(0)
    key = _zeros(1, '<i4')
    reil = _zeros(1, '<f4')
    tc = _zeros(1, '<f4')
    wavl = _zeros(1, '<f4')
    __result_gamfog = _ZERO32
    D_9955 = _c64(0)
    D_9956 = _c64(0)
    D_9957 = _c64(0)
    D_9958 = _c64(0)
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = rho[0]
                _pc = 1 if _1 > 0.0 else 2
                continue
            case 1:  # <D.18582>
                _pc = 3
                continue
            case 2:  # L.380
                __result_gamfog = _f32(0.0)
                D_18584 = _f32(__result_gamfog)
                return D_18584
            case 3:  # __label_000002
                key[0] = 1
                _2 = mr[0]
                _pc = 4 if _2 > 4 else 5
                continue
            case 4:  # <D.18585>
                key[0] = 0
                _pc = 5
                continue
            case 5:  # L.381
                _3 = freq[0]
                _4 = _div(1.0e+0, _3)
                wavl[0] = _4
                _5 = t[0]
                _6 = _5 - 2.7320001220703125e+2
                tc[0] = _6
                tc_382_7 = tc[0]
                _pc = 6 if tc_382_7 < -2.0e+1 else 7
                continue
            case 6:  # <D.18588>
                tc[0] = -2.0e+1
                _pc = 7
                continue
            case 7:  # L.382
                _ft_indx(_state, wavl, tc, key, reil, aimak)
                reil_383_8 = reil[0]
                aimak_384_9 = aimak[0]
                cindex = _c64(__complex__(reil_383_8, aimak_384_9))
                D_9955 = _c64(cindex)
                D_9956 = _c64(D_9955 * D_9955)
                D_9957 = _c64(cindex)
                D_9958 = _c64(D_9957 * D_9957)
                _10 = freq[0]
                _11 = _10 * 1.8849999904632568359375e+0
                _12 = rho[0]
                _13 = _11 * _12
                _14 = D_9956 - __complex__(1.0e+0, 0.0)
                _15 = _14
                _16 = D_9958 + __complex__(2.0e+0, 0.0)
                _17 = _16
                _18 = _div(_15, _17)
                _19 = -_18
                _20 = _imag(_19)
                _21 = _13 * _20
                __result_gamfog = _f32(_21)
                D_18584 = _f32(__result_gamfog)
                return D_18584
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_indx(_state, wavl, tc, key, reil, aimag):
    r1 = _ZERO32
    r2 = _ZERO32
    C_9987 = _array([1.8389899730682373046875e+0], '<f4')
    C_9988 = _array([1.639e+3], '<f4')
    C_9989 = _array([5.23403984375e+4], '<f4')
    C_9990 = _array([1.03992001953125e+4], '<f4')
    C_9991 = _array([5.88239990234375e+2], '<f4')
    C_9992 = _array([3.45005e+5], '<f4')
    C_9993 = _array([2.59913e+5], '<f4')
    C_9994 = _array([1.612899932861328125e+2], '<f4')
    C_9995 = _array([4.331969921875e+4], '<f4')
    C_9996 = _array([2.766119921875e+4], '<f4')
    D_10010 = _ZERO32
    C_10014 = _array([1.8389899730682373046875e+0], '<f4')
    C_10015 = _array([1.639e+3], '<f4')
    C_10016 = _array([5.23403984375e+4], '<f4')
    C_10017 = _array([1.03992001953125e+4], '<f4')
    C_10018 = _array([5.88239990234375e+2], '<f4')
    C_10019 = _array([3.45005e+5], '<f4')
    C_10020 = _array([2.59913e+5], '<f4')
    C_10021 = _array([1.612899932861328125e+2], '<f4')
    C_10022 = _array([4.331969921875e+4], '<f4')
    C_10023 = _array([2.766119921875e+4], '<f4')
    D_10024 = _ZERO32
    C_10027 = _array([1.79907000064849853515625e+0], '<f4')
    C_10028 = _array([3.35227001953125e+3], '<f4')
    C_10029 = _array([9.9914e+5], '<f4')
    C_10030 = _array([1.51963e+5], '<f4')
    C_10031 = _array([1.639e+3], '<f4')
    C_10032 = _array([5.04835e+4], '<f4')
    C_10033 = _array([9.24626953125e+3], '<f4')
    C_10034 = _array([5.88239990234375e+2], '<f4')
    C_10035 = _array([8.44697e+5], '<f4')
    C_10036 = _array([1.07615e+6], '<f4')
    D_10037 = _ZERO32
    C_10038 = _array([1.79907000064849853515625e+0], '<f4')
    C_10039 = _array([3.35227001953125e+3], '<f4')
    C_10040 = _array([9.9914e+5], '<f4')
    C_10041 = _array([1.51963e+5], '<f4')
    C_10042 = _array([1.639e+3], '<f4')
    C_10043 = _array([5.04835e+4], '<f4')
    C_10044 = _array([9.24626953125e+3], '<f4')
    C_10045 = _array([5.88239990234375e+2], '<f4')
    C_10046 = _array([8.44697e+5], '<f4')
    C_10047 = _array([1.07615e+6], '<f4')
    D_10048 = _ZERO32
    C_10054 = _array([2.5e-1], '<f4')
    C_10055 = _array([3.0e+2], '<f4')
    C_10056 = _array([4.699999988079071044921875e-1], '<f4')
    C_10057 = _array([3.0e+0], '<f4')
    C_10065 = _array([3.8999998569488525390625e-1], '<f4')
    C_10066 = _array([1.7e+1], '<f4')
    C_10067 = _array([4.49999988079071044921875e-1], '<f4')
    C_10068 = _array([1.2999999523162841796875e+0], '<f4')
    C_10069 = _array([4.099999964237213134765625e-1], '<f4')
    C_10070 = _array([6.2e+1], '<f4')
    C_10071 = _array([3.499999940395355224609375e-1], '<f4')
    C_10072 = _array([1.7000000476837158203125e+0], '<f4')
    C_10076 = _array([4.099999964237213134765625e-1], '<f4')
    C_10077 = _array([6.2e+1], '<f4')
    C_10078 = _array([3.499999940395355224609375e-1], '<f4')
    C_10079 = _array([1.7000000476837158203125e+0], '<f4')
    C_10080 = _array([3.8999998569488525390625e-1], '<f4')
    C_10081 = _array([1.7e+1], '<f4')
    C_10082 = _array([4.49999988079071044921875e-1], '<f4')
    C_10083 = _array([1.2999999523162841796875e+0], '<f4')
    C_10084 = _array([2.5e-1], '<f4')
    C_10085 = _array([3.0e+2], '<f4')
    C_10086 = _array([4.000000059604644775390625e-1], '<f4')
    C_10087 = _array([2.0e+0], '<f4')
    C_10091 = _array([3.8999998569488525390625e-1], '<f4')
    C_10092 = _array([1.7e+1], '<f4')
    C_10093 = _array([4.49999988079071044921875e-1], '<f4')
    C_10094 = _array([1.2999999523162841796875e+0], '<f4')
    C_10095 = _array([4.099999964237213134765625e-1], '<f4')
    C_10096 = _array([6.2e+1], '<f4')
    C_10097 = _array([2.199999988079071044921875e-1], '<f4')
    C_10098 = _array([1.7999999523162841796875e+0], '<f4')
    C_10099 = _array([2.5e-1], '<f4')
    C_10100 = _array([3.0e+2], '<f4')
    C_10101 = _array([4.000000059604644775390625e-1], '<f4')
    C_10102 = _array([2.0e+0], '<f4')
    C_10106 = _array([1.19999997317790985107421875e-1], '<f4')
    C_10107 = _array([6.099999904632568359375e+0], '<f4')
    C_10108 = _array([4.19999994337558746337890625e-2], '<f4')
    C_10109 = _array([6.0000002384185791015625e-1], '<f4')
    C_10110 = _array([3.8999998569488525390625e-1], '<f4')
    C_10111 = _array([1.7e+1], '<f4')
    C_10112 = _array([1.6500000655651092529296875e-1], '<f4')
    C_10113 = _array([2.400000095367431640625e+0], '<f4')
    C_10114 = _array([4.099999964237213134765625e-1], '<f4')
    C_10115 = _array([6.2e+1], '<f4')
    C_10116 = _array([2.199999988079071044921875e-1], '<f4')
    C_10117 = _array([1.7999999523162841796875e+0], '<f4')
    C_10121 = _array([9.99999977648258209228515625e-3], '<f4')
    C_10122 = _array([4.94999980926513671875e+0], '<f4')
    C_10123 = _array([5.00000007450580596923828125e-2], '<f4')
    C_10124 = _array([1.0e+0], '<f4')
    C_10125 = _array([1.19999997317790985107421875e-1], '<f4')
    C_10126 = _array([6.099999904632568359375e+0], '<f4')
    C_10127 = _array([8.9999996125698089599609375e-3], '<f4')
    C_10128 = _array([2.0e+0], '<f4')
    C_10132 = _array([2.700000107288360595703125e-1], '<f4')
    C_10133 = _array([2.9700000286102294921875e+0], '<f4')
    C_10134 = _array([3.9999999105930328369140625e-2], '<f4')
    C_10135 = _array([2.0e+0], '<f4')
    C_10136 = _array([9.99999977648258209228515625e-3], '<f4')
    C_10137 = _array([4.94999980926513671875e+0], '<f4')
    C_10138 = _array([5.99999986588954925537109375e-2], '<f4')
    C_10139 = _array([1.0e+0], '<f4')
    C_10140 = _array([2.700000107288360595703125e-1], '<f4')
    C_10141 = _array([2.9700000286102294921875e+0], '<f4')
    C_10142 = _array([2.500000037252902984619140625e-2], '<f4')
    C_10143 = _array([2.0e+0], '<f4')
    C_10144 = _array([9.99999977648258209228515625e-3], '<f4')
    C_10145 = _array([4.94999980926513671875e+0], '<f4')
    C_10146 = _array([5.99999986588954925537109375e-2], '<f4')
    C_10147 = _array([1.0e+0], '<f4')
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                r1 = _f32(0.0)
                r2 = _f32(0.0)
                _pc = 1
            case 1:  # __label_000002
                _ft_debye(_state, wavl, tc, key, reil, aimag)
                _pc = 2
            case 2:  # __label_000004
                _1 = wavl[0]
                _pc = 3 if _1 > 3.4000001847743988037109375e-2 else 4
                continue
            case 3:  # <D.18593>
                _pc = 5
                continue
            case 4:  # L.383
                _pc = 8
                continue
            case 5:  # __label_000005
                _2 = wavl[0]
                _pc = 6 if _2 > 1.00000001490116119384765625e-1 else 7
                continue
            case 6:  # <D.18595>
                _pc = 15
                continue
            case 7:  # __label_000006
                r2 = _f32(_ft_dop(_state, wavl, C_9987, C_9988, C_9989, C_9990, C_9991, C_9992, C_9993, C_9994, C_9995, C_9996))
                _3 = wavl[0]
                _4 = _3 * 2.4999999368446879088878631591796875e-5
                D_10010 = _f32(_4)
                _5 = tc[0]
                _6 = _5 - 2.5e+1
                _7 = _6
                _8 = r2 * _7
                _9 = _8 * 9.99999974737875163555145263671875e-5
                _10 = __builtin_powf(D_10010, 2.5e-1)
                _11 = __builtin_expf(_10)
                _12 = _9 * _11
                r2 = _f32(r2 + _12)
                _13 = reil[0]
                _14 = wavl[0]
                _15 = _14 - 3.4000001847743988037109375e-2
                _16 = _15
                _17 = _13 * _16
                _18 = _div(_17, 6.599999964237213134765625e-2)
                _19 = wavl[0]
                _20 = 1.00000001490116119384765625e-1 - _19
                _21 = _20
                _22 = r2 * _21
                _23 = _div(_22, 6.599999964237213134765625e-2)
                _24 = _18 + _23
                reil[0] = _24
                _pc = 15
                continue
            case 8:  # __label_000007
                _25 = wavl[0]
                _pc = 9 if _25 > 6.00000028498470783233642578125e-4 else 10
                continue
            case 9:  # <D.18597>
                _pc = 11
                continue
            case 10:  # L.385
                _pc = 14
                continue
            case 11:  # __label_000008
                _26 = _ft_dop(_state, wavl, C_10014, C_10015, C_10016, C_10017, C_10018, C_10019, C_10020, C_10021, C_10022, C_10023)
                reil[0] = _26
                _27 = wavl[0]
                _28 = _27 * 2.4999999368446879088878631591796875e-5
                D_10024 = _f32(_28)
                _29 = reil[0]
                _30 = reil[0]
                _31 = tc[0]
                _32 = _31 - 2.5e+1
                _33 = _32
                _34 = _30 * _33
                _35 = _34 * 9.99999974737875163555145263671875e-5
                _36 = __builtin_powf(D_10024, 2.5e-1)
                _37 = __builtin_expf(_36)
                _38 = _35 * _37
                _39 = _29 + _38
                reil[0] = _39
                _40 = wavl[0]
                _pc = 12 if _40 > 6.9999997504055500030517578125e-4 else 13
                continue
            case 12:  # <D.18599>
                _pc = 15
                continue
            case 13:  # __label_000009
                r1 = _f32(_ft_dop(_state, wavl, C_10027, C_10028, C_10029, C_10030, C_10031, C_10032, C_10033, C_10034, C_10035, C_10036))
                _41 = wavl[0]
                _42 = _41 * 2.4999999368446879088878631591796875e-5
                D_10037 = _f32(_42)
                _43 = tc[0]
                _44 = _43 - 2.5e+1
                _45 = _44
                _46 = r1 * _45
                _47 = _46 * 9.99999974737875163555145263671875e-5
                _48 = __builtin_powf(D_10037, 2.5e-1)
                _49 = __builtin_expf(_48)
                _50 = _47 * _49
                r1 = _f32(r1 + _50)
                _51 = wavl[0]
                _52 = 6.9999997504055500030517578125e-4 - _51
                _53 = _52
                _54 = r1 * _53
                _55 = _div(_54, 9.99999974737875163555145263671875e-5)
                _56 = reil[0]
                _57 = wavl[0]
                _58 = _57 - 6.00000028498470783233642578125e-4
                _59 = _58
                _60 = _56 * _59
                _61 = _div(_60, 9.99999974737875163555145263671875e-5)
                _62 = _55 + _61
                reil[0] = _62
                _pc = 15
                continue
            case 14:  # __label_000010
                _63 = _ft_dop(_state, wavl, C_10038, C_10039, C_10040, C_10041, C_10042, C_10043, C_10044, C_10045, C_10046, C_10047)
                reil[0] = _63
                _64 = wavl[0]
                _65 = _64 * 2.4999999368446879088878631591796875e-5
                D_10048 = _f32(_65)
                _66 = reil[0]
                _67 = reil[0]
                _68 = tc[0]
                _69 = _68 - 2.5e+1
                _70 = _69
                _71 = _67 * _70
                _72 = _71 * 9.99999974737875163555145263671875e-5
                _73 = __builtin_powf(D_10048, 2.5e-1)
                _74 = __builtin_expf(_73)
                _75 = _72 * _74
                _76 = _66 + _75
                reil[0] = _76
                _pc = 15
            case 15:  # __label_000011
                _77 = wavl[0]
                _pc = 16 if _77 >= 3.00000011920928955078125e-1 else 17
                continue
            case 16:  # <D.18601>
                _pc = -1
                continue
            case 17:  # L.387
                _78 = wavl[0]
                _pc = 18 if _78 >= 2.999999932944774627685546875e-2 else 19
                continue
            case 18:  # <D.18603>
                _pc = 20
                continue
            case 19:  # L.388
                _pc = 21
                continue
            case 20:  # __label_000012
                _79 = aimag[0]
                _80 = _ft_ab(_state, wavl, C_10054, C_10055, C_10056, C_10057)
                _81 = _79 + _80
                _82 = _ft_ab(_state, wavl, C_10065, C_10066, C_10067, C_10068)
                _83 = _81 + _82
                _84 = _ft_ab(_state, wavl, C_10069, C_10070, C_10071, C_10072)
                _85 = _83 + _84
                aimag[0] = _85
                _pc = -1
                continue
            case 21:  # __label_000013
                _86 = wavl[0]
                _pc = 22 if _86 >= 6.2000001780688762664794921875e-3 else 23
                continue
            case 22:  # <D.18605>
                _pc = 24
                continue
            case 23:  # L.389
                _pc = 25
                continue
            case 24:  # __label_000014
                _87 = aimag[0]
                _88 = _ft_ab(_state, wavl, C_10076, C_10077, C_10078, C_10079)
                _89 = _87 + _88
                _90 = _ft_ab(_state, wavl, C_10080, C_10081, C_10082, C_10083)
                _91 = _89 + _90
                _92 = _ft_ab(_state, wavl, C_10084, C_10085, C_10086, C_10087)
                _93 = _91 + _92
                aimag[0] = _93
                _pc = -1
                continue
            case 25:  # __label_000015
                _94 = wavl[0]
                _pc = 26 if _94 >= 1.700000022538006305694580078125e-3 else 27
                continue
            case 26:  # <D.18607>
                _pc = 28
                continue
            case 27:  # L.390
                _pc = 29
                continue
            case 28:  # __label_000016
                _95 = aimag[0]
                _96 = _ft_ab(_state, wavl, C_10091, C_10092, C_10093, C_10094)
                _97 = _95 + _96
                _98 = _ft_ab(_state, wavl, C_10095, C_10096, C_10097, C_10098)
                _99 = _97 + _98
                _100 = _ft_ab(_state, wavl, C_10099, C_10100, C_10101, C_10102)
                _101 = _99 + _100
                aimag[0] = _101
                _pc = -1
                continue
            case 29:  # __label_000017
                _102 = wavl[0]
                _pc = 30 if _102 >= 6.099999882280826568603515625e-4 else 31
                continue
            case 30:  # <D.18609>
                _pc = 32
                continue
            case 31:  # L.391
                _pc = 33
                continue
            case 32:  # __label_000018
                _103 = aimag[0]
                _104 = _ft_ab(_state, wavl, C_10106, C_10107, C_10108, C_10109)
                _105 = _103 + _104
                _106 = _ft_ab(_state, wavl, C_10110, C_10111, C_10112, C_10113)
                _107 = _105 + _106
                _108 = _ft_ab(_state, wavl, C_10114, C_10115, C_10116, C_10117)
                _109 = _107 + _108
                aimag[0] = _109
                _pc = -1
                continue
            case 33:  # __label_000019
                _110 = wavl[0]
                _pc = 34 if _110 >= 4.949999856762588024139404296875e-4 else 35
                continue
            case 34:  # <D.18611>
                _pc = 36
                continue
            case 35:  # L.392
                _pc = 37
                continue
            case 36:  # __label_000020
                _111 = aimag[0]
                _112 = _ft_ab(_state, wavl, C_10121, C_10122, C_10123, C_10124)
                _113 = _111 + _112
                _114 = _ft_ab(_state, wavl, C_10125, C_10126, C_10127, C_10128)
                _115 = _113 + _114
                aimag[0] = _115
                _pc = -1
                continue
            case 37:  # __label_000021
                _116 = wavl[0]
                _pc = 38 if _116 >= 2.969999914057552814483642578125e-4 else 39
                continue
            case 38:  # <D.18613>
                _pc = 40
                continue
            case 39:  # L.393
                _pc = 41
                continue
            case 40:  # __label_000022
                _117 = aimag[0]
                _118 = _ft_ab(_state, wavl, C_10132, C_10133, C_10134, C_10135)
                _119 = _117 + _118
                _120 = _ft_ab(_state, wavl, C_10136, C_10137, C_10138, C_10139)
                _121 = _119 + _120
                aimag[0] = _121
                _pc = -1
                continue
            case 41:  # __label_000023
                _122 = aimag[0]
                _123 = _ft_ab(_state, wavl, C_10140, C_10141, C_10142, C_10143)
                _124 = _122 + _123
                _125 = _ft_ab(_state, wavl, C_10144, C_10145, C_10146, C_10147)
                _126 = _124 + _125
                aimag[0] = _126
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_ab(_state, wavl, a, cen, b, c):
    D_18615 = _ZERO32
    __result_ab = _ZERO32
    D_10148 = _ZERO32
    _1 = wavl[0]
    _2 = _1 * 1.0e+4
    _3 = cen[0]
    _4 = _div(_2, _3)
    _5 = __builtin_log10f(_4)
    _6 = b[0]
    _7 = _div(_5, _6)
    _8 = _7
    D_10148 = _f32(abs(_8))
    _9 = a[0]
    _10 = c[0]
    _11 = __builtin_powf(D_10148, _10)
    _12 = -_11
    _13 = __builtin_expf(_12)
    _14 = _9 * _13
    _15 = -_14
    __result_ab = _f32(_15)
    D_18615 = _f32(__result_ab)
    return D_18615


def _ft_dop(_state, wavl, a, cen1, b, c, cen2, d, e, cen3, f, g):
    D_18618 = _ZERO32
    h1 = _ZERO32
    h2 = _ZERO32
    h3 = _ZERO32
    v = _ZERO32
    v2 = _ZERO32
    __result_dop = _ZERO32
    D_10155 = _ZERO32
    D_10156 = _ZERO32
    D_10157 = _ZERO32
    D_10158 = _ZERO32
    D_10159 = _ZERO32
    D_10160 = _ZERO32
    _1 = wavl[0]
    v = _f32(_div(1.0e+0, _1))
    v2 = _f32(v * v)
    D_10155 = _f32(cen1[0])
    D_10156 = _f32(D_10155 * D_10155)
    h1 = _f32(D_10156 - v2)
    D_10157 = _f32(cen2[0])
    D_10158 = _f32(D_10157 * D_10157)
    h2 = _f32(D_10158 - v2)
    D_10159 = _f32(cen3[0])
    D_10160 = _f32(D_10159 * D_10159)
    h3 = _f32(D_10160 - v2)
    _2 = a[0]
    _3 = b[0]
    _4 = h1 * _3
    _5 = h1 * h1
    _6 = c[0]
    _7 = v2 * _6
    _8 = _5 + _7
    _9 = _8
    _10 = _div(_4, _9)
    _11 = _2 + _10
    _12 = d[0]
    _13 = h2 * _12
    _14 = h2 * h2
    _15 = e[0]
    _16 = v2 * _15
    _17 = _14 + _16
    _18 = _17
    _19 = _div(_13, _18)
    _20 = _11 + _19
    _21 = f[0]
    _22 = h3 * _21
    _23 = h3 * h3
    _24 = g[0]
    _25 = v2 * _24
    _26 = _23 + _25
    _27 = _26
    _28 = _div(_22, _27)
    _29 = _20 + _28
    _30 = __builtin_sqrtf(_29)
    __result_dop = _f32(_30)
    D_18618 = _f32(__result_dop)
    return D_18618


def _ft_debye(_state, wavl, tc, key, re, ai):
    cnstns_bigexp = _state.view(246180, '<f4')
    alpha = _ZERO32
    c1 = _ZERO32
    c2 = _ZERO32
    dem = _ZERO32
    e1 = _ZERO32
    e2 = _ZERO32
    efin = _ZERO32
    es = _ZERO32
    sig = _ZERO32
    t = _ZERO32
    t125 = _ZERO32
    tau = _ZERO32
    D_10189 = _ZERO32
    D_10190 = _ZERO32
    D_10191 = _ZERO32
    D_10194 = _ZERO32
    D_10195 = _ZERO32
    D_10196 = _ZERO32
    D_10199 = _ZERO32
    D_10200 = _ZERO32
    D_10201 = _ZERO32
    D_10202 = _ZERO32
    D_10203 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = tc[0]
                t = _f32(_1 + 2.73149993896484375e+2)
                _2 = key[0]
                _pc = 1 if _2 != 0 else 2
                continue
            case 1:  # <D.18621>
                _pc = 3
                continue
            case 2:  # L.394
                _pc = 4
                continue
            case 3:  # __label_000001
                _3 = tc[0]
                _4 = _3 * 2.164739929139614105224609375e-2
                _5 = _4 + 5.27136993408203125e+0
                _6 = tc[0]
                _7 = _6 * 1.31197995506227016448974609375e-3
                _8 = tc[0]
                _9 = _7 * _8
                efin = _f32(_5 - _9)
                _10 = _div(1.6812900543212890625e+1, t)
                alpha = _f32(6.09265007078647613525390625e-2 - _10)
                _11 = _div(2.51397998046875e+3, t)
                _12 = __builtin_expf(_11)
                tau = _f32(_12 * 3.3835999784059822559356689453125e-4)
                sig = _f32(1.25664e+9)
                _13 = tc[0]
                _14 = _13 - 2.5e+1
                D_10189 = _f32(_14)
                D_10190 = _f32(D_10189 * D_10189)
                _15 = tc[0]
                _16 = _15 - 2.5e+1
                D_10191 = _f32(_16)
                _17 = tc[0]
                _18 = _17 - 2.5e+1
                _19 = _18
                _20 = _19 * 4.579000174999237060546875e-3
                _21 = 1.0e+0 - _20
                _22 = D_10190 * 1.189999966300092637538909912109375e-5
                _23 = _21 + _22
                _24 = __builtin_powif(D_10191, 3)
                _25 = _24 * 2.80000005403735485742799937725067138671875e-8
                _26 = _23 - _25
                _27 = _26
                es = _f32(_27 * 7.854000091552734375e+1)
                _pc = 8
                continue
            case 4:  # __label_000002
                efin = _f32(3.1679999828338623046875e+0)
                _28 = tc[0]
                _29 = _28 * 2.30000005103647708892822265625e-4
                _30 = tc[0]
                _31 = _29 * _30
                _32 = tc[0]
                _33 = _32 * 5.2000000141561031341552734375e-3
                _34 = _31 + _33
                alpha = _f32(_34 + 2.8799998760223388671875e-1)
                _35 = t * 1.98689997196197509765625e+0
                _36 = _35
                t125 = _f32(_div(1.25e+4, _36))
                _37 = cnstns_bigexp[0]
                _pc = 5 if t125 <= _37 else 6
                continue
            case 5:  # <D.18623>
                _38 = -t125
                _39 = __builtin_expf(_38)
                sig = _f32(_39 * 1.2599999904632568359375e+0)
                _pc = 7
                continue
            case 6:  # <D.18624>
                sig = _f32(0.0)
                _pc = 7
            case 7:  # L.395
                _40 = t * 1.98689997196197509765625e+0
                _41 = _40
                _42 = _div(1.32e+4, _41)
                _43 = __builtin_expf(_42)
                tau = _f32(_43 * 9.99028779915533959865570068359375e-5)
                _44 = tc[0]
                _45 = _44 * 1.500000059604644775390625e-1
                _46 = tc[0]
                _47 = _45 * _46
                _48 = _47 + 3.1679999828338623046875e+0
                _49 = tc[0]
                _50 = _49 * 2.5e+0
                _51 = _48 + _50
                es = _f32(_51 + 2.0e+2)
                _pc = 8
            case 8:  # __label_000003
                _52 = wavl[0]
                c1 = _f32(_div(tau, _52))
                alpha = _f32(0.0)
                sig = _f32(0.0)
                c2 = _f32(alpha * 1.57079994678497314453125e+0)
                D_10194 = _f32(c1)
                D_10195 = _f32(c1)
                _53 = 1.0e+0 - alpha
                _54 = _53
                _55 = __builtin_powf(D_10194, _54)
                _56 = _55 * 2.0e+0
                _57 = __builtin_sinf(c2)
                _58 = _56 * _57
                _59 = _58 + 1.0e+0
                _60 = 1.0e+0 - alpha
                _61 = _60
                _62 = _61 * 2.0e+0
                _63 = _62
                _64 = __builtin_powf(D_10195, _63)
                dem = _f32(_59 + _64)
                D_10196 = _f32(c1)
                _65 = es - efin
                _66 = _65
                _67 = 1.0e+0 - alpha
                _68 = _67
                _69 = __builtin_powf(D_10196, _68)
                _70 = __builtin_sinf(c2)
                _71 = _69 * _70
                _72 = _71
                _73 = _72 + 1.0e+0
                _74 = _73
                _75 = _66 * _74
                _76 = _div(_75, dem)
                e1 = _f32(efin + _76)
                _77 = key[0]
                _78 = _77 != 0
                _79 = wavl[0]
                _80 = _79 >= 3.0e+2
                _81 = _78 & _80
                _pc = 9 if _81 != 0 else 10
                continue
            case 9:  # <D.18626>
                _82 = tc[0]
                _83 = _82 * 3.955999910831451416015625e-1
                e1 = _f32(8.7529998779296875e+1 - _83)
                _pc = 10
                continue
            case 10:  # L.396
                _84 = key[0]
                _85 = _84 != 0
                _86 = wavl[0]
                _87 = _86 >= 3.0e+2
                _88 = _85 & _87
                _pc = 11 if _88 != 0 else 12
                continue
            case 11:  # <D.18629>
                e1 = _f32(es)
                _pc = 12
                continue
            case 12:  # L.397
                D_10199 = _f32(c1)
                _89 = es - efin
                _90 = _89
                _91 = 1.0e+0 - alpha
                _92 = _91
                _93 = __builtin_powf(D_10199, _92)
                _94 = _90 * _93
                _95 = __builtin_cosf(c2)
                _96 = _94 * _95
                _97 = _div(_96, dem)
                _98 = wavl[0]
                _99 = sig * _98
                _100 = _div(_99, 1.88496003072e+11)
                e2 = _f32(_97 + _100)
                D_10200 = _f32(c1)
                D_10201 = _f32(D_10200 * D_10200)
                _101 = es - efin
                _102 = _101
                _103 = D_10201 + 1.0e+0
                _104 = _103
                _105 = _div(_102, _104)
                e1 = _f32(efin + _105)
                D_10202 = _f32(c1)
                D_10203 = _f32(D_10202 * D_10202)
                _106 = es - efin
                _107 = _106
                _108 = c1 * _107
                _109 = _108
                _110 = D_10203 + 1.0e+0
                _111 = _110
                e2 = _f32(_div(_109, _111))
                _112 = e1 * e1
                _113 = e2 * e2
                _114 = _112 + _113
                _115 = __builtin_sqrtf(_114)
                _116 = e1 + _115
                _117 = _116
                _118 = _div(_117, 2.0e+0)
                _119 = __builtin_sqrtf(_118)
                re[0] = _119
                _120 = re[0]
                _121 = _120 * 2.0e+0
                _122 = _121
                _123 = _div(e2, _122)
                _124 = -_123
                ai[0] = _124
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_hno3(_state, v, habs):
    h1 = _state.view(179872, '<f4')
    h2 = _state.view(179936, '<f4')
    h3 = _state.view(180000, '<f4')
    i = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                habs[0] = 0.0
                _1 = v[0]
                _2 = _1 >= 8.5e+2
                _3 = v[0]
                _4 = _3 <= 9.2e+2
                _5 = _2 & _4
                _pc = 1 if _5 != 0 else 2
                continue
            case 1:  # <D.18632>
                _pc = 7
                continue
            case 2:  # L.398
                _6 = v[0]
                _7 = _6 >= 1.275e+3
                _8 = v[0]
                _9 = _8 <= 1.35e+3
                _10 = _7 & _9
                _pc = 3 if _10 != 0 else 4
                continue
            case 3:  # <D.18634>
                _pc = 8
                continue
            case 4:  # L.399
                _11 = v[0]
                _12 = _11 >= 1.675e+3
                _13 = v[0]
                _14 = _13 <= 1.735e+3
                _15 = _12 & _14
                _pc = 5 if _15 != 0 else 6
                continue
            case 5:  # <D.18636>
                _pc = 9
                continue
            case 6:  # L.400
                return
            case 7:  # __label_000005
                _16 = v[0]
                _17 = _16 - 8.45e+2
                _18 = _17
                _19 = _div(_18, 5.0e+0)
                i = _int(_int(_19))
                _20 = _int(i)
                _21 = _20 + -1
                _22 = h1[_21]
                habs[0] = _22
                return
            case 8:  # __label_000010
                _23 = v[0]
                _24 = _23 - 1.27e+3
                _25 = _24
                _26 = _div(_25, 5.0e+0)
                i = _int(_int(_26))
                _27 = _int(i)
                _28 = _27 + -1
                _29 = h2[_28]
                habs[0] = _29
                return
            case 9:  # __label_000015
                _30 = v[0]
                _31 = _30 - 1.67e+3
                _32 = _31
                _33 = _div(_32, 5.0e+0)
                i = _int(_int(_33))
                _34 = _int(i)
                _35 = _34 + -1
                _36 = h3[_35]
                habs[0] = _36
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_c8dta(_state, c8l, v):
    c4c8_c8 = _state.view(104500, '<f4')
    iv = 0
    n = 0
    xd = _ZERO32
    xi = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                c8l[0] = 0.0
                _1 = v[0]
                _pc = 1 if _1 < 1.3e+4 else 2
                continue
            case 1:  # <D.18639>
                return
            case 2:  # L.401
                _2 = v[0]
                _pc = 3 if _2 > 5.0e+4 else 4
                continue
            case 3:  # <D.18641>
                return
            case 4:  # L.402
                _3 = v[0]
                iv = _int(_int(_3))
                _4 = iv > 24200
                _5 = iv <= 27499
                _6 = _4 & _5
                _pc = 5 if _6 != 0 else 6
                continue
            case 5:  # <D.18643>
                return
            case 6:  # L.403
                _7 = v[0]
                _8 = _7 - 1.3e+4
                _9 = _8
                _10 = _div(_9, 2.0e+2)
                xi = _f32(_10 + 1.0e+0)
                _pc = 7 if iv > 27499 else 8
                continue
            case 7:  # <D.18645>
                _11 = v[0]
                _12 = _11 - 2.75e+4
                _13 = _12
                _14 = _div(_13, 5.0e+2)
                xi = _f32(_14 + 5.7e+1)
                _pc = 8
                continue
            case 8:  # L.404
                _15 = xi + 1.00100004673004150390625e+0
                n = _int(_int(_15))
                _16 = _f32(n)
                xd = _f32(xi - _16)
                _17 = _int(n)
                _18 = _17 + -1
                _19 = c4c8_c8[_18]
                _20 = _int(n)
                _21 = _20 + -1
                _22 = c4c8_c8[_21]
                _23 = n + -1
                _24 = _int(_23)
                _25 = _24 + -1
                _26 = c4c8_c8[_25]
                _27 = _22 - _26
                _28 = _27
                _29 = xd * _28
                _30 = _19 + _29
                c8l[0] = _30
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_c6dta(_state, c6l, v):
    D_10231 = _ZERO32
    D_10232 = _ZERO32
    D_10233 = _ZERO32
    D_10231 = _f32(v[0])
    D_10232 = _f32(v[0])
    D_10233 = _f32(D_10232 * D_10232)
    _1 = __builtin_powif(D_10231, 4)
    _2 = D_10233 * 1.084259968e+9
    _3 = 9.380760529301143552e+18 - _2
    _4 = _3
    _5 = _div(_1, _4)
    c6l[0] = _5


def _ft_fudge(_state, v, sumy):
    ya = _ZERO32
    yainv = _ZERO32
    yb = _ZERO32
    ybinv = _ZERO32
    v_25 = _ZERO32
    v_26 = _ZERO32
    v_25 = _f32(v[0])
    _1 = v_25 * 2.74999998509883880615234375e-4
    _2 = -1.72457332611083984375e+1 - _1
    ya = _f32(__builtin_expf(_2))
    v_26 = _f32(v[0])
    _3 = v_26 * 1.300000003539025783538818359375e-3
    _4 = -1.162162494659423828125e+1 - _3
    yb = _f32(__builtin_expf(_4))
    yainv = _f32(_div(1.0e+0, ya))
    ybinv = _f32(_div(1.0e+0, yb))
    _5 = yainv + ybinv
    _6 = _5
    _7 = _div(1.0e+0, _6)
    sumy[0] = _7


def _ft_frn296(_state, v1c, fh2o):
    fh2o_v1 = _state.view(95936, '<f4')
    fh2o_dv = _state.view(95944, '<f4')
    fh2o_npt = _state.view(95948, '<i4')
    fh2o_f296 = _state.view(95952, '<f4')
    _ft_sint(_state, fh2o_v1, v1c, fh2o_dv, fh2o_npt, fh2o_f296, fh2o)


def _ft_sint(_state, v1, v1c, dv, npt, conti, conto):
    i = 0
    imod = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                conto[0] = 0.0
                _1 = v1c[0]
                _2 = v1[0]
                _3 = _1 - _2
                _4 = _3
                _5 = dv[0]
                _6 = _div(_4, _5)
                _7 = _6 + 1.000010013580322265625e+0
                i = _int(_int(_7))
                _8 = npt[0]
                _pc = 1 if i >= _8 else 2
                continue
            case 1:  # <D.18649>
                _pc = -1
                continue
            case 2:  # L.405
                _9 = _int(i)
                _10 = _9 + -1
                _11 = conti[_10]
                conto[0] = _11
                _12 = v1c[0]
                _13 = __builtin_fmodf(_12, 1.0e+1)
                imod = _int(_int(_13))
                _pc = 3 if imod > 0 else -1
                continue
            case 3:  # <D.18651>
                _14 = _int(i)
                _15 = _14 + -1
                _16 = conti[_15]
                _17 = i + 1
                _18 = _int(_17)
                _19 = _18 + -1
                _20 = conti[_19]
                _21 = _16 + _20
                _22 = _21
                _23 = _div(_22, 2.0e+0)
                conto[0] = _23
                _pc = -1
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_slf260(_state, v1c, sh2ot1):
    s260_v1 = _state.view(87904, '<f4')
    s260_dv = _state.view(87912, '<f4')
    s260_npt = _state.view(87916, '<i4')
    s260_s260 = _state.view(87920, '<f4')
    _ft_sint(_state, s260_v1, v1c, s260_dv, s260_npt, s260_s260, sh2ot1)


def _ft_slf296(_state, v1c, sh2ot0):
    sh2o_v1 = _state.view(79872, '<f4')
    sh2o_dv = _state.view(79880, '<f4')
    sh2o_npt = _state.view(79884, '<i4')
    sh2o_s296 = _state.view(79888, '<f4')
    _ft_sint(_state, sh2o_v1, v1c, sh2o_dv, sh2o_npt, sh2o_s296, sh2ot0)


def _ft_abcdta(_state, iv):
    aabbcc_aa = _state.view(245824, '<f4')
    aabbcc_bb = _state.view(245868, '<f4')
    aabbcc_cc = _state.view(245912, '<f4')
    aabbcc_ibnd = _state.view(245956, '<i4')
    aabbcc_a = _state.view(246000, '<f4')
    abc_anh3 = _state.view(2508, '<f4')
    abc_aco2 = _state.view(2516, '<f4')
    abc_aco = _state.view(2556, '<f4')
    abc_ach4 = _state.view(2568, '<f4')
    abc_ano2 = _state.view(2584, '<f4')
    abc_an2o = _state.view(2596, '<f4')
    abc_ao2 = _state.view(2640, '<f4')
    abc_ao3 = _state.view(2664, '<f4')
    abc_aso2 = _state.view(2684, '<f4')
    abc_ah2o = _state.view(2700, '<f4')
    abc_ano = _state.view(2756, '<f4')
    abc_aanh3 = _state.view(2760, '<f4')
    abc_bbnh3 = _state.view(2768, '<f4')
    abc_ccnh3 = _state.view(2776, '<f4')
    abc_aaco2 = _state.view(2784, '<f4')
    abc_bbco2 = _state.view(2824, '<f4')
    abc_ccco2 = _state.view(2864, '<f4')
    abc_aaco = _state.view(2904, '<f4')
    abc_bbco = _state.view(2916, '<f4')
    abc_ccco = _state.view(2928, '<f4')
    abc_aach4 = _state.view(2940, '<f4')
    abc_bbch4 = _state.view(2956, '<f4')
    abc_ccch4 = _state.view(2972, '<f4')
    abc_aano2 = _state.view(2988, '<f4')
    abc_bbno2 = _state.view(3000, '<f4')
    abc_ccno2 = _state.view(3012, '<f4')
    abc_aan2o = _state.view(3024, '<f4')
    abc_bbn2o = _state.view(3068, '<f4')
    abc_ccn2o = _state.view(3112, '<f4')
    abc_aao2 = _state.view(3156, '<f4')
    abc_bbo2 = _state.view(3180, '<f4')
    abc_cco2 = _state.view(3204, '<f4')
    abc_aao3 = _state.view(3228, '<f4')
    abc_bbo3 = _state.view(3248, '<f4')
    abc_cco3 = _state.view(3268, '<f4')
    abc_aaso2 = _state.view(3288, '<f4')
    abc_bbso2 = _state.view(3304, '<f4')
    abc_ccso2 = _state.view(3320, '<f4')
    abc_aah2o = _state.view(3336, '<f4')
    abc_bbh2o = _state.view(3392, '<f4')
    abc_cch2o = _state.view(3448, '<f4')
    abc_aano = _state.view(3504, '<f4')
    abc_bbno = _state.view(3508, '<f4')
    abc_ccno = _state.view(3512, '<f4')
    iband = 0
    imol = 0
    iw = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                imol = _int(1)
                iw = _int(-1)
                _1 = iv[0]
                _2 = _1 >= 0
                _3 = iv[0]
                _4 = _3 <= 345
                _5 = _2 & _4
                _pc = 1 if _5 != 0 else 2
                continue
            case 1:  # <D.18654>
                iw = _int(17)
                _pc = 2
                continue
            case 2:  # L.407
                _6 = iv[0]
                _7 = _6 > 349
                _8 = iv[0]
                _9 = _8 <= 1000
                _10 = _7 & _9
                _pc = 3 if _10 != 0 else 4
                continue
            case 3:  # <D.18657>
                iw = _int(18)
                _pc = 4
                continue
            case 4:  # L.408
                _11 = iv[0]
                _12 = _11 > 1004
                _13 = iv[0]
                _14 = _13 <= 1640
                _15 = _12 & _14
                _pc = 5 if _15 != 0 else 6
                continue
            case 5:  # <D.18660>
                iw = _int(19)
                _pc = 6
                continue
            case 6:  # L.409
                _16 = iv[0]
                _17 = _16 > 1644
                _18 = iv[0]
                _19 = _18 <= 2530
                _20 = _17 & _19
                _pc = 7 if _20 != 0 else 8
                continue
            case 7:  # <D.18663>
                iw = _int(20)
                _pc = 8
                continue
            case 8:  # L.410
                _21 = iv[0]
                _22 = _21 > 2534
                _23 = iv[0]
                _24 = _23 <= 3420
                _25 = _22 & _24
                _pc = 9 if _25 != 0 else 10
                continue
            case 9:  # <D.18666>
                iw = _int(21)
                _pc = 10
                continue
            case 10:  # L.411
                _26 = iv[0]
                _27 = _26 > 3424
                _28 = iv[0]
                _29 = _28 <= 4310
                _30 = _27 & _29
                _pc = 11 if _30 != 0 else 12
                continue
            case 11:  # <D.18669>
                iw = _int(22)
                _pc = 12
                continue
            case 12:  # L.412
                _31 = iv[0]
                _32 = _31 > 4314
                _33 = iv[0]
                _34 = _33 <= 6150
                _35 = _32 & _34
                _pc = 13 if _35 != 0 else 14
                continue
            case 13:  # <D.18672>
                iw = _int(23)
                _pc = 14
                continue
            case 14:  # L.413
                _36 = iv[0]
                _37 = _36 > 6154
                _38 = iv[0]
                _39 = _38 <= 8000
                _40 = _37 & _39
                _pc = 15 if _40 != 0 else 16
                continue
            case 15:  # <D.18675>
                iw = _int(24)
                _pc = 16
                continue
            case 16:  # L.414
                _41 = iv[0]
                _42 = _41 > 8004
                _43 = iv[0]
                _44 = _43 <= 9615
                _45 = _42 & _44
                _pc = 17 if _45 != 0 else 18
                continue
            case 17:  # <D.18678>
                iw = _int(25)
                _pc = 18
                continue
            case 18:  # L.415
                _46 = iv[0]
                _47 = _46 > 9619
                _48 = iv[0]
                _49 = _48 <= 11540
                _50 = _47 & _49
                _pc = 19 if _50 != 0 else 20
                continue
            case 19:  # <D.18681>
                iw = _int(26)
                _pc = 20
                continue
            case 20:  # L.416
                _51 = iv[0]
                _52 = _51 > 11544
                _53 = iv[0]
                _54 = _53 <= 13070
                _55 = _52 & _54
                _pc = 21 if _55 != 0 else 22
                continue
            case 21:  # <D.18684>
                iw = _int(27)
                _pc = 22
                continue
            case 22:  # L.417
                _56 = iv[0]
                _57 = _56 > 13074
                _58 = iv[0]
                _59 = _58 <= 14860
                _60 = _57 & _59
                _pc = 23 if _60 != 0 else 24
                continue
            case 23:  # <D.18687>
                iw = _int(28)
                _pc = 24
                continue
            case 24:  # L.418
                _61 = iv[0]
                _62 = _61 > 14864
                _63 = iv[0]
                _64 = _63 <= 16045
                _65 = _62 & _64
                _pc = 25 if _65 != 0 else 26
                continue
            case 25:  # <D.18690>
                iw = _int(29)
                _pc = 26
                continue
            case 26:  # L.419
                _66 = iv[0]
                _67 = _66 > 16339
                _68 = iv[0]
                _69 = _68 <= 17860
                _70 = _67 & _69
                _pc = 27 if _70 != 0 else 28
                continue
            case 27:  # <D.18693>
                iw = _int(30)
                _pc = 28
                continue
            case 28:  # L.420
                iband = _int(iw + -16)
                _71 = _int(imol)
                _72 = _71 + -1
                aabbcc_ibnd[_72] = iw
                _pc = 29 if iw > 0 else 30
                continue
            case 29:  # <D.18696>
                _73 = _int(iband)
                _74 = _73 + -1
                _75 = _int(imol)
                _76 = _75 + -1
                _77 = abc_ah2o[_74]
                aabbcc_a[_76] = _77
                _78 = _int(iband)
                _79 = _78 + -1
                _80 = _int(imol)
                _81 = _80 + -1
                _82 = abc_aah2o[_79]
                aabbcc_aa[_81] = _82
                _83 = _int(iband)
                _84 = _83 + -1
                _85 = _int(imol)
                _86 = _85 + -1
                _87 = abc_bbh2o[_84]
                aabbcc_bb[_86] = _87
                _88 = _int(iband)
                _89 = _88 + -1
                _90 = _int(imol)
                _91 = _90 + -1
                _92 = abc_cch2o[_89]
                aabbcc_cc[_91] = _92
                _pc = 30
                continue
            case 30:  # L.421
                imol = _int(3)
                iw = _int(-1)
                _93 = iv[0]
                _94 = _93 >= 0
                _95 = iv[0]
                _96 = _95 <= 200
                _97 = _94 & _96
                _pc = 31 if _97 != 0 else 32
                continue
            case 31:  # <D.18699>
                iw = _int(31)
                _pc = 32
                continue
            case 32:  # L.422
                _98 = iv[0]
                _99 = _98 > 514
                _100 = iv[0]
                _101 = _100 <= 1275
                _102 = _99 & _101
                _pc = 33 if _102 != 0 else 34
                continue
            case 33:  # <D.18702>
                iw = _int(32)
                _pc = 34
                continue
            case 34:  # L.423
                _103 = iv[0]
                _104 = _103 > 1629
                _105 = iv[0]
                _106 = _105 <= 2295
                _107 = _104 & _106
                _pc = 35 if _107 != 0 else 36
                continue
            case 35:  # <D.18705>
                iw = _int(33)
                _pc = 36
                continue
            case 36:  # L.424
                _108 = iv[0]
                _109 = _108 > 2669
                _110 = iv[0]
                _111 = _110 <= 2845
                _112 = _109 & _111
                _pc = 37 if _112 != 0 else 38
                continue
            case 37:  # <D.18708>
                iw = _int(34)
                _pc = 38
                continue
            case 38:  # L.425
                _113 = iv[0]
                _114 = _113 > 2849
                _115 = iv[0]
                _116 = _115 <= 3260
                _117 = _114 & _116
                _pc = 39 if _117 != 0 else 40
                continue
            case 39:  # <D.18711>
                iw = _int(35)
                _pc = 40
                continue
            case 40:  # L.426
                iband = _int(iw + -30)
                _118 = _int(imol)
                _119 = _118 + -1
                aabbcc_ibnd[_119] = iw
                _pc = 41 if iw > 0 else 42
                continue
            case 41:  # <D.18714>
                _120 = _int(iband)
                _121 = _120 + -1
                _122 = _int(imol)
                _123 = _122 + -1
                _124 = abc_ao3[_121]
                aabbcc_a[_123] = _124
                _125 = _int(iband)
                _126 = _125 + -1
                _127 = _int(imol)
                _128 = _127 + -1
                _129 = abc_aao3[_126]
                aabbcc_aa[_128] = _129
                _130 = _int(iband)
                _131 = _130 + -1
                _132 = _int(imol)
                _133 = _132 + -1
                _134 = abc_bbo3[_131]
                aabbcc_bb[_133] = _134
                _135 = _int(iband)
                _136 = _135 + -1
                _137 = _int(imol)
                _138 = _137 + -1
                _139 = abc_cco3[_136]
                aabbcc_cc[_138] = _139
                _pc = 42
                continue
            case 42:  # L.427
                imol = _int(2)
                iw = _int(-1)
                _140 = iv[0]
                _141 = _140 > 424
                _142 = iv[0]
                _143 = _142 <= 835
                _144 = _141 & _143
                _pc = 43 if _144 != 0 else 44
                continue
            case 43:  # <D.18717>
                iw = _int(36)
                _pc = 44
                continue
            case 44:  # L.428
                _145 = iv[0]
                _146 = _145 > 839
                _147 = iv[0]
                _148 = _147 <= 1440
                _149 = _146 & _148
                _pc = 45 if _149 != 0 else 46
                continue
            case 45:  # <D.18720>
                iw = _int(37)
                _pc = 46
                continue
            case 46:  # L.429
                _150 = iv[0]
                _151 = _150 > 1804
                _152 = iv[0]
                _153 = _152 <= 2855
                _154 = _151 & _153
                _pc = 47 if _154 != 0 else 48
                continue
            case 47:  # <D.18723>
                iw = _int(38)
                _pc = 48
                continue
            case 48:  # L.430
                _155 = iv[0]
                _156 = _155 > 3069
                _157 = iv[0]
                _158 = _157 <= 3755
                _159 = _156 & _158
                _pc = 49 if _159 != 0 else 50
                continue
            case 49:  # <D.18726>
                iw = _int(39)
                _pc = 50
                continue
            case 50:  # L.431
                _160 = iv[0]
                _161 = _160 > 3759
                _162 = iv[0]
                _163 = _162 <= 4065
                _164 = _161 & _163
                _pc = 51 if _164 != 0 else 52
                continue
            case 51:  # <D.18729>
                iw = _int(40)
                _pc = 52
                continue
            case 52:  # L.432
                _165 = iv[0]
                _166 = _165 > 4529
                _167 = iv[0]
                _168 = _167 <= 5380
                _169 = _166 & _168
                _pc = 53 if _169 != 0 else 54
                continue
            case 53:  # <D.18732>
                iw = _int(41)
                _pc = 54
                continue
            case 54:  # L.433
                _170 = iv[0]
                _171 = _170 > 5904
                _172 = iv[0]
                _173 = _172 <= 7025
                _174 = _171 & _173
                _pc = 55 if _174 != 0 else 56
                continue
            case 55:  # <D.18735>
                iw = _int(42)
                _pc = 56
                continue
            case 56:  # L.434
                _175 = iv[0]
                _176 = _175 > 7394
                _177 = iv[0]
                _178 = _177 <= 7785
                _179 = _176 & _178
                _180 = iv[0]
                _181 = _180 > 8029
                _182 = iv[0]
                _183 = _182 <= 8335
                _184 = _181 & _183
                _185 = _179 | _184
                _186 = iv[0]
                _187 = _186 > 9339
                _188 = iv[0]
                _189 = _188 <= 9670
                _190 = _187 & _189
                _191 = _185 | _190
                _pc = 57 if _191 != 0 else 58
                continue
            case 57:  # <D.18738>
                iw = _int(43)
                _pc = 58
                continue
            case 58:  # L.435
                iband = _int(iw + -35)
                _192 = _int(imol)
                _193 = _192 + -1
                aabbcc_ibnd[_193] = iw
                _pc = 59 if iw > 0 else 60
                continue
            case 59:  # <D.18741>
                _194 = _int(iband)
                _195 = _194 + -1
                _196 = _int(imol)
                _197 = _196 + -1
                _198 = abc_aco2[_195]
                aabbcc_a[_197] = _198
                _199 = _int(iband)
                _200 = _199 + -1
                _201 = _int(imol)
                _202 = _201 + -1
                _203 = abc_aaco2[_200]
                aabbcc_aa[_202] = _203
                _204 = _int(iband)
                _205 = _204 + -1
                _206 = _int(imol)
                _207 = _206 + -1
                _208 = abc_bbco2[_205]
                aabbcc_bb[_207] = _208
                _209 = _int(iband)
                _210 = _209 + -1
                _211 = _int(imol)
                _212 = _211 + -1
                _213 = abc_ccco2[_210]
                aabbcc_cc[_212] = _213
                _pc = 60
                continue
            case 60:  # L.436
                imol = _int(5)
                iw = _int(-1)
                _214 = iv[0]
                _215 = _214 >= 0
                _216 = iv[0]
                _217 = _216 <= 175
                _218 = _215 & _217
                _pc = 61 if _218 != 0 else 62
                continue
            case 61:  # <D.18744>
                iw = _int(44)
                _pc = 62
                continue
            case 62:  # L.437
                _219 = iv[0]
                _220 = _219 > 1939
                _221 = iv[0]
                _222 = _221 <= 2285
                _223 = _220 & _222
                _224 = iv[0]
                _225 = _224 > 4039
                _226 = iv[0]
                _227 = _226 <= 4370
                _228 = _225 & _227
                _229 = _223 | _228
                _pc = 63 if _229 != 0 else 64
                continue
            case 63:  # <D.18747>
                iw = _int(45)
                _pc = 64
                continue
            case 64:  # L.438
                iband = _int(iw + -43)
                _230 = _int(imol)
                _231 = _230 + -1
                aabbcc_ibnd[_231] = iw
                _pc = 65 if iw > 0 else 66
                continue
            case 65:  # <D.18750>
                _232 = _int(iband)
                _233 = _232 + -1
                _234 = _int(imol)
                _235 = _234 + -1
                _236 = abc_aco[_233]
                aabbcc_a[_235] = _236
                _237 = _int(iband)
                _238 = _237 + -1
                _239 = _int(imol)
                _240 = _239 + -1
                _241 = abc_aaco[_238]
                aabbcc_aa[_240] = _241
                _242 = _int(iband)
                _243 = _242 + -1
                _244 = _int(imol)
                _245 = _244 + -1
                _246 = abc_bbco[_243]
                aabbcc_bb[_245] = _246
                _247 = _int(iband)
                _248 = _247 + -1
                _249 = _int(imol)
                _250 = _249 + -1
                _251 = abc_ccco[_248]
                aabbcc_cc[_250] = _251
                _pc = 66
                continue
            case 66:  # L.439
                imol = _int(6)
                iw = _int(-1)
                _252 = iv[0]
                _253 = _252 > 1064
                _254 = iv[0]
                _255 = _254 <= 1775
                _256 = _253 & _255
                _257 = iv[0]
                _258 = _257 > 2344
                _259 = iv[0]
                _260 = _259 <= 3230
                _261 = _258 & _260
                _262 = _256 | _261
                _263 = iv[0]
                _264 = _263 > 4109
                _265 = iv[0]
                _266 = _265 <= 4690
                _267 = _264 & _266
                _268 = _262 | _267
                _269 = iv[0]
                _270 = _269 > 5864
                _271 = iv[0]
                _272 = _271 <= 6135
                _273 = _270 & _272
                _274 = _268 | _273
                _pc = 67 if _274 != 0 else 68
                continue
            case 67:  # <D.18753>
                iw = _int(46)
                _pc = 68
                continue
            case 68:  # L.440
                iband = _int(iw + -45)
                _275 = _int(imol)
                _276 = _275 + -1
                aabbcc_ibnd[_276] = iw
                _pc = 69 if iw > 0 else 70
                continue
            case 69:  # <D.18756>
                _277 = _int(iband)
                _278 = _277 + -1
                _279 = _int(imol)
                _280 = _279 + -1
                _281 = abc_ach4[_278]
                aabbcc_a[_280] = _281
                _282 = _int(iband)
                _283 = _282 + -1
                _284 = _int(imol)
                _285 = _284 + -1
                _286 = abc_aach4[_283]
                aabbcc_aa[_285] = _286
                _287 = _int(iband)
                _288 = _287 + -1
                _289 = _int(imol)
                _290 = _289 + -1
                _291 = abc_bbch4[_288]
                aabbcc_bb[_290] = _291
                _292 = _int(iband)
                _293 = _292 + -1
                _294 = _int(imol)
                _295 = _294 + -1
                _296 = abc_ccch4[_293]
                aabbcc_cc[_295] = _296
                _pc = 70
                continue
            case 70:  # L.441
                imol = _int(4)
                iw = _int(-1)
                _297 = iv[0]
                _298 = _297 >= 0
                _299 = iv[0]
                _300 = _299 <= 120
                _301 = _298 & _300
                _pc = 71 if _301 != 0 else 72
                continue
            case 71:  # <D.18759>
                iw = _int(47)
                _pc = 72
                continue
            case 72:  # L.442
                _302 = iv[0]
                _303 = _302 > 489
                _304 = iv[0]
                _305 = _304 <= 775
                _306 = _303 & _305
                _307 = iv[0]
                _308 = _307 > 864
                _309 = iv[0]
                _310 = _309 <= 995
                _311 = _308 & _310
                _312 = _306 | _311
                _313 = iv[0]
                _314 = _313 > 1064
                _315 = iv[0]
                _316 = _315 <= 1385
                _317 = _314 & _316
                _318 = _312 | _317
                _319 = iv[0]
                _320 = _319 > 1544
                _321 = iv[0]
                _322 = _321 <= 2040
                _323 = _320 & _322
                _324 = _318 | _323
                _325 = iv[0]
                _326 = _325 > 2089
                _327 = iv[0]
                _328 = _327 <= 2655
                _329 = _326 & _328
                _330 = _324 | _329
                _pc = 73 if _330 != 0 else 74
                continue
            case 73:  # <D.18762>
                iw = _int(48)
                _pc = 74
                continue
            case 74:  # L.443
                _331 = iv[0]
                _332 = _331 > 2704
                _333 = iv[0]
                _334 = _333 <= 2865
                _335 = _332 & _334
                _336 = iv[0]
                _337 = _336 > 3244
                _338 = iv[0]
                _339 = _338 <= 3925
                _340 = _337 & _339
                _341 = _335 | _340
                _342 = iv[0]
                _343 = _342 > 4259
                _344 = iv[0]
                _345 = _344 <= 4470
                _346 = _343 & _345
                _347 = _341 | _346
                _348 = iv[0]
                _349 = _348 > 4539
                _350 = iv[0]
                _351 = _350 <= 4785
                _352 = _349 & _351
                _353 = _347 | _352
                _354 = iv[0]
                _355 = _354 > 4909
                _356 = iv[0]
                _357 = _356 <= 5165
                _358 = _355 & _357
                _359 = _353 | _358
                _pc = 75 if _359 != 0 else 76
                continue
            case 75:  # <D.18765>
                iw = _int(49)
                _pc = 76
                continue
            case 76:  # L.444
                iband = _int(iw + -46)
                _360 = _int(imol)
                _361 = _360 + -1
                aabbcc_ibnd[_361] = iw
                _pc = 77 if iw > 0 else 78
                continue
            case 77:  # <D.18768>
                _362 = _int(iband)
                _363 = _362 + -1
                _364 = _int(imol)
                _365 = _364 + -1
                _366 = abc_an2o[_363]
                aabbcc_a[_365] = _366
                _367 = _int(iband)
                _368 = _367 + -1
                _369 = _int(imol)
                _370 = _369 + -1
                _371 = abc_aan2o[_368]
                aabbcc_aa[_370] = _371
                _372 = _int(iband)
                _373 = _372 + -1
                _374 = _int(imol)
                _375 = _374 + -1
                _376 = abc_bbn2o[_373]
                aabbcc_bb[_375] = _376
                _377 = _int(iband)
                _378 = _377 + -1
                _379 = _int(imol)
                _380 = _379 + -1
                _381 = abc_ccn2o[_378]
                aabbcc_cc[_380] = _381
                _pc = 78
                continue
            case 78:  # L.445
                imol = _int(7)
                iw = _int(-1)
                _382 = iv[0]
                _383 = _382 >= 0
                _384 = iv[0]
                _385 = _384 <= 265
                _386 = _383 & _385
                _pc = 79 if _386 != 0 else 80
                continue
            case 79:  # <D.18771>
                iw = _int(50)
                _pc = 80
                continue
            case 80:  # L.446
                _387 = iv[0]
                _388 = _387 > 7649
                _389 = iv[0]
                _390 = _389 <= 8080
                _391 = _388 & _390
                _392 = iv[0]
                _393 = _392 > 9234
                _394 = iv[0]
                _395 = _394 <= 9490
                _396 = _393 & _395
                _397 = _391 | _396
                _398 = iv[0]
                _399 = _398 > 12849
                _400 = iv[0]
                _401 = _400 <= 13220
                _402 = _399 & _401
                _403 = _397 | _402
                _404 = iv[0]
                _405 = _404 > 14299
                _406 = iv[0]
                _407 = _406 <= 14600
                _408 = _405 & _407
                _409 = _403 | _408
                _410 = iv[0]
                _411 = _410 > 15694
                _412 = iv[0]
                _413 = _412 <= 15955
                _414 = _411 & _413
                _415 = _409 | _414
                _pc = 81 if _415 != 0 else 82
                continue
            case 81:  # <D.18774>
                iw = _int(51)
                _pc = 82
                continue
            case 82:  # L.447
                _416 = iv[0]
                _417 = _416 > 49599
                _418 = iv[0]
                _419 = _418 <= 52710
                _420 = _417 & _419
                _pc = 83 if _420 != 0 else 84
                continue
            case 83:  # <D.18777>
                iw = _int(51)
                _pc = 84
                continue
            case 84:  # L.448
                iband = _int(iw + -49)
                _421 = _int(imol)
                _422 = _421 + -1
                aabbcc_ibnd[_422] = iw
                _pc = 85 if iw > 0 else 88
                continue
            case 85:  # <D.18780>
                _423 = _int(iband)
                _424 = _423 + -1
                _425 = _int(imol)
                _426 = _425 + -1
                _427 = abc_ao2[_424]
                aabbcc_a[_426] = _427
                _428 = iv[0]
                _429 = _428 > 49599
                _430 = iv[0]
                _431 = _430 <= 52710
                _432 = _429 & _431
                _pc = 86 if _432 != 0 else 87
                continue
            case 86:  # <D.18782>
                _433 = _int(imol)
                _434 = _433 + -1
                aabbcc_a[_434] = 4.704000055789947509765625e-1
                _pc = 87
                continue
            case 87:  # L.450
                _435 = _int(iband)
                _436 = _435 + -1
                _437 = _int(imol)
                _438 = _437 + -1
                _439 = abc_aao2[_436]
                aabbcc_aa[_438] = _439
                _440 = _int(iband)
                _441 = _440 + -1
                _442 = _int(imol)
                _443 = _442 + -1
                _444 = abc_bbo2[_441]
                aabbcc_bb[_443] = _444
                _445 = _int(iband)
                _446 = _445 + -1
                _447 = _int(imol)
                _448 = _447 + -1
                _449 = abc_cco2[_446]
                aabbcc_cc[_448] = _449
                _pc = 88
                continue
            case 88:  # L.449
                imol = _int(11)
                iw = _int(-1)
                _450 = iv[0]
                _451 = _450 >= 0
                _452 = iv[0]
                _453 = _452 <= 385
                _454 = _451 & _453
                _pc = 89 if _454 != 0 else 90
                continue
            case 89:  # <D.18786>
                iw = _int(52)
                _pc = 90
                continue
            case 90:  # L.451
                _455 = iv[0]
                _456 = _455 > 389
                _457 = iv[0]
                _458 = _457 <= 2150
                _459 = _456 & _458
                _pc = 91 if _459 != 0 else 92
                continue
            case 91:  # <D.18789>
                iw = _int(53)
                _pc = 92
                continue
            case 92:  # L.452
                iband = _int(iw + -51)
                _460 = _int(imol)
                _461 = _460 + -1
                aabbcc_ibnd[_461] = iw
                _pc = 93 if iw > 0 else 94
                continue
            case 93:  # <D.18792>
                _462 = _int(iband)
                _463 = _462 + -1
                _464 = _int(imol)
                _465 = _464 + -1
                _466 = abc_anh3[_463]
                aabbcc_a[_465] = _466
                _467 = _int(iband)
                _468 = _467 + -1
                _469 = _int(imol)
                _470 = _469 + -1
                _471 = abc_aanh3[_468]
                aabbcc_aa[_470] = _471
                _472 = _int(iband)
                _473 = _472 + -1
                _474 = _int(imol)
                _475 = _474 + -1
                _476 = abc_bbnh3[_473]
                aabbcc_bb[_475] = _476
                _477 = _int(iband)
                _478 = _477 + -1
                _479 = _int(imol)
                _480 = _479 + -1
                _481 = abc_ccnh3[_478]
                aabbcc_cc[_480] = _481
                _pc = 94
                continue
            case 94:  # L.453
                imol = _int(8)
                iw = _int(-1)
                _482 = iv[0]
                _483 = _482 > 1699
                _484 = iv[0]
                _485 = _484 <= 2005
                _486 = _483 & _485
                _pc = 95 if _486 != 0 else 96
                continue
            case 95:  # <D.18795>
                iw = _int(54)
                _pc = 96
                continue
            case 96:  # L.454
                iband = _int(iw + -53)
                _487 = _int(imol)
                _488 = _487 + -1
                aabbcc_ibnd[_488] = iw
                _pc = 97 if iw > 0 else 98
                continue
            case 97:  # <D.18798>
                _489 = _int(imol)
                _490 = _489 + -1
                _491 = abc_ano[0]
                aabbcc_a[_490] = _491
                _492 = _int(imol)
                _493 = _492 + -1
                _494 = abc_aano[0]
                aabbcc_aa[_493] = _494
                _495 = _int(imol)
                _496 = _495 + -1
                _497 = abc_bbno[0]
                aabbcc_bb[_496] = _497
                _498 = _int(imol)
                _499 = _498 + -1
                _500 = abc_ccno[0]
                aabbcc_cc[_499] = _500
                _pc = 98
                continue
            case 98:  # L.455
                iw = _int(-1)
                imol = _int(10)
                _501 = iv[0]
                _502 = _501 > 579
                _503 = iv[0]
                _504 = _503 <= 925
                _505 = _502 & _504
                _506 = iv[0]
                _507 = _506 > 1514
                _508 = iv[0]
                _509 = _508 <= 1695
                _510 = _507 & _509
                _511 = _505 | _510
                _512 = iv[0]
                _513 = _512 > 2799
                _514 = iv[0]
                _515 = _514 <= 2970
                _516 = _513 & _515
                _517 = _511 | _516
                _pc = 99 if _517 != 0 else 100
                continue
            case 99:  # <D.18801>
                iw = _int(55)
                _pc = 100
                continue
            case 100:  # L.456
                iband = _int(iw + -54)
                _518 = _int(imol)
                _519 = _518 + -1
                aabbcc_ibnd[_519] = iw
                _pc = 101 if iw > 0 else 102
                continue
            case 101:  # <D.18804>
                _520 = _int(iband)
                _521 = _520 + -1
                _522 = _int(imol)
                _523 = _522 + -1
                _524 = abc_ano2[_521]
                aabbcc_a[_523] = _524
                _525 = _int(iband)
                _526 = _525 + -1
                _527 = _int(imol)
                _528 = _527 + -1
                _529 = abc_aano2[_526]
                aabbcc_aa[_528] = _529
                _530 = _int(iband)
                _531 = _530 + -1
                _532 = _int(imol)
                _533 = _532 + -1
                _534 = abc_bbno2[_531]
                aabbcc_bb[_533] = _534
                _535 = _int(iband)
                _536 = _535 + -1
                _537 = _int(imol)
                _538 = _537 + -1
                _539 = abc_ccno2[_536]
                aabbcc_cc[_538] = _539
                _pc = 102
                continue
            case 102:  # L.457
                imol = _int(9)
                iw = _int(-1)
                _540 = iv[0]
                _541 = _540 >= 0
                _542 = iv[0]
                _543 = _542 <= 185
                _544 = _541 & _543
                _pc = 103 if _544 != 0 else 104
                continue
            case 103:  # <D.18807>
                iw = _int(56)
                _pc = 104
                continue
            case 104:  # L.458
                _545 = iv[0]
                _546 = _545 > 399
                _547 = iv[0]
                _548 = _547 <= 650
                _549 = _546 & _548
                _550 = iv[0]
                _551 = _550 > 949
                _552 = iv[0]
                _553 = _552 <= 1460
                _554 = _551 & _553
                _555 = _549 | _554
                _556 = iv[0]
                _557 = _556 > 2414
                _558 = iv[0]
                _559 = _558 <= 2580
                _560 = _557 & _559
                _561 = _555 | _560
                _pc = 105 if _561 != 0 else 106
                continue
            case 105:  # <D.18810>
                iw = _int(57)
                _pc = 106
                continue
            case 106:  # L.459
                iband = _int(iw + -55)
                _562 = _int(imol)
                _563 = _562 + -1
                aabbcc_ibnd[_563] = iw
                _pc = 107 if iw > 0 else -1
                continue
            case 107:  # <D.18813>
                _564 = _int(iband)
                _565 = _564 + -1
                _566 = _int(imol)
                _567 = _566 + -1
                _568 = abc_aso2[_565]
                aabbcc_a[_567] = _568
                _569 = _int(iband)
                _570 = _569 + -1
                _571 = _int(imol)
                _572 = _571 + -1
                _573 = abc_aaso2[_570]
                aabbcc_aa[_572] = _573
                _574 = _int(iband)
                _575 = _574 + -1
                _576 = _int(imol)
                _577 = _576 + -1
                _578 = abc_bbso2[_575]
                aabbcc_bb[_577] = _578
                _579 = _int(iband)
                _580 = _579 + -1
                _581 = _int(imol)
                _582 = _581 + -1
                _583 = abc_ccso2[_580]
                aabbcc_cc[_582] = _583
                _pc = -1
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_c4dta(_state, c4l, v):
    c4c8_c4 = _state.view(103968, '<f4')
    iv = 0
    l = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                c4l[0] = 0.0
                _1 = v[0]
                _pc = 1 if _1 < 2.08e+3 else 2
                continue
            case 1:  # <D.18816>
                return
            case 2:  # L.461
                _2 = v[0]
                _pc = 3 if _2 > 2.74e+3 else 4
                continue
            case 3:  # <D.18818>
                return
            case 4:  # L.462
                _3 = v[0]
                iv = _int(_int(_3))
                _4 = iv + -2080
                _5 = _div(_4, 5)
                l = _int(_5 + 1)
                _6 = _int(l)
                _7 = _6 + -1
                _8 = c4c8_c4[_7]
                c4l[0] = _8
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_cxdta(_state, cprime, v, iwl, iwh, cp, ind):
    i = 0
    ic = 0
    indm1 = 0
    iv = 0
    D_10558 = 0
    D_10561 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = v[0]
                iv = _int(_int(_1))
                cprime[0] = -2.0e+1
                _2 = ind[0]
                _3 = _2 + 1
                _4 = _int(_3)
                _5 = _4 + -1
                _6 = iwl[_5]
                _7 = _6 == -999
                _8 = ind[0]
                _9 = _int(_8)
                _10 = _9 + -1
                _11 = iwh[_10]
                _12 = iv > _11
                _13 = _7 & _12
                _pc = 1 if _13 != 0 else 2
                continue
            case 1:  # <D.18821>
                return
            case 2:  # L.463
                _14 = iwl[0]
                _pc = 3 if iv < _14 else 4
                continue
            case 3:  # <D.18823>
                return
            case 4:  # L.464
                ic = _int(0)
                _pc = 5
            case 5:  # __label_000100
                _15 = ind[0]
                _16 = _int(_15)
                _17 = _16 + -1
                _18 = iwl[_17]
                _19 = iv >= _18
                _20 = ind[0]
                _21 = _int(_20)
                _22 = _21 + -1
                _23 = iwh[_22]
                _24 = iv <= _23
                _25 = _19 & _24
                _pc = 6 if _25 != 0 else 7
                continue
            case 6:  # <D.18825>
                _pc = 14
                continue
            case 7:  # L.465
                _26 = ind[0]
                _27 = _int(_26)
                _28 = _27 + -1
                _29 = iwh[_28]
                _30 = iv > _29
                _31 = ind[0]
                _32 = _31 + 1
                _33 = _int(_32)
                _34 = _33 + -1
                _35 = iwl[_34]
                _36 = iv < _35
                _37 = _30 & _36
                _pc = 8 if _37 != 0 else 9
                continue
            case 8:  # <D.18827>
                return
            case 9:  # L.466
                _38 = ind[0]
                _39 = _38 + 1
                ind[0] = _39
                _40 = ind[0]
                _41 = _int(_40)
                _42 = _41 + -1
                _43 = iwl[_42]
                _pc = 10 if _43 != -999 else 11
                continue
            case 10:  # <D.18829>
                _pc = 5
                continue
            case 11:  # L.467
                _44 = ind[0]
                _45 = _44 + -1
                ind[0] = _45
                _46 = ind[0]
                _47 = _int(_46)
                _48 = _47 + -1
                _49 = iwh[_48]
                _pc = 12 if iv > _49 else 13
                continue
            case 12:  # <D.18831>
                return
            case 13:  # L.468
                ind[0] = 1
                _pc = 5
                continue
            case 14:  # __label_000200
                _50 = ind[0]
                _pc = 15 if _50 == 1 else 16
                continue
            case 15:  # <D.18833>
                _pc = 20
                continue
            case 16:  # L.469
                _51 = ind[0]
                indm1 = _int(_51 + -1)
                D_10558 = _int(indm1)
                i = _int(1)
                _pc = 17
            case 17:  # <D.18835>
                D_10561 = _int(i > D_10558)
                _pc = 20 if D_10561 != 0 else 18
                continue
            case 18:  # <D.18836>
                _52 = _int(i)
                _53 = _52 + -1
                _54 = iwh[_53]
                _55 = _int(i)
                _56 = _55 + -1
                _57 = iwl[_56]
                _58 = _54 - _57
                _59 = _div(_58, 5)
                _60 = ic + _59
                ic = _int(_60 + 1)
                _pc = 19
            case 19:  # L.470
                i = _int(i + 1)
                _pc = 17
                continue
            case 20:  # __label_000400
                _61 = ind[0]
                _62 = _int(_61)
                _63 = _62 + -1
                _64 = iwl[_63]
                _65 = iv - _64
                _66 = _div(_65, 5)
                _67 = ic + _66
                ic = _int(_67 + 1)
                _68 = _int(ic)
                _69 = _68 + -1
                _70 = cp[_69]
                cprime[0] = _70
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_mapms(_state, ml, ikmax, zm, aht, imap):
    i = 0
    j = 0
    D_10565 = 0
    D_10568 = 0
    D_10569 = 0
    D_10572 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                D_10565 = _int(ikmax[0])
                j = _int(1)
                _pc = 1
            case 1:  # <D.18838>
                D_10568 = _int(j > D_10565)
                _pc = -1 if D_10568 != 0 else 2
                continue
            case 2:  # <D.18839>
                D_10569 = _int(ml[0])
                i = _int(1)
                _pc = 3
            case 3:  # <D.18840>
                D_10572 = _int(i > D_10569)
                _pc = 8 if D_10572 != 0 else 4
                continue
            case 4:  # <D.18841>
                _1 = _int(i)
                _2 = _1 + -1
                _3 = zm[_2]
                _4 = _int(j)
                _5 = _4 + -1
                _6 = aht[_5]
                _pc = 5 if _3 > _6 else 6
                continue
            case 5:  # <D.18842>
                _pc = 8
                continue
            case 6:  # L.476
                _7 = _int(j)
                _8 = _7 + -1
                imap[_8] = i
                _pc = 7
            case 7:  # L.474
                i = _int(i + 1)
                _pc = 3
                continue
            case 8:  # L.472
                j = _int(j + 1)
                _pc = 1
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_equlwc(_state):
    __BLNK___awccon = _state.view(286844, '<f4')
    cntrl_ml = _state.view(245616, '<i4')
    model_densty = _state.view(232448, '<f4')
    model_eqlwc = _state.view(241288, '<f4')
    i = 0
    D_10661 = 0
    D_10664 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                D_10661 = _int(cntrl_ml[0])
                i = _int(1)
                _pc = 1
            case 1:  # <D.18844>
                D_10664 = _int(i > D_10661)
                _pc = -1 if D_10664 != 0 else 2
                continue
            case 2:  # <D.18845>
                _1 = _int(i)
                _2 = _1 * 63
                _3 = _2 + -57
                _4 = model_densty[_3]
                _pc = 3 if _4 != 0.0 else 4
                continue
            case 3:  # <D.18846>
                _5 = _int(i)
                _6 = _5 * 63
                _7 = _6 + -57
                _8 = model_densty[_7]
                _9 = __BLNK___awccon[0]
                _10 = _int(i)
                _11 = _10 + -1
                _12 = _8 * _9
                model_eqlwc[_11] = _12
                _pc = 4
                continue
            case 4:  # L.479
                _13 = _int(i)
                _14 = _13 * 63
                _15 = _14 + -52
                _16 = model_densty[_15]
                _pc = 5 if _16 != 0.0 else 6
                continue
            case 5:  # <D.18849>
                _17 = _int(i)
                _18 = _17 * 63
                _19 = _18 + -52
                _20 = model_densty[_19]
                _21 = __BLNK___awccon[1]
                _22 = _int(i)
                _23 = _22 + -1
                _24 = _20 * _21
                model_eqlwc[_23] = _24
                _pc = 6
                continue
            case 6:  # L.480
                _25 = _int(i)
                _26 = _25 * 63
                _27 = _26 + -51
                _28 = model_densty[_27]
                _pc = 7 if _28 != 0.0 else 8
                continue
            case 7:  # <D.18852>
                _29 = _int(i)
                _30 = _29 * 63
                _31 = _30 + -51
                _32 = model_densty[_31]
                _33 = __BLNK___awccon[2]
                _34 = _int(i)
                _35 = _34 + -1
                _36 = _32 * _33
                model_eqlwc[_35] = _36
                _pc = 8
                continue
            case 8:  # L.481
                _37 = _int(i)
                _38 = _37 * 63
                _39 = _38 + -50
                _40 = model_densty[_39]
                _pc = 9 if _40 != 0.0 else 10
                continue
            case 9:  # <D.18855>
                _41 = _int(i)
                _42 = _41 * 63
                _43 = _42 + -50
                _44 = model_densty[_43]
                _45 = __BLNK___awccon[3]
                _46 = _int(i)
                _47 = _46 + -1
                _48 = _44 * _45
                model_eqlwc[_47] = _48
                _pc = 10
                continue
            case 10:  # L.477
                i = _int(i + 1)
                _pc = 1
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_exabin(_state):
    __BLNK___ich = _state.view(265840, '<i4')
    __BLNK___w = _state.view(266176, '<f4')
    __BLNK___absc = _state.view(283836, '<f4')
    __BLNK___extc = _state.view(284776, '<f4')
    __BLNK___asym = _state.view(285716, '<f4')
    __BLNK___vx0 = _state.view(286656, '<f4')
    __BLNK___awccon = _state.view(286844, '<f4')
    card2_icld = _state.view(231760, '<i4')
    card2d_ireg = _state.view(214080, '<i4')
    card2d_iregc = _state.view(214112, '<i4')
    cirr_ci32xt = _state.view(63296, '<f4')
    cirr_ci32ab = _state.view(63484, '<f4')
    cirr_ci32g = _state.view(63672, '<f4')
    cirr_cir2xt = _state.view(63860, '<f4')
    cirr_cir2ab = _state.view(64048, '<f4')
    cirr_cir2g = _state.view(64236, '<f4')
    extd_vx2 = _state.view(64448, '<f4')
    extd_rurext = _state.view(64636, '<f4')
    extd_rurabs = _state.view(65388, '<f4')
    extd_rursym = _state.view(66140, '<f4')
    extd_urbext = _state.view(66892, '<f4')
    extd_urbabs = _state.view(67644, '<f4')
    extd_urbsym = _state.view(68396, '<f4')
    extd_ocnext = _state.view(69148, '<f4')
    extd_ocnabs = _state.view(69900, '<f4')
    extd_ocnsym = _state.view(70652, '<f4')
    extd_troext = _state.view(71404, '<f4')
    extd_troabs = _state.view(72156, '<f4')
    extd_trosym = _state.view(72908, '<f4')
    extd_fg1ext = _state.view(73660, '<f4')
    extd_fg1abs = _state.view(73848, '<f4')
    extd_fg1sym = _state.view(74036, '<f4')
    extd_fg2ext = _state.view(74224, '<f4')
    extd_fg2abs = _state.view(74412, '<f4')
    extd_fg2sym = _state.view(74600, '<f4')
    extd_bstext = _state.view(74788, '<f4')
    extd_bstabs = _state.view(74976, '<f4')
    extd_bstsym = _state.view(75164, '<f4')
    extd_avoext = _state.view(75352, '<f4')
    extd_avoabs = _state.view(75540, '<f4')
    extd_avosym = _state.view(75728, '<f4')
    extd_fvoext = _state.view(75916, '<f4')
    extd_fvoabs = _state.view(76104, '<f4')
    extd_fvosym = _state.view(76292, '<f4')
    extd_dmeext = _state.view(76480, '<f4')
    extd_dmeabs = _state.view(76668, '<f4')
    extd_dmesym = _state.view(76856, '<f4')
    extd_ccuext = _state.view(77044, '<f4')
    extd_ccuabs = _state.view(77232, '<f4')
    extd_ccusym = _state.view(77420, '<f4')
    extd_calext = _state.view(77608, '<f4')
    extd_calabs = _state.view(77796, '<f4')
    extd_calsym = _state.view(77984, '<f4')
    extd_cstext = _state.view(78172, '<f4')
    extd_cstabs = _state.view(78360, '<f4')
    extd_cstsym = _state.view(78548, '<f4')
    extd_cscext = _state.view(78736, '<f4')
    extd_cscabs = _state.view(78924, '<f4')
    extd_cscsym = _state.view(79112, '<f4')
    extd_cniext = _state.view(79300, '<f4')
    extd_cniabs = _state.view(79488, '<f4')
    extd_cnisym = _state.view(79676, '<f4')
    aflwc = _state.view(180192, '<f4')
    aslwc = _state.view(180220, '<f4')
    avlwc = _state.view(180204, '<f4')
    bslwc = _state.view(180200, '<f4')
    culwc = _state.view(180216, '<f4')
    elwcm = _state.view(180144, '<f4')
    elwcr = _state.view(180128, '<f4')
    elwct = _state.view(180176, '<f4')
    elwcu = _state.view(180160, '<f4')
    fvlwc = _state.view(180208, '<f4')
    mdlwc = _state.view(180212, '<f4')
    rflwc = _state.view(180196, '<f4')
    rhzone = _state.view(180112, '<f4')
    sclwc = _state.view(180228, '<f4')
    snlwc = _state.view(180232, '<f4')
    stlwc = _state.view(180224, '<f4')
    a = _ZERO32
    a1 = _ZERO32
    a2 = _ZERO32
    e1 = _ZERO32
    e2 = _ZERO32
    ec = _ZERO32
    i = 0
    ic = 0
    ii = 0
    ita = 0
    itas = 0
    itc = 0
    m = 0
    n = 0
    nb = 0
    ne = 0
    wrh = _ZERO32
    x = _ZERO32
    x1 = _ZERO32
    x2 = _ZERO32
    y = _ZERO32
    y1 = _ZERO32
    y2 = _ZERO32
    z1 = _ZERO32
    z2 = _ZERO32
    zk = _ZERO32
    D_10999 = 0
    D_11003 = 0
    D_11007 = 0
    D_11016 = 0
    D_11024 = 0
    D_11025 = 0
    D_11028 = 0
    D_11081 = 0
    D_11082 = 0
    D_11085 = 0
    D_11112 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                i = _int(1)
                _pc = 1
            case 1:  # <D.18858>
                D_10999 = _int(i > 4)
                _pc = 4 if D_10999 != 0 else 2
                continue
            case 2:  # __label_000002
                _1 = _int(i)
                _2 = _1 + -1
                __BLNK___awccon[_2] = 0.0
                _pc = 3
            case 3:  # L.483
                i = _int(i + 1)
                _pc = 1
                continue
            case 4:  # L.484
                i = _int(1)
                _pc = 5
            case 5:  # <D.18860>
                D_11003 = _int(i > 47)
                _pc = 8 if D_11003 != 0 else 6
                continue
            case 6:  # __label_000005
                _3 = _int(i)
                _4 = _3 + -1
                _5 = _int(i)
                _6 = _5 + -1
                _7 = extd_vx2[_4]
                __BLNK___vx0[_6] = _7
                _pc = 7
            case 7:  # L.485
                i = _int(i + 1)
                _pc = 5
                continue
            case 8:  # L.486
                nb = _int(1)
                ne = _int(46)
                m = _int(1)
                _pc = 9
            case 9:  # <D.18862>
                D_11007 = _int(m > 4)
                _pc = 152 if D_11007 != 0 else 10
                continue
            case 10:  # <D.18863>
                _8 = _int(m)
                _9 = _8 + -1
                _10 = card2d_ireg[_9]
                _pc = 11 if _10 != 0 else 12
                continue
            case 11:  # <D.18864>
                _pc = 151
                continue
            case 12:  # L.489
                _11 = _int(m)
                _12 = _11 + -1
                ita = _int(__BLNK___ich[_12])
                _13 = _int(m)
                _14 = _13 + -1
                _15 = __BLNK___ich[_14]
                itc = _int(_15 + -7)
                itas = _int(ita)
                _16 = _int(m)
                _17 = _16 + -1
                _18 = card2d_iregc[_17]
                _pc = 13 if _18 != 0 else 14
                continue
            case 13:  # <D.18866>
                _pc = 111
                continue
            case 14:  # __label_000012
                wrh = _f32(__BLNK___w[14])
                _19 = _int(m)
                _20 = _19 + -1
                _21 = __BLNK___ich[_20]
                _22 = _21 == 6
                _23 = m != 1
                _24 = _22 & _23
                _pc = 15 if _24 != 0 else 16
                continue
            case 15:  # <D.18868>
                wrh = _f32(7.0e+1)
                _pc = 16
                continue
            case 16:  # L.491
                i = _int(2)
                _pc = 17
            case 17:  # <D.18871>
                D_11016 = _int(i > 4)
                _pc = 21 if D_11016 != 0 else 18
                continue
            case 18:  # <D.18872>
                _25 = _int(i)
                _26 = _25 + -1
                _27 = rhzone[_26]
                _pc = 19 if wrh < _27 else 20
                continue
            case 19:  # <D.18873>
                _pc = 22
                continue
            case 20:  # L.492
                i = _int(i + 1)
                _pc = 17
                continue
            case 21:  # L.493
                i = _int(4)
                _pc = 22
            case 22:  # __label_000015
                ii = _int(i + -1)
                _28 = wrh > 0.0
                _29 = wrh < 9.9e+1
                _30 = _28 & _29
                _pc = 23 if _30 != 0 else 24
                continue
            case 23:  # <D.18875>
                _31 = 1.0e+2 - wrh
                x = _f32(__builtin_logf(_31))
                _pc = 24
                continue
            case 24:  # L.495
                _32 = _int(ii)
                _33 = _32 + -1
                _34 = rhzone[_33]
                _35 = 1.0e+2 - _34
                x1 = _f32(__builtin_logf(_35))
                _36 = _int(i)
                _37 = _36 + -1
                _38 = rhzone[_37]
                _39 = 1.0e+2 - _38
                x2 = _f32(__builtin_logf(_39))
                _pc = 25 if wrh >= 9.9e+1 else 26
                continue
            case 25:  # <D.18878>
                x = _f32(x2)
                _pc = 26
                continue
            case 26:  # L.496
                _pc = 27 if wrh <= 0.0 else 28
                continue
            case 27:  # <D.18881>
                x = _f32(x1)
                _pc = 28
                continue
            case 28:  # __label_000017
                D_11024 = _int(nb)
                D_11025 = _int(ne)
                n = _int(D_11024)
                _pc = 29
            case 29:  # <D.18884>
                D_11028 = _int(n > D_11025)
                _pc = 110 if D_11028 != 0 else 30
                continue
            case 30:  # <D.18885>
                ita = _int(itas)
                _40 = ita == 3
                _41 = m == 1
                _42 = _40 & _41
                _pc = 31 if _42 != 0 else 32
                continue
            case 31:  # <D.18886>
                _pc = 36
                continue
            case 32:  # L.500
                _43 = _int(n)
                _44 = _43 * 5
                _45 = _int(m)
                _46 = _44 + _45
                _47 = _46 + -6
                __BLNK___absc[_47] = 0.0
                _48 = _int(n)
                _49 = _48 * 5
                _50 = _int(m)
                _51 = _49 + _50
                _52 = _51 + -6
                __BLNK___extc[_52] = 0.0
                _53 = _int(n)
                _54 = _53 * 5
                _55 = _int(m)
                _56 = _54 + _55
                _57 = _56 + -6
                __BLNK___asym[_57] = 0.0
                _pc = 33 if ita > 6 else 34
                continue
            case 33:  # <D.18888>
                _pc = 63
                continue
            case 34:  # L.501
                _pc = 35 if ita <= 0 else 36
                continue
            case 35:  # <D.18890>
                _pc = 109
                continue
            case 36:  # __label_000018
                _58 = n > 40
                _59 = ita == 3
                _60 = _58 & _59
                _pc = 37 if _60 != 0 else 38
                continue
            case 37:  # <D.18892>
                ita = _int(4)
                _pc = 38
                continue
            case 38:  # L.503
                _pc = {1: 39, 2: 41, 3: 43, 4: 45, 5: 47, 6: 49}.get(ita, 51)
                continue
            case 39:  # L.506
                _pc = 51
                continue
            case 40:  # continuation_94
                _pc = 51
                continue
            case 41:  # L.507
                _pc = 51
                continue
            case 42:  # continuation_97
                _pc = 51
                continue
            case 43:  # L.508
                _pc = 52
                continue
            case 44:  # continuation_100
                _pc = 51
                continue
            case 45:  # L.509
                _pc = 55
                continue
            case 46:  # continuation_103
                _pc = 51
                continue
            case 47:  # L.510
                _pc = 56
                continue
            case 48:  # continuation_106
                _pc = 51
                continue
            case 49:  # L.511
                _pc = 57
                continue
            case 50:  # continuation_109
                _pc = 51
                continue
            case 51:  # __label_000020
                _61 = _int(i)
                _62 = _61 * 47
                _63 = _int(n)
                _64 = _62 + _63
                _65 = _64 + -48
                _66 = extd_rurext[_65]
                y2 = _f32(__builtin_logf(_66))
                _67 = _int(ii)
                _68 = _67 * 47
                _69 = _int(n)
                _70 = _68 + _69
                _71 = _70 + -48
                _72 = extd_rurext[_71]
                y1 = _f32(__builtin_logf(_72))
                _73 = _int(i)
                _74 = _73 * 47
                _75 = _int(n)
                _76 = _74 + _75
                _77 = _76 + -48
                _78 = extd_rurabs[_77]
                z2 = _f32(__builtin_logf(_78))
                _79 = _int(ii)
                _80 = _79 * 47
                _81 = _int(n)
                _82 = _80 + _81
                _83 = _82 + -48
                _84 = extd_rurabs[_83]
                z1 = _f32(__builtin_logf(_84))
                _85 = _int(i)
                _86 = _85 * 47
                _87 = _int(n)
                _88 = _86 + _87
                _89 = _88 + -48
                _90 = extd_rursym[_89]
                a2 = _f32(__builtin_logf(_90))
                _91 = _int(ii)
                _92 = _91 * 47
                _93 = _int(n)
                _94 = _92 + _93
                _95 = _94 + -48
                _96 = extd_rursym[_95]
                a1 = _f32(__builtin_logf(_96))
                _97 = _int(i)
                _98 = _97 + -1
                _99 = elwcr[_98]
                e2 = _f32(__builtin_logf(_99))
                _100 = _int(ii)
                _101 = _100 + -1
                _102 = elwcr[_101]
                e1 = _f32(__builtin_logf(_102))
                _pc = 58
                continue
            case 52:  # __label_000022
                _pc = 53 if m > 1 else 54
                continue
            case 53:  # <D.18896>
                _pc = 55
                continue
            case 54:  # L.512
                _103 = _int(i)
                _104 = _103 * 47
                _105 = _int(n)
                _106 = _104 + _105
                _107 = _106 + -48
                _108 = extd_ocnsym[_107]
                a2 = _f32(__builtin_logf(_108))
                _109 = _int(ii)
                _110 = _109 * 47
                _111 = _int(n)
                _112 = _110 + _111
                _113 = _112 + -48
                _114 = extd_ocnsym[_113]
                a1 = _f32(__builtin_logf(_114))
                _115 = a2 - a1
                _116 = _115
                _117 = x - x1
                _118 = _117
                _119 = _116 * _118
                _120 = x2 - x1
                _121 = _120
                _122 = _div(_119, _121)
                a = _f32(a1 + _122)
                _123 = _int(n)
                _124 = _123 * 5
                _125 = _int(m)
                _126 = _124 + _125
                _127 = _126 + -6
                _128 = __builtin_expf(a)
                __BLNK___asym[_127] = _128
                _129 = _int(i)
                _130 = _129 + -1
                _131 = elwcm[_130]
                e2 = _f32(__builtin_logf(_131))
                _132 = _int(ii)
                _133 = _132 + -1
                _134 = elwcm[_133]
                e1 = _f32(__builtin_logf(_134))
                _pc = 109
                continue
            case 55:  # __label_000025
                _135 = _int(i)
                _136 = _135 * 47
                _137 = _int(n)
                _138 = _136 + _137
                _139 = _138 + -48
                _140 = extd_ocnext[_139]
                y2 = _f32(__builtin_logf(_140))
                _141 = _int(ii)
                _142 = _141 * 47
                _143 = _int(n)
                _144 = _142 + _143
                _145 = _144 + -48
                _146 = extd_ocnext[_145]
                y1 = _f32(__builtin_logf(_146))
                _147 = _int(i)
                _148 = _147 * 47
                _149 = _int(n)
                _150 = _148 + _149
                _151 = _150 + -48
                _152 = extd_ocnabs[_151]
                z2 = _f32(__builtin_logf(_152))
                _153 = _int(ii)
                _154 = _153 * 47
                _155 = _int(n)
                _156 = _154 + _155
                _157 = _156 + -48
                _158 = extd_ocnabs[_157]
                z1 = _f32(__builtin_logf(_158))
                _159 = _int(i)
                _160 = _159 * 47
                _161 = _int(n)
                _162 = _160 + _161
                _163 = _162 + -48
                _164 = extd_ocnsym[_163]
                a2 = _f32(__builtin_logf(_164))
                _165 = _int(ii)
                _166 = _165 * 47
                _167 = _int(n)
                _168 = _166 + _167
                _169 = _168 + -48
                _170 = extd_ocnsym[_169]
                a1 = _f32(__builtin_logf(_170))
                _171 = _int(i)
                _172 = _171 + -1
                _173 = elwcm[_172]
                e2 = _f32(__builtin_logf(_173))
                _174 = _int(ii)
                _175 = _174 + -1
                _176 = elwcm[_175]
                e1 = _f32(__builtin_logf(_176))
                _pc = 58
                continue
            case 56:  # __label_000030
                _177 = _int(i)
                _178 = _177 * 47
                _179 = _int(n)
                _180 = _178 + _179
                _181 = _180 + -48
                _182 = extd_urbext[_181]
                y2 = _f32(__builtin_logf(_182))
                _183 = _int(ii)
                _184 = _183 * 47
                _185 = _int(n)
                _186 = _184 + _185
                _187 = _186 + -48
                _188 = extd_urbext[_187]
                y1 = _f32(__builtin_logf(_188))
                _189 = _int(i)
                _190 = _189 * 47
                _191 = _int(n)
                _192 = _190 + _191
                _193 = _192 + -48
                _194 = extd_urbabs[_193]
                z2 = _f32(__builtin_logf(_194))
                _195 = _int(ii)
                _196 = _195 * 47
                _197 = _int(n)
                _198 = _196 + _197
                _199 = _198 + -48
                _200 = extd_urbabs[_199]
                z1 = _f32(__builtin_logf(_200))
                _201 = _int(i)
                _202 = _201 * 47
                _203 = _int(n)
                _204 = _202 + _203
                _205 = _204 + -48
                _206 = extd_urbsym[_205]
                a2 = _f32(__builtin_logf(_206))
                _207 = _int(ii)
                _208 = _207 * 47
                _209 = _int(n)
                _210 = _208 + _209
                _211 = _210 + -48
                _212 = extd_urbsym[_211]
                a1 = _f32(__builtin_logf(_212))
                _213 = _int(i)
                _214 = _213 + -1
                _215 = elwcu[_214]
                e2 = _f32(__builtin_logf(_215))
                _216 = _int(ii)
                _217 = _216 + -1
                _218 = elwcu[_217]
                e1 = _f32(__builtin_logf(_218))
                _pc = 58
                continue
            case 57:  # __label_000035
                _219 = _int(i)
                _220 = _219 * 47
                _221 = _int(n)
                _222 = _220 + _221
                _223 = _222 + -48
                _224 = extd_troext[_223]
                y2 = _f32(__builtin_logf(_224))
                _225 = _int(ii)
                _226 = _225 * 47
                _227 = _int(n)
                _228 = _226 + _227
                _229 = _228 + -48
                _230 = extd_troext[_229]
                y1 = _f32(__builtin_logf(_230))
                _231 = _int(i)
                _232 = _231 * 47
                _233 = _int(n)
                _234 = _232 + _233
                _235 = _234 + -48
                _236 = extd_troabs[_235]
                z2 = _f32(__builtin_logf(_236))
                _237 = _int(ii)
                _238 = _237 * 47
                _239 = _int(n)
                _240 = _238 + _239
                _241 = _240 + -48
                _242 = extd_troabs[_241]
                z1 = _f32(__builtin_logf(_242))
                _243 = _int(i)
                _244 = _243 * 47
                _245 = _int(n)
                _246 = _244 + _245
                _247 = _246 + -48
                _248 = extd_trosym[_247]
                a2 = _f32(__builtin_logf(_248))
                _249 = _int(ii)
                _250 = _249 * 47
                _251 = _int(n)
                _252 = _250 + _251
                _253 = _252 + -48
                _254 = extd_trosym[_253]
                a1 = _f32(__builtin_logf(_254))
                _255 = _int(i)
                _256 = _255 + -1
                _257 = elwct[_256]
                e2 = _f32(__builtin_logf(_257))
                _258 = _int(ii)
                _259 = _258 + -1
                _260 = elwct[_259]
                e1 = _f32(__builtin_logf(_260))
                _pc = 58
            case 58:  # __label_000040
                _261 = y2 - y1
                _262 = _261
                _263 = x - x1
                _264 = _263
                _265 = _262 * _264
                _266 = x2 - x1
                _267 = _266
                _268 = _div(_265, _267)
                y = _f32(y1 + _268)
                _269 = z2 - z1
                _270 = _269
                _271 = x - x1
                _272 = _271
                _273 = _270 * _272
                _274 = x2 - x1
                _275 = _274
                _276 = _div(_273, _275)
                zk = _f32(z1 + _276)
                _277 = a2 - a1
                _278 = _277
                _279 = x - x1
                _280 = _279
                _281 = _278 * _280
                _282 = x2 - x1
                _283 = _282
                _284 = _div(_281, _283)
                a = _f32(a1 + _284)
                _285 = _int(n)
                _286 = _285 * 5
                _287 = _int(m)
                _288 = _286 + _287
                _289 = _288 + -6
                _290 = __builtin_expf(zk)
                __BLNK___absc[_289] = _290
                _291 = _int(n)
                _292 = _291 * 5
                _293 = _int(m)
                _294 = _292 + _293
                _295 = _294 + -6
                _296 = __builtin_expf(y)
                __BLNK___extc[_295] = _296
                _297 = _int(n)
                _298 = _297 * 5
                _299 = _int(m)
                _300 = _298 + _299
                _301 = _300 + -6
                _302 = __builtin_expf(a)
                __BLNK___asym[_301] = _302
                _pc = 59 if n == 1 else 60
                continue
            case 59:  # <D.18898>
                _303 = e2 - e1
                _304 = _303
                _305 = x - x1
                _306 = _305
                _307 = _304 * _306
                _308 = x2 - x1
                _309 = _308
                _310 = _div(_307, _309)
                ec = _f32(e1 + _310)
                _pc = 60
                continue
            case 60:  # L.513
                _pc = 61 if n == 1 else 62
                continue
            case 61:  # <D.18901>
                _311 = _int(m)
                _312 = _311 + -1
                _313 = __builtin_expf(ec)
                __BLNK___awccon[_312] = _313
                _pc = 62
                continue
            case 62:  # L.514
                _pc = 109
                continue
            case 63:  # __label_000045
                _pc = 64 if ita > 19 else 65
                continue
            case 64:  # <D.18904>
                _pc = 107
                continue
            case 65:  # L.515
                _pc = 66 if itc <= 0 else 67
                continue
            case 66:  # <D.18906>
                _pc = 109
                continue
            case 67:  # L.516
                _pc = {1: 68, 2: 70, 3: 72, 4: 74, 5: 76, 6: 78, 7: 80, 8: 82, 9: 84, 10: 86, 11: 88, 12: 90}.get(itc, 92)
                continue
            case 68:  # L.519
                _pc = 92
                continue
            case 69:  # continuation_155
                _pc = 92
                continue
            case 70:  # L.520
                _pc = 95
                continue
            case 71:  # continuation_158
                _pc = 92
                continue
            case 72:  # L.521
                _pc = 109
                continue
            case 73:  # continuation_161
                _pc = 92
                continue
            case 74:  # L.522
                _pc = 98
                continue
            case 75:  # continuation_164
                _pc = 92
                continue
            case 76:  # L.523
                _pc = 101
                continue
            case 77:  # continuation_167
                _pc = 92
                continue
            case 78:  # L.524
                _pc = 104
                continue
            case 79:  # continuation_170
                _pc = 92
                continue
            case 80:  # L.525
                _pc = 101
                continue
            case 81:  # continuation_173
                _pc = 92
                continue
            case 82:  # L.526
                _pc = 104
                continue
            case 83:  # continuation_176
                _pc = 92
                continue
            case 84:  # L.527
                _pc = 98
                continue
            case 85:  # continuation_179
                _pc = 92
                continue
            case 86:  # L.528
                _pc = 98
                continue
            case 87:  # continuation_182
                _pc = 92
                continue
            case 88:  # L.529
                _pc = 104
                continue
            case 89:  # continuation_185
                _pc = 92
                continue
            case 90:  # L.530
                _pc = 107
                continue
            case 91:  # continuation_188
                _pc = 92
                continue
            case 92:  # __label_000050
                _314 = _int(n)
                _315 = _314 + -1
                _316 = _int(n)
                _317 = _316 * 5
                _318 = _int(m)
                _319 = _317 + _318
                _320 = _319 + -6
                _321 = extd_fg1abs[_315]
                __BLNK___absc[_320] = _321
                _322 = _int(n)
                _323 = _322 + -1
                _324 = _int(n)
                _325 = _324 * 5
                _326 = _int(m)
                _327 = _325 + _326
                _328 = _327 + -6
                _329 = extd_fg1ext[_323]
                __BLNK___extc[_328] = _329
                _330 = _int(n)
                _331 = _330 + -1
                _332 = _int(n)
                _333 = _332 * 5
                _334 = _int(m)
                _335 = _333 + _334
                _336 = _335 + -6
                _337 = extd_fg1sym[_331]
                __BLNK___asym[_336] = _337
                _pc = 93 if n == 1 else 94
                continue
            case 93:  # <D.18909>
                _338 = _int(m)
                _339 = _338 + -1
                aflwc_385_340 = aflwc[0]
                __BLNK___awccon[_339] = aflwc_385_340
                _pc = 94
                continue
            case 94:  # L.531
                _pc = 109
                continue
            case 95:  # __label_000055
                _341 = _int(n)
                _342 = _341 + -1
                _343 = _int(n)
                _344 = _343 * 5
                _345 = _int(m)
                _346 = _344 + _345
                _347 = _346 + -6
                _348 = extd_fg2abs[_342]
                __BLNK___absc[_347] = _348
                _349 = _int(n)
                _350 = _349 + -1
                _351 = _int(n)
                _352 = _351 * 5
                _353 = _int(m)
                _354 = _352 + _353
                _355 = _354 + -6
                _356 = extd_fg2ext[_350]
                __BLNK___extc[_355] = _356
                _357 = _int(n)
                _358 = _357 + -1
                _359 = _int(n)
                _360 = _359 * 5
                _361 = _int(m)
                _362 = _360 + _361
                _363 = _362 + -6
                _364 = extd_fg2sym[_358]
                __BLNK___asym[_363] = _364
                _pc = 96 if n == 1 else 97
                continue
            case 96:  # <D.18912>
                _365 = _int(m)
                _366 = _365 + -1
                rflwc_386_367 = rflwc[0]
                __BLNK___awccon[_366] = rflwc_386_367
                _pc = 97
                continue
            case 97:  # L.532
                _pc = 109
                continue
            case 98:  # __label_000060
                _368 = _int(n)
                _369 = _368 + -1
                _370 = _int(n)
                _371 = _370 * 5
                _372 = _int(m)
                _373 = _371 + _372
                _374 = _373 + -6
                _375 = extd_bstabs[_369]
                __BLNK___absc[_374] = _375
                _376 = _int(n)
                _377 = _376 + -1
                _378 = _int(n)
                _379 = _378 * 5
                _380 = _int(m)
                _381 = _379 + _380
                _382 = _381 + -6
                _383 = extd_bstext[_377]
                __BLNK___extc[_382] = _383
                _384 = _int(n)
                _385 = _384 + -1
                _386 = _int(n)
                _387 = _386 * 5
                _388 = _int(m)
                _389 = _387 + _388
                _390 = _389 + -6
                _391 = extd_bstsym[_385]
                __BLNK___asym[_390] = _391
                _pc = 99 if n == 1 else 100
                continue
            case 99:  # <D.18915>
                _392 = _int(m)
                _393 = _392 + -1
                bslwc_387_394 = bslwc[0]
                __BLNK___awccon[_393] = bslwc_387_394
                _pc = 100
                continue
            case 100:  # L.533
                _pc = 109
                continue
            case 101:  # __label_000065
                _395 = _int(n)
                _396 = _395 + -1
                _397 = _int(n)
                _398 = _397 * 5
                _399 = _int(m)
                _400 = _398 + _399
                _401 = _400 + -6
                _402 = extd_avoabs[_396]
                __BLNK___absc[_401] = _402
                _403 = _int(n)
                _404 = _403 + -1
                _405 = _int(n)
                _406 = _405 * 5
                _407 = _int(m)
                _408 = _406 + _407
                _409 = _408 + -6
                _410 = extd_avoext[_404]
                __BLNK___extc[_409] = _410
                _411 = _int(n)
                _412 = _411 + -1
                _413 = _int(n)
                _414 = _413 * 5
                _415 = _int(m)
                _416 = _414 + _415
                _417 = _416 + -6
                _418 = extd_avosym[_412]
                __BLNK___asym[_417] = _418
                _pc = 102 if n == 1 else 103
                continue
            case 102:  # <D.18918>
                _419 = _int(m)
                _420 = _419 + -1
                avlwc_388_421 = avlwc[0]
                __BLNK___awccon[_420] = avlwc_388_421
                _pc = 103
                continue
            case 103:  # L.534
                _pc = 109
                continue
            case 104:  # __label_000070
                _422 = _int(n)
                _423 = _422 + -1
                _424 = _int(n)
                _425 = _424 * 5
                _426 = _int(m)
                _427 = _425 + _426
                _428 = _427 + -6
                _429 = extd_fvoabs[_423]
                __BLNK___absc[_428] = _429
                _430 = _int(n)
                _431 = _430 + -1
                _432 = _int(n)
                _433 = _432 * 5
                _434 = _int(m)
                _435 = _433 + _434
                _436 = _435 + -6
                _437 = extd_fvoext[_431]
                __BLNK___extc[_436] = _437
                _438 = _int(n)
                _439 = _438 + -1
                _440 = _int(n)
                _441 = _440 * 5
                _442 = _int(m)
                _443 = _441 + _442
                _444 = _443 + -6
                _445 = extd_fvosym[_439]
                __BLNK___asym[_444] = _445
                _pc = 105 if n == 1 else 106
                continue
            case 105:  # <D.18921>
                _446 = _int(m)
                _447 = _446 + -1
                fvlwc_389_448 = fvlwc[0]
                __BLNK___awccon[_447] = fvlwc_389_448
                _pc = 106
                continue
            case 106:  # L.535
                _pc = 109
                continue
            case 107:  # __label_000075
                _449 = _int(n)
                _450 = _449 + -1
                _451 = _int(n)
                _452 = _451 * 5
                _453 = _int(m)
                _454 = _452 + _453
                _455 = _454 + -6
                _456 = extd_dmeabs[_450]
                __BLNK___absc[_455] = _456
                _457 = _int(n)
                _458 = _457 + -1
                _459 = _int(n)
                _460 = _459 * 5
                _461 = _int(m)
                _462 = _460 + _461
                _463 = _462 + -6
                _464 = extd_dmeext[_458]
                __BLNK___extc[_463] = _464
                _465 = _int(n)
                _466 = _465 + -1
                _467 = _int(n)
                _468 = _467 * 5
                _469 = _int(m)
                _470 = _468 + _469
                _471 = _470 + -6
                _472 = extd_dmesym[_466]
                __BLNK___asym[_471] = _472
                _pc = 108 if n == 1 else 109
                continue
            case 108:  # <D.18924>
                _473 = _int(m)
                _474 = _473 + -1
                mdlwc_390_475 = mdlwc[0]
                __BLNK___awccon[_474] = mdlwc_390_475
                _pc = 109
                continue
            case 109:  # L.498
                n = _int(n + 1)
                _pc = 29
                continue
            case 110:  # L.499
                _pc = 151
                continue
            case 111:  # __label_000100
                D_11081 = _int(nb)
                D_11082 = _int(ne)
                n = _int(D_11081)
                _pc = 112
            case 112:  # <D.18927>
                D_11085 = _int(n > D_11082)
                _pc = 151 if D_11085 != 0 else 113
                continue
            case 113:  # <D.18928>
                _476 = _int(n)
                _477 = _476 * 5
                _478 = _int(m)
                _479 = _477 + _478
                _480 = _479 + -6
                __BLNK___absc[_480] = 0.0
                _481 = _int(n)
                _482 = _481 * 5
                _483 = _int(m)
                _484 = _482 + _483
                _485 = _484 + -6
                __BLNK___extc[_485] = 0.0
                _486 = _int(n)
                _487 = _486 * 5
                _488 = _int(m)
                _489 = _487 + _488
                _490 = _489 + -6
                __BLNK___asym[_490] = 0.0
                ic = _int(card2_icld[0])
                _pc = {1: 114, 2: 116, 3: 118, 4: 120, 5: 122, 6: 124, 7: 126, 8: 128, 9: 130, 10: 132, 11: 134}.get(ic, 136)
                continue
            case 114:  # L.541
                _pc = 136
                continue
            case 115:  # continuation_251
                _pc = 136
                continue
            case 116:  # L.542
                _pc = 139
                continue
            case 117:  # continuation_254
                _pc = 136
                continue
            case 118:  # L.543
                _pc = 142
                continue
            case 119:  # continuation_257
                _pc = 136
                continue
            case 120:  # L.544
                _pc = 145
                continue
            case 121:  # continuation_260
                _pc = 136
                continue
            case 122:  # L.545
                _pc = 148
                continue
            case 123:  # continuation_263
                _pc = 136
                continue
            case 124:  # L.546
                _pc = 142
                continue
            case 125:  # continuation_266
                _pc = 136
                continue
            case 126:  # L.547
                _pc = 148
                continue
            case 127:  # continuation_269
                _pc = 136
                continue
            case 128:  # L.548
                _pc = 148
                continue
            case 129:  # continuation_272
                _pc = 136
                continue
            case 130:  # L.549
                _pc = 136
                continue
            case 131:  # continuation_275
                _pc = 136
                continue
            case 132:  # L.550
                _pc = 136
                continue
            case 133:  # continuation_278
                _pc = 136
                continue
            case 134:  # L.551
                _pc = 136
                continue
            case 135:  # continuation_281
                _pc = 136
                continue
            case 136:  # __label_000125
                _491 = _int(n)
                _492 = _491 + -1
                _493 = _int(n)
                _494 = _493 * 5
                _495 = _int(m)
                _496 = _494 + _495
                _497 = _496 + -6
                _498 = extd_ccuabs[_492]
                __BLNK___absc[_497] = _498
                _499 = _int(n)
                _500 = _499 + -1
                _501 = _int(n)
                _502 = _501 * 5
                _503 = _int(m)
                _504 = _502 + _503
                _505 = _504 + -6
                _506 = extd_ccuext[_500]
                __BLNK___extc[_505] = _506
                _507 = _int(n)
                _508 = _507 + -1
                _509 = _int(n)
                _510 = _509 * 5
                _511 = _int(m)
                _512 = _510 + _511
                _513 = _512 + -6
                _514 = extd_ccusym[_508]
                __BLNK___asym[_513] = _514
                _pc = 137 if n == 1 else 138
                continue
            case 137:  # <D.18930>
                _515 = _int(m)
                _516 = _515 + -1
                culwc_391_517 = culwc[0]
                __BLNK___awccon[_516] = culwc_391_517
                _pc = 138
                continue
            case 138:  # L.552
                _pc = 150
                continue
            case 139:  # __label_000130
                _518 = _int(n)
                _519 = _518 + -1
                _520 = _int(n)
                _521 = _520 * 5
                _522 = _int(m)
                _523 = _521 + _522
                _524 = _523 + -6
                _525 = extd_calabs[_519]
                __BLNK___absc[_524] = _525
                _526 = _int(n)
                _527 = _526 + -1
                _528 = _int(n)
                _529 = _528 * 5
                _530 = _int(m)
                _531 = _529 + _530
                _532 = _531 + -6
                _533 = extd_calext[_527]
                __BLNK___extc[_532] = _533
                _534 = _int(n)
                _535 = _534 + -1
                _536 = _int(n)
                _537 = _536 * 5
                _538 = _int(m)
                _539 = _537 + _538
                _540 = _539 + -6
                _541 = extd_calsym[_535]
                __BLNK___asym[_540] = _541
                _pc = 140 if n == 1 else 141
                continue
            case 140:  # <D.18933>
                _542 = _int(m)
                _543 = _542 + -1
                aslwc_392_544 = aslwc[0]
                __BLNK___awccon[_543] = aslwc_392_544
                _pc = 141
                continue
            case 141:  # L.553
                _pc = 150
                continue
            case 142:  # __label_000135
                _545 = _int(n)
                _546 = _545 + -1
                _547 = _int(n)
                _548 = _547 * 5
                _549 = _int(m)
                _550 = _548 + _549
                _551 = _550 + -6
                _552 = extd_cstabs[_546]
                __BLNK___absc[_551] = _552
                _553 = _int(n)
                _554 = _553 + -1
                _555 = _int(n)
                _556 = _555 * 5
                _557 = _int(m)
                _558 = _556 + _557
                _559 = _558 + -6
                _560 = extd_cstext[_554]
                __BLNK___extc[_559] = _560
                _561 = _int(n)
                _562 = _561 + -1
                _563 = _int(n)
                _564 = _563 * 5
                _565 = _int(m)
                _566 = _564 + _565
                _567 = _566 + -6
                _568 = extd_cstsym[_562]
                __BLNK___asym[_567] = _568
                _pc = 143 if n == 1 else 144
                continue
            case 143:  # <D.18936>
                _569 = _int(m)
                _570 = _569 + -1
                stlwc_393_571 = stlwc[0]
                __BLNK___awccon[_570] = stlwc_393_571
                _pc = 144
                continue
            case 144:  # L.554
                _pc = 150
                continue
            case 145:  # __label_000140
                _572 = _int(n)
                _573 = _572 + -1
                _574 = _int(n)
                _575 = _574 * 5
                _576 = _int(m)
                _577 = _575 + _576
                _578 = _577 + -6
                _579 = extd_cscabs[_573]
                __BLNK___absc[_578] = _579
                _580 = _int(n)
                _581 = _580 + -1
                _582 = _int(n)
                _583 = _582 * 5
                _584 = _int(m)
                _585 = _583 + _584
                _586 = _585 + -6
                _587 = extd_cscext[_581]
                __BLNK___extc[_586] = _587
                _588 = _int(n)
                _589 = _588 + -1
                _590 = _int(n)
                _591 = _590 * 5
                _592 = _int(m)
                _593 = _591 + _592
                _594 = _593 + -6
                _595 = extd_cscsym[_589]
                __BLNK___asym[_594] = _595
                _pc = 146 if n == 1 else 147
                continue
            case 146:  # <D.18939>
                _596 = _int(m)
                _597 = _596 + -1
                sclwc_394_598 = sclwc[0]
                __BLNK___awccon[_597] = sclwc_394_598
                _pc = 147
                continue
            case 147:  # L.555
                _pc = 150
                continue
            case 148:  # __label_000145
                _599 = _int(n)
                _600 = _599 + -1
                _601 = _int(n)
                _602 = _601 * 5
                _603 = _int(m)
                _604 = _602 + _603
                _605 = _604 + -6
                _606 = extd_cniabs[_600]
                __BLNK___absc[_605] = _606
                _607 = _int(n)
                _608 = _607 + -1
                _609 = _int(n)
                _610 = _609 * 5
                _611 = _int(m)
                _612 = _610 + _611
                _613 = _612 + -6
                _614 = extd_cniext[_608]
                __BLNK___extc[_613] = _614
                _615 = _int(n)
                _616 = _615 + -1
                _617 = _int(n)
                _618 = _617 * 5
                _619 = _int(m)
                _620 = _618 + _619
                _621 = _620 + -6
                _622 = extd_cnisym[_616]
                __BLNK___asym[_621] = _622
                _pc = 149 if n == 1 else 150
                continue
            case 149:  # <D.18942>
                _623 = _int(m)
                _624 = _623 + -1
                snlwc_395_625 = snlwc[0]
                __BLNK___awccon[_624] = snlwc_395_625
                _pc = 150
                continue
            case 150:  # L.537
                n = _int(n + 1)
                _pc = 112
                continue
            case 151:  # L.487
                m = _int(m + 1)
                _pc = 9
                continue
            case 152:  # L.488
                n = _int(1)
                _pc = 153
            case 153:  # <D.18945>
                D_11112 = _int(n > 47)
                _pc = -1 if D_11112 != 0 else 154
                continue
            case 154:  # <D.18946>
                _626 = _int(n)
                _627 = _626 * 5
                _628 = _627 + -1
                __BLNK___absc[_628] = 0.0
                _629 = _int(n)
                _630 = _629 * 5
                _631 = _630 + -1
                __BLNK___extc[_631] = 0.0
                _632 = _int(n)
                _633 = _632 * 5
                _634 = _633 + -1
                __BLNK___asym[_634] = 0.0
                __BLNK___awccon[4] = 0.0
                _635 = card2_icld[0]
                _pc = 155 if _635 == 18 else 156
                continue
            case 155:  # <D.18947>
                _636 = _int(n)
                _637 = _636 + -1
                _638 = _int(n)
                _639 = _638 * 5
                _640 = _639 + -1
                _641 = cirr_ci32xt[_637]
                __BLNK___extc[_640] = _641
                _642 = _int(n)
                _643 = _642 + -1
                _644 = _int(n)
                _645 = _644 * 5
                _646 = _645 + -1
                _647 = cirr_ci32ab[_643]
                __BLNK___absc[_646] = _647
                _648 = _int(n)
                _649 = _648 + -1
                _650 = _int(n)
                _651 = _650 * 5
                _652 = _651 + -1
                _653 = cirr_ci32g[_649]
                __BLNK___asym[_652] = _653
                __BLNK___awccon[4] = 3.44599992968142032623291015625e-3
                _pc = 156
                continue
            case 156:  # L.559
                _654 = card2_icld[0]
                _pc = 157 if _654 == 19 else 158
                continue
            case 157:  # <D.18950>
                _655 = _int(n)
                _656 = _655 + -1
                _657 = _int(n)
                _658 = _657 * 5
                _659 = _658 + -1
                _660 = cirr_cir2xt[_656]
                __BLNK___extc[_659] = _660
                _661 = _int(n)
                _662 = _661 + -1
                _663 = _int(n)
                _664 = _663 * 5
                _665 = _664 + -1
                _666 = cirr_cir2ab[_662]
                __BLNK___absc[_665] = _666
                _667 = _int(n)
                _668 = _667 + -1
                _669 = _int(n)
                _670 = _669 * 5
                _671 = _670 + -1
                _672 = cirr_cir2g[_668]
                __BLNK___asym[_671] = _672
                __BLNK___awccon[4] = 5.81099987030029296875e-2
                _pc = 158
                continue
            case 158:  # L.557
                n = _int(n + 1)
                _pc = 153
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_ssgeo(_state, ierror, iph, iparm, parm1, parm2, parm3, parm4, psipo, g, maxgeo):
    __BLNK___relhum = _state.view(265568, '<f4')
    __BLNK___w = _state.view(266176, '<f4')
    __BLNK___wpath = _state.view(266428, '<f4')
    __BLNK___tbby = _state.view(283564, '<f4')
    card1_itype = _state.view(209572, '<i4')
    card1_noprnt = _state.view(209596, '<i4')
    card3_h1 = _state.view(246128, '<f4')
    card3_h2 = _state.view(246132, '<f4')
    card3_angle = _state.view(246136, '<f4')
    card3_range = _state.view(246140, '<f4')
    card3_beta = _state.view(246144, '<f4')
    card3_len = _state.view(246152, '<i4')
    cnstns_pi = _state.view(246160, '<f4')
    cnstns_ca = _state.view(246164, '<f4')
    cntrl_kmax = _state.view(245600, '<i4')
    cntrl_ikmax = _state.view(245608, '<i4')
    cntrl_ml = _state.view(245616, '<i4')
    cntrl_iklo = _state.view(245620, '<i4')
    cntrl_issgeo = _state.view(245624, '<i4')
    ifil_npr = _state.view(243020, '<i4')
    parmtr_zmax = _state.view(245640, '<f4')
    parmtr_imax = _state.view(245644, '<i4')
    rfrpth_zp = _state.view(246784, '<f4')
    sols_ah1 = _state.view(189472, '<f4')
    sols_arh = _state.view(189744, '<f4')
    sols_wpaths = _state.view(190016, '<f4')
    sols_pa = _state.view(207152, '<f4')
    sols_pr = _state.view(207424, '<f4')
    sols_atheta = _state.view(207696, '<f4')
    sols_adbeta = _state.view(207836, '<f4')
    sols_lj = _state.view(207976, '<i4')
    sols_jturn = _state.view(208252, '<i4')
    sols_angsun = _state.view(208256, '<f4')
    sols_cszen = _state.view(208260, '<f4')
    usrdta_nangls = _state.view(208544, '<i4')
    usrdta_angf = _state.view(208548, '<f4')
    usrdta_f = _state.view(208748, '<f4')
    angd = _ZERO32
    angl0 = _ZERO32
    az = _zeros(35, '<f4')
    bendng = _zeros(1, '<f4')
    betast = _zeros(1, '<f4')
    betd = _ZERO32
    corr = _ZERO32
    cosang = _ZERO32
    delo = _zeros(1, '<f4')
    h1d = _ZERO32
    h2d = _ZERO32
    htop = _ZERO32
    iarb = _zeros(1, '<i4')
    iarbo = _zeros(1, '<i4')
    ikmaxd = 0
    itd = 0
    j = 0
    jiter = 0
    jturnd = 0
    k = 0
    l = 0
    lend = 0
    ljd = _zeros(68, '<i4')
    ljdl = 0
    ljp1 = 0
    ll = 0
    lp1 = 0
    m = 0
    phio = _zeros(1, '<f4')
    phis = _zeros(1, '<f4')
    psio = _zeros(1, '<f4')
    psist = _zeros(1, '<f4')
    psist2 = _ZERO32
    relh = _ZERO32
    rhd = _zeros(35, '<f4')
    rngd = _ZERO32
    sangle = _zeros(1, '<f4')
    tbdum = _zeros(68, '<f4')
    thetao = _zeros(1, '<f4')
    thetas = _zeros(1, '<f4')
    thtst = _zeros(1, '<f4')
    wpdum = _zeros(4284, '<f4')
    D_11435 = 0
    D_11438 = 0
    D_11440 = 0
    D_11443 = 0
    D_11445 = 0
    D_11448 = 0
    D_11465 = 0
    D_11466 = 0
    D_11469 = 0
    D_11495 = 0
    D_11501 = 0
    D_11504 = 0
    D_11515 = 0
    D_11518 = 0
    x_27 = _ZERO32
    D_11529 = _ZERO32
    D_11530 = _ZERO32
    gg_28 = _ZERO32
    x_29 = _ZERO32
    D_11535 = _ZERO32
    D_11536 = _ZERO32
    D_11537 = _ZERO32
    D_11538 = _ZERO32
    D_11539 = _ZERO32
    D_11546 = 0
    D_11549 = 0
    C_11554 = _array([2], '<i4')
    D_11555 = 0
    D_11558 = 0
    D_11562 = 0
    D_11565 = 0
    D_11566 = 0
    D_11569 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                cntrl_iklo[0] = 1
                ifil_npr[0] = 1
                cntrl_issgeo[0] = 1
                _1 = iparm[0]
                _pc = 1 if _1 == 2 else 2
                continue
            case 1:  # <D.18953>
                _pc = 3
                continue
            case 2:  # L.561
                _2 = parm1[0]
                thetao[0] = _2
                _3 = parm2[0]
                phio[0] = _3
                _4 = parm3[0]
                thetas[0] = _4
                _5 = parm4[0]
                phis[0] = _5
                _pc = 4
                continue
            case 3:  # __label_000001
                _6 = parm1[0]
                psio[0] = _6
                _7 = parm2[0]
                delo[0] = _7
                _pc = 4
            case 4:  # __label_000002
                _8 = iparm[0]
                _pc = 5 if _8 != 0 else 6
                continue
            case 5:  # <D.18955>
                _pc = 12
                continue
            case 6:  # L.562
                thetao_396_9 = thetao[0]
                _10 = abs(thetao_396_9)
                _pc = 7 if _10 < 8.95e+1 else 8
                continue
            case 7:  # <D.18957>
                _pc = 12
                continue
            case 8:  # L.563
                thetao_397_11 = thetao[0]
                _pc = 9 if thetao_397_11 > 0.0 else 10
                continue
            case 9:  # <D.18959>
                _pc = 11
                continue
            case 10:  # L.564
                _12 = psipo[0]
                phis_398_13 = phis[0]
                _14 = _12 - phis_398_13
                psipo[0] = _14
                thetao[0] = 0.0
                phio[0] = 0.0
                thetas[0] = 0.0
                thetas_399_15 = thetas[0]
                _16 = thetas_399_15 + 9.0e+1
                phis[0] = _16
                _pc = 12
                continue
            case 11:  # __label_000004
                phis_400_17 = phis[0]
                _18 = psipo[0]
                _19 = phis_400_17 - _18
                psipo[0] = _19
                thetao[0] = 0.0
                phio[0] = 0.0
                thetas[0] = 0.0
                thetas_401_20 = thetas[0]
                _21 = 9.0e+1 - thetas_401_20
                phis[0] = _21
                _pc = 12
            case 12:  # __label_000005
                jturnd = _int(sols_jturn[0])
                _22 = cntrl_ikmax[0]
                ikmaxd = _int(_22 + 1)
                h1d = _f32(card3_h1[0])
                h2d = _f32(card3_h2[0])
                angd = _f32(card3_angle[0])
                rngd = _f32(card3_range[0])
                betd = _f32(card3_beta[0])
                card3_beta[0] = 0.0
                lend = _int(card3_len[0])
                itd = _int(card1_itype[0])
                _23 = cntrl_ml[0]
                parmtr_imax[0] = _23
                D_11435 = _int(parmtr_imax[0])
                j = _int(1)
                _pc = 13
            case 13:  # <D.18961>
                D_11438 = _int(j > D_11435)
                _pc = 17 if D_11438 != 0 else 14
                continue
            case 14:  # <D.18962>
                _24 = _int(j)
                _25 = _24 + -1
                _26 = _int(j)
                _27 = _26 + -1
                _28 = rfrpth_zp[_25]
                az[_27] = _28
                _pc = 15
            case 15:  # __label_000010
                _29 = _int(j)
                _30 = _29 + -1
                _31 = _int(j)
                _32 = _31 + -1
                _33 = __BLNK___relhum[_30]
                rhd[_32] = _33
                _pc = 16
            case 16:  # L.565
                j = _int(j + 1)
                _pc = 13
                continue
            case 17:  # L.566
                D_11440 = _int(ikmaxd)
                j = _int(1)
                _pc = 18
            case 18:  # <D.18963>
                D_11443 = _int(j > D_11440)
                _pc = 26 if D_11443 != 0 else 19
                continue
            case 19:  # <D.18964>
                _34 = _int(j)
                _35 = _34 + -1
                _36 = _int(j)
                _37 = _36 + -1
                _38 = __BLNK___tbby[_35]
                tbdum[_37] = _38
                _39 = _int(j)
                _40 = _39 + -1
                _41 = _int(j)
                _42 = _41 + -1
                _43 = sols_lj[_40]
                ljd[_42] = _43
                _44 = _int(j)
                _45 = _44 + -1
                _46 = ljd[_45]
                _47 = parmtr_imax[0]
                _pc = 20 if _46 > _47 else 21
                continue
            case 20:  # <D.18965>
                _48 = _int(j)
                _49 = _48 + -1
                _50 = parmtr_imax[0]
                ljd[_49] = _50
                _pc = 21
                continue
            case 21:  # L.569
                D_11445 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 22
            case 22:  # <D.18968>
                D_11448 = _int(k > D_11445)
                _pc = 25 if D_11448 != 0 else 23
                continue
            case 23:  # __label_000011
                _51 = _int(k)
                _52 = _51 * 68
                _53 = _int(j)
                _54 = _52 + _53
                _55 = _54 + -69
                _56 = _int(k)
                _57 = _56 * 68
                _58 = _int(j)
                _59 = _57 + _58
                _60 = _59 + -69
                _61 = __BLNK___wpath[_55]
                wpdum[_60] = _61
                _pc = 24
            case 24:  # L.570
                k = _int(k + 1)
                _pc = 22
                continue
            case 25:  # L.567
                j = _int(j + 1)
                _pc = 18
                continue
            case 26:  # L.568
                _62 = parmtr_imax[0]
                _63 = _62 + -1
                parmtr_imax[0] = _63
                iarbo[0] = 0
                _64 = card3_angle[0]
                _65 = _64 < 9.99999977648258209228515625e-3
                _66 = card3_angle[0]
                _67 = _66 > 1.799900054931640625e+2
                _68 = _65 | _67
                _pc = 27 if _68 != 0 else 28
                continue
            case 27:  # <D.18970>
                iarbo[0] = 1
                _pc = 28
                continue
            case 28:  # L.572
                _69 = iparm[0]
                _pc = 29 if _69 != 2 else 30
                continue
            case 29:  # <D.18973>
                _ft_psidel(_state, thetas, phis, thetao, phio, psipo, psio, delo, iarbo)
                _pc = 30
                continue
            case 30:  # L.573
                iarbo_402_70 = iarbo[0]
                iarb[0] = iarbo_402_70
                betast[0] = 0.0
                iarbo_403_71 = iarbo[0]
                _pc = 31 if iarbo_403_71 == 0 else 32
                continue
            case 31:  # <D.18976>
                psio_404_72 = psio[0]
                psist[0] = psio_404_72
                _pc = 32
                continue
            case 32:  # L.574
                angl0 = _f32(delo[0])
                _pc = 33
            case 33:  # __label_000952
                D_11465 = _int(cntrl_iklo[0])
                D_11466 = _int(ikmaxd)
                l = _int(D_11465)
                _pc = 34
            case 34:  # <D.18979>
                D_11469 = _int(l > D_11466)
                _pc = 99 if D_11469 != 0 else 35
                continue
            case 35:  # <D.18980>
                _73 = lend == 1
                _74 = jturnd != 0
                _75 = _73 | _74
                _pc = 36 if _75 != 0 else 37
                continue
            case 36:  # <D.18981>
                _pc = 40
                continue
            case 37:  # L.577
                _76 = _int(l)
                _77 = _76 + -1
                _78 = az[_77]
                card3_h1[0] = _78
                _79 = _int(l)
                _80 = _79 + -1
                relh = _f32(rhd[_80])
                _81 = _int(l)
                _82 = _81 + -1
                _83 = sols_atheta[_82]
                thtst[0] = _83
                _pc = 38 if l > 1 else 39
                continue
            case 38:  # <D.18983>
                _84 = l + -1
                _85 = _int(_84)
                _86 = _85 + -1
                _87 = sols_adbeta[_86]
                betast_405_88 = betast[0]
                _89 = _87 + betast_405_88
                betast[0] = _89
                _pc = 39
                continue
            case 39:  # L.578
                _pc = 47
                continue
            case 40:  # __label_000020
                _pc = 41 if l > 1 else 42
                continue
            case 41:  # <D.18986>
                _90 = l + -1
                _91 = _int(_90)
                _92 = _91 + -1
                _93 = ljd[_92]
                _94 = _int(_93)
                _95 = _94 + -1
                _96 = sols_adbeta[_95]
                betast_406_97 = betast[0]
                _98 = _96 + betast_406_97
                betast[0] = _98
                _pc = 42
                continue
            case 42:  # L.579
                _pc = 43 if l >= jturnd else 44
                continue
            case 43:  # <D.18989>
                _pc = 45
                continue
            case 44:  # L.580
                _99 = _int(l)
                _100 = _99 + -1
                _101 = ljd[_100]
                ljp1 = _int(_101 + 1)
                _102 = _int(ljp1)
                _103 = _102 + -1
                _104 = az[_103]
                card3_h1[0] = _104
                _105 = _int(ljp1)
                _106 = _105 + -1
                relh = _f32(rhd[_106])
                _107 = _int(ljp1)
                _108 = _107 + -1
                _109 = sols_atheta[_108]
                _110 = 1.8e+2 - _109
                thtst[0] = _110
                _pc = 47
                continue
            case 45:  # __label_000025
                _111 = _int(l)
                _112 = _111 + -1
                ljdl = _int(ljd[_112])
                _113 = _int(ljdl)
                _114 = _113 + -1
                _115 = az[_114]
                card3_h1[0] = _115
                _116 = _int(ljdl)
                _117 = _116 + -1
                relh = _f32(rhd[_117])
                _118 = _int(ljdl)
                _119 = _118 + -1
                _120 = sols_atheta[_119]
                thtst[0] = _120
                _pc = 46 if l == jturnd else 47
                continue
            case 46:  # <D.18991>
                _121 = _int(ljdl)
                _122 = _121 + -1
                _123 = sols_atheta[_122]
                _124 = 1.8e+2 - _123
                thtst[0] = _124
                _pc = 47
                continue
            case 47:  # __label_000030
                _125 = _int(l)
                _126 = _125 + -1
                _127 = card3_h1[0]
                sols_ah1[_126] = _127
                _128 = _int(l)
                _129 = _128 + -1
                sols_arh[_129] = relh
                _pc = 48 if l <= 1 else 49
                continue
            case 48:  # <D.18994>
                _pc = 50
                continue
            case 49:  # L.582
                _130 = _ft_psi(_state, psio, delo, betast, iarb, iarbo)
                psist[0] = _130
                angl0 = _f32(_ft_del(_state, psio, delo, betast, iarbo))
                _pc = 50
            case 50:  # __label_000035
                corr = _f32(0.0)
                card1_itype[0] = 3
                jiter = _int(1)
                _pc = 51
            case 51:  # <D.18996>
                D_11495 = _int(jiter > 4)
                _pc = 73 if D_11495 != 0 else 52
                continue
            case 52:  # <D.18997>
                card3_h2[0] = 0.0
                _131 = angl0 - corr
                card3_angle[0] = _131
                card3_len[0] = 0
                _132 = card3_angle[0]
                _pc = 53 if _132 <= 9.0e+1 else 54
                continue
            case 53:  # <D.18998>
                _pc = 55
                continue
            case 54:  # L.585
                card3_len[0] = 1
                _pc = 55
            case 55:  # __label_000040
                htop = _f32(parmtr_zmax[0])
                _133 = card3_h1[0]
                _134 = htop > _133
                _135 = card3_len[0]
                _136 = _135 == 1
                _137 = _134 | _136
                _pc = 56 if _137 != 0 else 57
                continue
            case 56:  # <D.19000>
                _pc = 62
                continue
            case 57:  # L.586
                D_11501 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 58
            case 58:  # <D.19002>
                D_11504 = _int(k > D_11501)
                _pc = 61 if D_11504 != 0 else 59
                continue
            case 59:  # __label_000050
                _138 = _int(k)
                _139 = _138 + -1
                __BLNK___w[_139] = 0.0
                _pc = 60
            case 60:  # L.587
                k = _int(k + 1)
                _pc = 58
                continue
            case 61:  # L.588
                _pc = 73
                continue
            case 62:  # __label_000060
                _ft_geo(_state, ierror, bendng, maxgeo)
                _140 = ierror[0]
                _pc = 63 if _140 != -5 else 64
                continue
            case 63:  # <D.19004>
                _pc = 69
                continue
            case 64:  # __label_000970
                D_11515 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 65
            case 65:  # <D.19006>
                D_11518 = _int(k > D_11515)
                _pc = 68 if D_11518 != 0 else 66
                continue
            case 66:  # __label_000070
                _141 = _int(k)
                _142 = _141 + -1
                __BLNK___w[_142] = -5.0e+0
                _pc = 67
            case 67:  # L.590
                k = _int(k + 1)
                _pc = 65
                continue
            case 68:  # L.591
                ierror[0] = 0
                _pc = 73
                continue
            case 69:  # __label_000080
                bendng_407_143 = bendng[0]
                _144 = corr - bendng_407_143
                _145 = abs(_144)
                _pc = 70 if _145 < 1.00000001490116119384765625e-1 else 71
                continue
            case 70:  # <D.19008>
                _pc = 73
                continue
            case 71:  # __label_000090
                corr = _f32(bendng[0])
                _pc = 72
            case 72:  # L.583
                jiter = _int(jiter + 1)
                _pc = 51
                continue
            case 73:  # __label_000100
                _146 = _ft_sctang(_state, card3_angle, thtst, psist, iarb)
                sangle[0] = _146
                _147 = cnstns_ca[0]
                sangle_408_148 = sangle[0]
                _149 = _147 * sangle_408_148
                cosang = _f32(__builtin_cosf(_149))
                x_27 = _f32(cosang)
                D_11529 = _f32(x_27)
                D_11530 = _f32(D_11529 * D_11529)
                _150 = D_11530 * 5.721969902515411376953125e-2
                _151 = _int(l)
                _152 = _151 + -1
                _153 = _150 + 6.0504019260406494140625e-2
                sols_pr[_152] = _153
                _154 = iph[0]
                _pc = 74 if _154 != 0 else 75
                continue
            case 74:  # <D.19010>
                _pc = 76
                continue
            case 75:  # L.593
                gg_28 = _f32(g[0])
                x_29 = _f32(cosang)
                D_11535 = _f32(gg_28)
                D_11536 = _f32(D_11535 * D_11535)
                D_11537 = _f32(gg_28)
                D_11538 = _f32(D_11537 * D_11537)
                _155 = D_11538 + 1.0e+0
                _156 = gg_28 * 2.0e+0
                _157 = x_29 * _156
                _158 = _155 - _157
                D_11539 = _f32(_158)
                _159 = 1.0e+0 - D_11536
                _160 = _159
                _161 = cnstns_pi[0]
                _162 = _161 * 4.0e+0
                _163 = __builtin_powf(D_11539, 1.5e+0)
                _164 = _162 * _163
                _165 = _164
                _166 = _int(l)
                _167 = _166 + -1
                _168 = _div(_160, _165)
                sols_pa[_167] = _168
                _pc = 93
                continue
            case 76:  # __label_000105
                _169 = iph[0]
                _pc = 77 if _169 != 1 else 78
                continue
            case 77:  # <D.19012>
                _pc = 92
                continue
            case 78:  # L.594
                m = _int(4)
                _170 = card3_h1[0]
                _pc = 79 if _170 <= 3.0e+1 else 80
                continue
            case 79:  # <D.19014>
                m = _int(3)
                _pc = 80
                continue
            case 80:  # L.595
                _171 = card3_h1[0]
                _pc = 81 if _171 <= 1.0e+1 else 82
                continue
            case 81:  # <D.19017>
                m = _int(2)
                _pc = 82
                continue
            case 82:  # L.596
                _172 = card3_h1[0]
                _pc = 83 if _172 <= 2.0e+0 else 84
                continue
            case 83:  # <D.19020>
                m = _int(1)
                _pc = 84
                continue
            case 84:  # L.597
                D_11546 = _int(usrdta_nangls[0])
                ll = _int(1)
                _pc = 85
            case 85:  # <D.19023>
                D_11549 = _int(ll > D_11546)
                _pc = 91 if D_11549 != 0 else 86
                continue
            case 86:  # <D.19024>
                _173 = _int(ll)
                _174 = _173 + -1
                _175 = usrdta_angf[_174]
                sangle_409_176 = sangle[0]
                _pc = 87 if _175 == sangle_409_176 else 88
                continue
            case 87:  # <D.19025>
                _177 = _int(ll)
                _178 = _177 * 4
                _179 = _int(m)
                _180 = _178 + _179
                _181 = _180 + -5
                _182 = _int(l)
                _183 = _182 + -1
                _184 = usrdta_f[_181]
                sols_pa[_183] = _184
                _pc = 93
                continue
            case 88:  # L.600
                _185 = _int(ll)
                _186 = _185 + -1
                _187 = usrdta_angf[_186]
                sangle_410_188 = sangle[0]
                _pc = 89 if _187 > sangle_410_188 else 90
                continue
            case 89:  # <D.19027>
                _pc = 91
                continue
            case 90:  # L.598
                ll = _int(ll + 1)
                _pc = 85
                continue
            case 91:  # __label_000107
                lp1 = _int(ll)
                ll = _int(ll + -1)
                _189 = _int(lp1)
                _190 = _189 * 4
                _191 = _int(m)
                _192 = _190 + _191
                _193 = _192 + -5
                _194 = usrdta_f[_193:]
                _195 = _int(ll)
                _196 = _195 * 4
                _197 = _int(m)
                _198 = _196 + _197
                _199 = _198 + -5
                _200 = usrdta_f[_199:]
                _201 = _int(l)
                _202 = _201 + -1
                _203 = sols_pa[_202:]
                _204 = _int(lp1)
                _205 = _204 + -1
                _206 = usrdta_angf[_205:]
                _207 = _int(ll)
                _208 = _207 + -1
                _209 = usrdta_angf[_208:]
                _ft_interp(_state, C_11554, sangle, _209, _206, _203, _200, _194)
                _pc = 93
                continue
            case 92:  # __label_000110
                _210 = _int(l)
                _211 = _210 + -1
                sangle_411_212 = sangle[0]
                sols_pa[_211] = sangle_411_212
                _pc = 93
            case 93:  # __label_000115
                D_11555 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 94
            case 94:  # <D.19029>
                D_11558 = _int(k > D_11555)
                _pc = 97 if D_11558 != 0 else 95
                continue
            case 95:  # __label_000120
                _213 = _int(k)
                _214 = _213 + -1
                _215 = _int(k)
                _216 = _215 * 68
                _217 = _int(l)
                _218 = _216 + _217
                _219 = _218 + -69
                _220 = __BLNK___w[_214]
                sols_wpaths[_219] = _220
                _pc = 96
            case 96:  # L.602
                k = _int(k + 1)
                _pc = 94
                continue
            case 97:  # L.603
                psist_412_221 = psist[0]
                psist2 = _f32(-psist_412_221)
                _222 = card3_angle[0]
                _223 = cnstns_ca[0]
                _224 = _222 * _223
                _225 = _int(l)
                _226 = _225 + -1
                _227 = __builtin_cosf(_224)
                sols_cszen[_226] = _227
                _pc = 98
            case 98:  # L.575
                l = _int(l + 1)
                _pc = 34
                continue
            case 99:  # L.576
                _228 = ikmaxd + -1
                cntrl_ikmax[0] = _228
                card3_h1[0] = h1d
                card3_h2[0] = h2d
                _229 = card3_angle[0]
                sols_angsun[0] = _229
                card3_angle[0] = angd
                card3_range[0] = rngd
                card3_beta[0] = betd
                card3_len[0] = lend
                card1_itype[0] = itd
                D_11562 = _int(ikmaxd)
                j = _int(1)
                _pc = 100
            case 100:  # <D.19031>
                D_11565 = _int(j > D_11562)
                _pc = 106 if D_11565 != 0 else 101
                continue
            case 101:  # <D.19032>
                _230 = _int(j)
                _231 = _230 + -1
                _232 = _int(j)
                _233 = _232 + -1
                _234 = tbdum[_231]
                __BLNK___tbby[_233] = _234
                _235 = _int(j)
                _236 = _235 + -1
                _237 = _int(j)
                _238 = _237 + -1
                _239 = ljd[_236]
                sols_lj[_238] = _239
                D_11566 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 102
            case 102:  # <D.19033>
                D_11569 = _int(k > D_11566)
                _pc = 105 if D_11569 != 0 else 103
                continue
            case 103:  # __label_000160
                _240 = _int(k)
                _241 = _240 * 68
                _242 = _int(j)
                _243 = _241 + _242
                _244 = _243 + -69
                _245 = _int(k)
                _246 = _245 * 68
                _247 = _int(j)
                _248 = _246 + _247
                _249 = _248 + -69
                _250 = wpdum[_244]
                __BLNK___wpath[_249] = _250
                _pc = 104
            case 104:  # L.606
                k = _int(k + 1)
                _pc = 102
                continue
            case 105:  # L.604
                j = _int(j + 1)
                _pc = 100
                continue
            case 106:  # L.605
                _251 = card1_noprnt[0]
                ifil_npr[0] = _251
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_aertmp(_state):
    __BLNK___wpath = _state.view(266428, '<f4')
    __BLNK___tbby = _state.view(283564, '<f4')
    aertm_tae7 = _state.view(246096, '<f4')
    aertm_tae12 = _state.view(246100, '<f4')
    aertm_tae13 = _state.view(246104, '<f4')
    aertm_tae14 = _state.view(246108, '<f4')
    aertm_tae16 = _state.view(246112, '<f4')
    cntrl_ikmax = _state.view(245608, '<i4')
    kk = 0
    sum12 = _ZERO32
    sum13 = _ZERO32
    sum14 = _ZERO32
    sum16 = _ZERO32
    sum7 = _ZERO32
    wdf12 = _ZERO32
    wdf13 = _ZERO32
    wdf14 = _ZERO32
    wdf16 = _ZERO32
    wdf7 = _ZERO32
    D_11668 = 0
    D_11671 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                sum7 = _f32(0.0)
                sum12 = _f32(0.0)
                sum13 = _f32(0.0)
                sum14 = _f32(0.0)
                sum16 = _f32(0.0)
                aertm_tae7[0] = 0.0
                aertm_tae12[0] = 0.0
                aertm_tae13[0] = 0.0
                aertm_tae14[0] = 0.0
                aertm_tae16[0] = 0.0
                D_11668 = _int(cntrl_ikmax[0])
                kk = _int(1)
                _pc = 1
            case 1:  # <D.19035>
                D_11671 = _int(kk > D_11668)
                _pc = 8 if D_11671 != 0 else 2
                continue
            case 2:  # <D.19036>
                _pc = 3 if kk == 1 else 4
                continue
            case 3:  # <D.19037>
                _1 = _int(kk)
                _2 = _1 + 407
                wdf7 = _f32(__BLNK___wpath[_2])
                _3 = _int(kk)
                _4 = _3 + 747
                wdf12 = _f32(__BLNK___wpath[_4])
                _5 = _int(kk)
                _6 = _5 + 815
                wdf13 = _f32(__BLNK___wpath[_6])
                _7 = _int(kk)
                _8 = _7 + 883
                wdf14 = _f32(__BLNK___wpath[_8])
                _9 = _int(kk)
                _10 = _9 + 1019
                wdf16 = _f32(__BLNK___wpath[_10])
                _pc = 5
                continue
            case 4:  # <D.19038>
                _11 = _int(kk)
                _12 = _11 + 407
                _13 = __BLNK___wpath[_12]
                _14 = kk + -1
                _15 = _int(_14)
                _16 = _15 + 407
                _17 = __BLNK___wpath[_16]
                wdf7 = _f32(_13 - _17)
                _18 = _int(kk)
                _19 = _18 + 747
                _20 = __BLNK___wpath[_19]
                _21 = kk + -1
                _22 = _int(_21)
                _23 = _22 + 747
                _24 = __BLNK___wpath[_23]
                wdf12 = _f32(_20 - _24)
                _25 = _int(kk)
                _26 = _25 + 815
                _27 = __BLNK___wpath[_26]
                _28 = kk + -1
                _29 = _int(_28)
                _30 = _29 + 815
                _31 = __BLNK___wpath[_30]
                wdf13 = _f32(_27 - _31)
                _32 = _int(kk)
                _33 = _32 + 883
                _34 = __BLNK___wpath[_33]
                _35 = kk + -1
                _36 = _int(_35)
                _37 = _36 + 883
                _38 = __BLNK___wpath[_37]
                wdf14 = _f32(_34 - _38)
                _39 = _int(kk)
                _40 = _39 + 1019
                _41 = __BLNK___wpath[_40]
                _42 = kk + -1
                _43 = _int(_42)
                _44 = _43 + 1019
                _45 = __BLNK___wpath[_44]
                wdf16 = _f32(_41 - _45)
                _pc = 5
            case 5:  # L.610
                sum7 = _f32(sum7 + wdf7)
                sum12 = _f32(sum12 + wdf12)
                sum13 = _f32(sum13 + wdf13)
                sum14 = _f32(sum14 + wdf14)
                sum16 = _f32(sum16 + wdf16)
                _46 = _int(kk)
                _47 = _46 + -1
                _48 = __BLNK___tbby[_47]
                _49 = wdf7 * _48
                _50 = aertm_tae7[0]
                _51 = _49 + _50
                aertm_tae7[0] = _51
                _52 = _int(kk)
                _53 = _52 + -1
                _54 = __BLNK___tbby[_53]
                _55 = wdf12 * _54
                _56 = aertm_tae12[0]
                _57 = _55 + _56
                aertm_tae12[0] = _57
                _58 = _int(kk)
                _59 = _58 + -1
                _60 = __BLNK___tbby[_59]
                _61 = wdf13 * _60
                _62 = aertm_tae13[0]
                _63 = _61 + _62
                aertm_tae13[0] = _63
                _64 = _int(kk)
                _65 = _64 + -1
                _66 = __BLNK___tbby[_65]
                _67 = wdf14 * _66
                _68 = aertm_tae14[0]
                _69 = _67 + _68
                aertm_tae14[0] = _69
                _pc = 6
            case 6:  # __label_000010
                _70 = _int(kk)
                _71 = _70 + -1
                _72 = __BLNK___tbby[_71]
                _73 = wdf16 * _72
                _74 = aertm_tae16[0]
                _75 = _73 + _74
                aertm_tae16[0] = _75
                _pc = 7
            case 7:  # L.608
                kk = _int(kk + 1)
                _pc = 1
                continue
            case 8:  # L.609
                _pc = 9 if sum7 > 0.0 else 10
                continue
            case 9:  # <D.19040>
                _76 = aertm_tae7[0]
                _77 = _div(_76, sum7)
                aertm_tae7[0] = _77
                _pc = 11
                continue
            case 10:  # <D.19041>
                _78 = __BLNK___tbby[0]
                aertm_tae7[0] = _78
                _pc = 11
            case 11:  # L.611
                _pc = 12 if sum12 > 0.0 else 13
                continue
            case 12:  # <D.19043>
                _79 = aertm_tae12[0]
                _80 = _div(_79, sum12)
                aertm_tae12[0] = _80
                _pc = 14
                continue
            case 13:  # <D.19044>
                _81 = __BLNK___tbby[0]
                aertm_tae12[0] = _81
                _pc = 14
            case 14:  # L.612
                _pc = 15 if sum13 > 0.0 else 16
                continue
            case 15:  # <D.19046>
                _82 = aertm_tae13[0]
                _83 = _div(_82, sum13)
                aertm_tae13[0] = _83
                _pc = 17
                continue
            case 16:  # <D.19047>
                _84 = __BLNK___tbby[0]
                aertm_tae13[0] = _84
                _pc = 17
            case 17:  # L.613
                _pc = 18 if sum14 > 0.0 else 19
                continue
            case 18:  # <D.19049>
                _85 = aertm_tae14[0]
                _86 = _div(_85, sum14)
                aertm_tae14[0] = _86
                _pc = 20
                continue
            case 19:  # <D.19050>
                _87 = __BLNK___tbby[0]
                aertm_tae14[0] = _87
                _pc = 20
            case 20:  # L.614
                _pc = 21 if sum16 > 0.0 else 22
                continue
            case 21:  # <D.19052>
                _88 = aertm_tae16[0]
                _89 = _div(_88, sum16)
                aertm_tae16[0] = _89
                _pc = -1
                continue
            case 22:  # <D.19053>
                _90 = __BLNK___tbby[0]
                aertm_tae16[0] = _90
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_geo(_state, ierror, bendng, maxgeo):
    __BLNK___ich = _state.view(265840, '<i4')
    __BLNK___w = _state.view(266176, '<f4')
    __BLNK___wpath = _state.view(266428, '<f4')
    __BLNK___tbby = _state.view(283564, '<f4')
    card1_model = _state.view(209568, '<i4')
    card1_itype = _state.view(209572, '<i4')
    card1_tbound = _state.view(209600, '<f4')
    card3_h1 = _state.view(246128, '<f4')
    card3_h2 = _state.view(246132, '<f4')
    card3_angle = _state.view(246136, '<f4')
    card3_range = _state.view(246140, '<f4')
    card3_beta = _state.view(246144, '<f4')
    card3_ree = _state.view(246148, '<f4')
    card3_len = _state.view(246152, '<i4')
    cntrl_kmax = _state.view(245600, '<i4')
    cntrl_ikmax = _state.view(245608, '<i4')
    cntrl_ml = _state.view(245616, '<i4')
    cntrl_issgeo = _state.view(245624, '<i4')
    ifil_npr = _state.view(243020, '<i4')
    model_zm = _state.view(231904, '<f4')
    model_pm = _state.view(232040, '<f4')
    model_tm = _state.view(232176, '<f4')
    model_densty = _state.view(232448, '<f4')
    model_rramt = _state.view(241152, '<f4')
    parmtr_re = _state.view(245632, '<f4')
    parmtr_deltas = _state.view(245636, '<f4')
    parmtr_zmax = _state.view(245640, '<f4')
    parmtr_imax = _state.view(245644, '<i4')
    parmtr_imod = _state.view(245648, '<i4')
    parmtr_ipath = _state.view(245656, '<i4')
    path_pl = _state.view(242144, '<f4')
    path_aht = _state.view(242700, '<f4')
    rain_rnpath = _state.view(241600, '<f4')
    rain_rramtk = _state.view(241872, '<f4')
    rfrpth_zp = _state.view(246784, '<f4')
    rfrpth_pp = _state.view(246924, '<f4')
    rfrpth_tp = _state.view(247064, '<f4')
    rfrpth_sp = _state.view(247344, '<f4')
    rfrpth_ppsum = _state.view(247484, '<f4')
    rfrpth_tpsum = _state.view(247624, '<f4')
    rfrpth_rhopsm = _state.view(247764, '<f4')
    rfrpth_denp = _state.view(247904, '<f4')
    rfrpth_amtp = _state.view(256724, '<f4')
    sols_lj = _state.view(207976, '<i4')
    sols_jturn = _state.view(208252, '<i4')
    amttot = _ZERO32
    fac = _zeros(1, '<f4')
    hmin = _zeros(1, '<f4')
    i = 0
    i1 = 0
    i2 = 0
    iamt = _zeros(1, '<i4')
    ih1 = 0
    ih2 = 0
    ii1 = 0
    ik = 0
    il = 0
    immax = 0
    j = 0
    j1 = 0
    jmax = 0
    jmaxp1 = 0
    jmaxst = 0
    k = 0
    l = 0
    ldel = 0
    lp = 0
    lz = 0
    phi = _zeros(1, '<f4')
    w15 = _ZERO32
    wtem = _ZERO32
    D_11970 = 0
    D_11971 = 0
    D_11974 = 0
    D_11982 = 0
    D_11985 = 0
    D_11996 = 0
    D_11999 = 0
    D_12003 = 0
    D_12006 = 0
    D_12011 = _ZERO32
    D_12012 = _ZERO32
    D_12041 = 0
    D_12044 = 0
    M_30 = 0
    D_12051 = 0
    D_12054 = 0
    D_12058 = 0
    D_12061 = 0
    D_12063 = 0
    D_12066 = 0
    D_12070 = 0
    D_12073 = 0
    D_12076 = _ZERO32
    D_12077 = _ZERO32
    D_12081 = 0
    D_12084 = 0
    D_12091 = 0
    D_12094 = 0
    D_12100 = 0
    D_12103 = 0
    D_12110 = 0
    D_12113 = 0
    D_12129 = 0
    D_12132 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                parmtr_deltas[0] = 5.0e+0
                jmaxst = _int(1)
                ierror[0] = 0
                _1 = card3_ree[0]
                parmtr_re[0] = _1
                _2 = cntrl_ml[0]
                parmtr_imod[0] = _2
                _3 = cntrl_ml[0]
                parmtr_imax[0] = _3
                i = _int(1)
                _pc = 1
            case 1:  # <D.19055>
                D_11970 = _int(i > 35)
                _pc = 7 if D_11970 != 0 else 2
                continue
            case 2:  # <D.19056>
                _4 = _int(i)
                _5 = _4 + -1
                sols_lj[_5] = 0
                _6 = _int(i)
                _7 = _6 + -1
                rfrpth_sp[_7] = 0.0
                _8 = _int(i)
                _9 = _8 + -1
                rfrpth_ppsum[_9] = 0.0
                _10 = _int(i)
                _11 = _10 + -1
                rfrpth_tpsum[_11] = 0.0
                _12 = _int(i)
                _13 = _12 + -1
                rfrpth_rhopsm[_13] = 0.0
                D_11971 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 3
            case 3:  # <D.19057>
                D_11974 = _int(k > D_11971)
                _pc = 6 if D_11974 != 0 else 4
                continue
            case 4:  # <D.19058>
                _14 = _int(i)
                _15 = _14 * 63
                _16 = _int(k)
                _17 = _15 + _16
                _18 = _17 + -64
                rfrpth_amtp[_18] = 0.0
                _pc = 5
            case 5:  # L.618
                k = _int(k + 1)
                _pc = 3
                continue
            case 6:  # L.616
                i = _int(i + 1)
                _pc = 1
                continue
            case 7:  # L.617
                _19 = parmtr_imax[0]
                _20 = _int(_19)
                _21 = _20 + -1
                _22 = model_zm[_21]
                parmtr_zmax[0] = _22
                _23 = cntrl_issgeo[0]
                _pc = 8 if _23 == 1 else 9
                continue
            case 8:  # <D.19059>
                _pc = 39
                continue
            case 9:  # L.620
                _24 = card1_itype[0]
                _pc = 10 if _24 > 1 else 11
                continue
            case 10:  # <D.19061>
                _pc = 39
                continue
            case 11:  # L.621
                _25 = card3_h1[0]
                rfrpth_zp[0] = _25
                _26 = cntrl_ml[0]
                _pc = 12 if _26 == 1 else 13
                continue
            case 12:  # <D.19063>
                _27 = model_pm[0]
                rfrpth_pp[0] = _27
                _28 = model_tm[0]
                rfrpth_tp[0] = _28
                sols_lj[0] = 1
                _29 = card3_range[0]
                rfrpth_sp[0] = _29
                _30 = card3_range[0]
                path_pl[0] = _30
                _pc = 26
                continue
            case 13:  # <D.19064>
                _31 = card1_model[0]
                _pc = 14 if _31 == 0 else 15
                continue
            case 14:  # <D.19066>
                _pc = 26
                continue
            case 15:  # L.623
                D_11982 = _int(cntrl_ml[0])
                i = _int(2)
                _pc = 16
            case 16:  # <D.19068>
                D_11985 = _int(i > D_11982)
                _pc = 20 if D_11985 != 0 else 17
                continue
            case 17:  # <D.19069>
                i2 = _int(i)
                _32 = _int(i)
                _33 = _32 + -1
                _34 = model_zm[_33]
                _35 = card3_h1[0]
                _pc = 18 if _34 > _35 else 19
                continue
            case 18:  # <D.19070>
                _pc = 20
                continue
            case 19:  # L.624
                i = _int(i + 1)
                _pc = 16
                continue
            case 20:  # __label_000130
                i1 = _int(i2 + -1)
                _36 = card3_h1[0]
                _37 = _int(i1)
                _38 = _37 + -1
                _39 = model_zm[_38]
                _40 = _36 - _39
                _41 = _40
                _42 = _int(i2)
                _43 = _42 + -1
                _44 = model_zm[_43]
                _45 = _int(i1)
                _46 = _45 + -1
                _47 = model_zm[_46]
                _48 = _44 - _47
                _49 = _48
                _50 = _div(_41, _49)
                fac[0] = _50
                _51 = _int(i2)
                _52 = _51 + -1
                _53 = model_pm[_52:]
                _54 = _int(i1)
                _55 = _54 + -1
                _56 = model_pm[_55:]
                _ft_expint(_state, rfrpth_pp[0:], _56, _53, fac)
                _57 = _int(i1)
                _58 = _57 + -1
                _59 = model_tm[_58]
                _60 = _int(i2)
                _61 = _60 + -1
                _62 = model_tm[_61]
                _63 = _int(i1)
                _64 = _63 + -1
                _65 = model_tm[_64]
                _66 = _62 - _65
                _67 = _66
                fac_413_68 = fac[0]
                _69 = _67 * fac_413_68
                _70 = _59 + _69
                rfrpth_tp[0] = _70
                ii1 = _int(i1)
                fac_414_71 = fac[0]
                _pc = 21 if fac_414_71 > 5.0e-1 else 22
                continue
            case 21:  # <D.19072>
                ii1 = _int(i2)
                _pc = 22
                continue
            case 22:  # L.627
                sols_lj[0] = ii1
                _72 = _int(ii1)
                _73 = _72 + -1
                _74 = card3_range[0]
                rfrpth_sp[_73] = _74
                D_11996 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 23
            case 23:  # <D.19075>
                D_11999 = _int(k > D_11996)
                _pc = 26 if D_11999 != 0 else 24
                continue
            case 24:  # <D.19076>
                _75 = _int(i2)
                _76 = _75 * 63
                _77 = _int(k)
                _78 = _76 + _77
                _79 = _78 + -64
                _80 = model_densty[_79:]
                _81 = _int(i1)
                _82 = _81 * 63
                _83 = _int(k)
                _84 = _82 + _83
                _85 = _84 + -64
                _86 = model_densty[_85:]
                _87 = _int(k)
                _88 = _87 + -1
                _89 = rfrpth_denp[_88:]
                _ft_expint(_state, _89, _86, _80, fac)
                _pc = 25
            case 25:  # L.628
                k = _int(k + 1)
                _pc = 23
                continue
            case 26:  # __label_000036
                cntrl_ikmax[0] = 1
                immax = _int(1)
                _90 = card1_model[0]
                _pc = 27 if _90 == 0 else 28
                continue
            case 27:  # <D.19077>
                _91 = model_tm[0]
                rfrpth_tp[0] = _91
                _pc = 28
                continue
            case 28:  # L.630
                _92 = rfrpth_tp[0]
                __BLNK___tbby[0] = _92
                D_12003 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 29
            case 29:  # <D.19080>
                D_12006 = _int(k > D_12003)
                _pc = 34 if D_12006 != 0 else 30
                continue
            case 30:  # <D.19081>
                _93 = cntrl_ml[0]
                _pc = 31 if _93 == 1 else 32
                continue
            case 31:  # <D.19082>
                _94 = _int(k)
                _95 = _94 + -1
                _96 = _int(k)
                _97 = _96 + -1
                _98 = model_densty[_95]
                rfrpth_denp[_97] = _98
                _pc = 32
                continue
            case 32:  # L.633
                _99 = _int(k)
                _100 = _99 + -1
                _101 = rfrpth_denp[_100]
                _102 = card3_range[0]
                _103 = _int(k)
                _104 = _103 + -1
                _105 = _101 * _102
                __BLNK___w[_104] = _105
                _106 = _int(k)
                _107 = _106 + -1
                _108 = _int(k)
                _109 = _108 + -1
                _110 = _109 * 68
                _111 = __BLNK___w[_107]
                __BLNK___wpath[_110] = _111
                _pc = 33
            case 33:  # L.631
                k = _int(k + 1)
                _pc = 29
                continue
            case 34:  # L.632
                _112 = rfrpth_tp[0]
                _113 = 2.96e+2 - _112
                _114 = _113
                wtem = _f32(_div(_114, 3.6e+1))
                _pc = 35 if wtem < 0.0 else 36
                continue
            case 35:  # <D.19085>
                wtem = _f32(0.0)
                _pc = 36
                continue
            case 36:  # L.634
                _pc = 37 if wtem > 1.0e+0 else 38
                continue
            case 37:  # <D.19088>
                wtem = _f32(1.0e+0)
                _pc = 38
                continue
            case 38:  # L.635
                _115 = __BLNK___w[4]
                _116 = wtem * _115
                __BLNK___w[8] = _116
                _117 = __BLNK___w[7]
                _118 = _117 * 2.68999993801116943359375e-1
                _119 = rfrpth_tp[0]
                _120 = _119 - 2.73149993896484375e+2
                _121 = _120
                _122 = _118 * _121
                __BLNK___w[58] = _122
                _123 = rfrpth_tp[0]
                _124 = _123 - 2.73149993896484375e+2
                D_12011 = _f32(_124)
                D_12012 = _f32(D_12011 * D_12011)
                _125 = __BLNK___w[7]
                _126 = _125 * 2.68999993801116943359375e-1
                _127 = D_12012 * _126
                __BLNK___w[59] = _127
                _128 = __BLNK___w[8]
                __BLNK___wpath[544] = _128
                _129 = __BLNK___w[58]
                __BLNK___wpath[3944] = _129
                _130 = __BLNK___w[59]
                __BLNK___wpath[4012] = _130
                _pc = 117
                continue
            case 39:  # __label_000200
                _ft_geoinp(_state, card3_h1, card3_h2, card3_angle, card3_range, card3_beta, card1_itype, card3_len, hmin, phi, ierror)
                _131 = ierror[0]
                _pc = 40 if _131 == 0 else 41
                continue
            case 40:  # <D.19091>
                _pc = 42
                continue
            case 41:  # __label_000038
                return
            case 42:  # __label_000210
                iamt[0] = 1
                _ft_rfpath(_state, card3_h1, card3_h2, card3_angle, phi, card3_len, hmin, iamt, card3_beta, card3_range, bendng)
                D_12041 = _int(parmtr_ipath[0])
                i = _int(1)
                _pc = 43
            case 43:  # <D.19093>
                D_12044 = _int(i > D_12041)
                _pc = 49 if D_12044 != 0 else 44
                continue
            case 44:  # <D.19094>
                _132 = _int(i)
                _133 = _132 + -1
                _134 = rfrpth_zp[_133]
                _135 = card3_h1[0]
                _pc = 45 if _134 == _135 else 46
                continue
            case 45:  # <D.19095>
                ih1 = _int(i)
                _pc = 46
                continue
            case 46:  # L.639
                _136 = _int(i)
                _137 = _136 + -1
                _138 = rfrpth_zp[_137]
                _139 = card3_h2[0]
                _pc = 47 if _138 == _139 else 48
                continue
            case 47:  # <D.19098>
                ih2 = _int(i)
                _pc = 48
                continue
            case 48:  # L.637
                i = _int(i + 1)
                _pc = 43
                continue
            case 49:  # L.638
                M_30 = _int(ih1)
                M_30 = _int(min(ih2, M_30))
                _140 = parmtr_ipath[0]
                _141 = _140 + -1
                _142 = M_30 + -1
                _143 = card3_len[0]
                _144 = _142 * _143
                jmax = _int(_141 + _144)
                cntrl_ikmax[0] = jmax
                l = _int(ih1)
                ldel = _int(-1)
                _145 = card3_len[0]
                _146 = _145 == 1
                _147 = card3_h1[0]
                _148 = card3_h2[0]
                _149 = _147 > _148
                _150 = _146 | _149
                _pc = 50 if _150 != 0 else 51
                continue
            case 50:  # <D.19101>
                _pc = 52
                continue
            case 51:  # L.641
                l = _int(0)
                ldel = _int(1)
                _pc = 52
            case 52:  # __label_000230
                sols_jturn[0] = 0
                jmaxp1 = _int(jmax + 1)
                D_12051 = _int(jmaxp1)
                j = _int(1)
                _pc = 53
            case 53:  # <D.19103>
                D_12054 = _int(j > D_12051)
                _pc = 59 if D_12054 != 0 else 54
                continue
            case 54:  # <D.19104>
                _151 = l != 1
                _152 = ldel != -1
                _153 = _151 | _152
                _pc = 55 if _153 != 0 else 56
                continue
            case 55:  # <D.19105>
                _pc = 57
                continue
            case 56:  # L.644
                sols_jturn[0] = j
                l = _int(0)
                ldel = _int(1)
                _pc = 57
            case 57:  # __label_000240
                l = _int(l + ldel)
                _154 = _int(j)
                _155 = _154 + -1
                sols_lj[_155] = l
                _pc = 58
            case 58:  # L.642
                j = _int(j + 1)
                _pc = 53
                continue
            case 59:  # L.643
                amttot = _f32(0.0)
                D_12058 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 60
            case 60:  # <D.19107>
                D_12061 = _int(k > D_12058)
                _pc = 63 if D_12061 != 0 else 61
                continue
            case 61:  # __label_000255
                _156 = _int(k)
                _157 = _156 + -1
                _158 = _157 * 68
                __BLNK___wpath[_158] = 0.0
                _pc = 62
            case 62:  # L.645
                k = _int(k + 1)
                _pc = 60
                continue
            case 63:  # L.646
                parmtr_imax[0] = 0
                D_12063 = _int(jmax)
                j = _int(1)
                _pc = 64
            case 64:  # <D.19109>
                D_12066 = _int(j > D_12063)
                _pc = 83 if D_12066 != 0 else 65
                continue
            case 65:  # <D.19110>
                _159 = _int(j)
                _160 = _159 + -1
                l = _int(sols_lj[_160])
                _161 = cntrl_ml[0]
                _pc = 66 if l >= _161 else 67
                continue
            case 66:  # <D.19111>
                l = _int(cntrl_ml[0])
                _pc = 67
                continue
            case 67:  # L.649
                _162 = parmtr_imax[0]
                _pc = 68 if l >= _162 else 69
                continue
            case 68:  # <D.19114>
                parmtr_imax[0] = l
                _pc = 69
                continue
            case 69:  # L.650
                _163 = _int(l)
                _164 = _163 + -1
                _165 = rfrpth_tpsum[_164]
                _166 = _int(l)
                _167 = _166 + -1
                _168 = rfrpth_rhopsm[_167]
                _169 = _int(j)
                _170 = _169 + -1
                _171 = _div(_165, _168)
                __BLNK___tbby[_170] = _171
                _172 = _int(l)
                _173 = _172 + -1
                _174 = rfrpth_rhopsm[_173]
                amttot = _f32(amttot + _174)
                j1 = _int(j + -1)
                _pc = 70 if j1 == 0 else 71
                continue
            case 70:  # <D.19117>
                j1 = _int(1)
                _pc = 71
                continue
            case 71:  # L.651
                D_12070 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 72
            case 72:  # <D.19120>
                D_12073 = _int(k > D_12070)
                _pc = 77 if D_12073 != 0 else 73
                continue
            case 73:  # <D.19121>
                _pc = 74 if k == 9 else 75
                continue
            case 74:  # <D.19122>
                _pc = 76
                continue
            case 75:  # L.654
                _175 = _int(k)
                _176 = _175 * 68
                _177 = _int(j1)
                _178 = _176 + _177
                _179 = _178 + -69
                _180 = __BLNK___wpath[_179]
                _181 = _int(l)
                _182 = _181 * 63
                _183 = _int(k)
                _184 = _182 + _183
                _185 = _184 + -64
                _186 = rfrpth_amtp[_185]
                _187 = _int(k)
                _188 = _187 * 68
                _189 = _int(j)
                _190 = _188 + _189
                _191 = _190 + -69
                _192 = _180 + _186
                __BLNK___wpath[_191] = _192
                _pc = 76
            case 76:  # L.652
                k = _int(k + 1)
                _pc = 72
                continue
            case 77:  # L.653
                _193 = _int(j1)
                _194 = _193 + 3943
                _195 = __BLNK___wpath[_194]
                _196 = _int(l)
                _197 = _196 * 63
                _198 = _197 + -56
                _199 = rfrpth_amtp[_198]
                _200 = _199 * 2.68999993801116943359375e-1
                _201 = _int(j)
                _202 = _201 + -1
                _203 = __BLNK___tbby[_202]
                _204 = _203 - 2.73149993896484375e+2
                _205 = _204
                _206 = _200 * _205
                _207 = _int(j)
                _208 = _207 + 3943
                _209 = _195 + _206
                __BLNK___wpath[_208] = _209
                _210 = _int(j)
                _211 = _210 + -1
                _212 = __BLNK___tbby[_211]
                _213 = _212 - 2.73149993896484375e+2
                D_12076 = _f32(_213)
                D_12077 = _f32(D_12076 * D_12076)
                _214 = _int(j1)
                _215 = _214 + 4011
                _216 = __BLNK___wpath[_215]
                _217 = _int(l)
                _218 = _217 * 63
                _219 = _218 + -56
                _220 = rfrpth_amtp[_219]
                _221 = _220 * 2.68999993801116943359375e-1
                _222 = D_12077 * _221
                _223 = _int(j)
                _224 = _223 + 4011
                _225 = _216 + _222
                __BLNK___wpath[_224] = _225
                _226 = _int(j)
                _227 = _226 + -1
                _228 = __BLNK___tbby[_227]
                _229 = 2.96e+2 - _228
                _230 = _229
                wtem = _f32(_div(_230, 3.6e+1))
                _pc = 78 if wtem < 0.0 else 79
                continue
            case 78:  # <D.19124>
                wtem = _f32(0.0)
                _pc = 79
                continue
            case 79:  # L.655
                _pc = 80 if wtem > 1.0e+0 else 81
                continue
            case 80:  # <D.19127>
                wtem = _f32(1.0e+0)
                _pc = 81
                continue
            case 81:  # L.656
                _231 = _int(j1)
                _232 = _231 + 543
                _233 = __BLNK___wpath[_232]
                _234 = _int(l)
                _235 = _234 * 63
                _236 = _235 + -59
                _237 = rfrpth_amtp[_236]
                _238 = wtem * _237
                _239 = _int(j)
                _240 = _239 + 543
                _241 = _233 + _238
                __BLNK___wpath[_240] = _241
                _pc = 82
            case 82:  # L.647
                j = _int(j + 1)
                _pc = 64
                continue
            case 83:  # L.648
                D_12081 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 84
            case 84:  # <D.19130>
                D_12084 = _int(k > D_12081)
                _pc = 87 if D_12084 != 0 else 85
                continue
            case 85:  # <D.19131>
                _242 = _int(k)
                _243 = _242 * 68
                _244 = _int(jmax)
                _245 = _243 + _244
                _246 = _245 + -69
                _247 = _int(k)
                _248 = _247 + -1
                _249 = __BLNK___wpath[_246]
                __BLNK___w[_248] = _249
                _pc = 86
            case 86:  # L.657
                k = _int(k + 1)
                _pc = 84
                continue
            case 87:  # L.658
                jmaxst = _int(jmax)
                immax = _int(parmtr_imax[0])
                cntrl_ikmax[0] = jmax
                _250 = card1_tbound[0]
                _251 = _250 == 0.0
                _252 = model_zm[0]
                _253 = card3_h2[0]
                _254 = _252 == _253
                _255 = _251 & _254
                _pc = 88 if _255 != 0 else 89
                continue
            case 88:  # <D.19132>
                _256 = model_tm[0]
                card1_tbound[0] = _256
                _pc = 89
                continue
            case 89:  # L.659
                _257 = ifil_npr[0]
                _pc = 90 if _257 == 1 else 91
                continue
            case 90:  # <D.19135>
                _pc = 107
                continue
            case 91:  # __label_000042
                lp = _int(1)
                _258 = card3_len[0]
                _259 = _258 == 1
                _260 = card3_h1[0]
                _261 = card3_h2[0]
                _262 = _260 > _261
                _263 = _259 | _262
                _pc = 92 if _263 != 0 else 93
                continue
            case 92:  # <D.19137>
                lp = _int(0)
                _pc = 93
                continue
            case 93:  # L.661
                _264 = card3_h1[0]
                path_aht[0] = _264
                D_12091 = _int(jmax)
                j = _int(1)
                _pc = 94
            case 94:  # <D.19140>
                D_12094 = _int(j > D_12091)
                _pc = 99 if D_12094 != 0 else 95
                continue
            case 95:  # <D.19141>
                _265 = _int(j)
                _266 = _265 + -1
                l = _int(sols_lj[_266])
                _267 = sols_jturn[0]
                _pc = 96 if j == _267 else 97
                continue
            case 96:  # <D.19142>
                lp = _int(1)
                _pc = 97
                continue
            case 97:  # L.664
                lz = _int(l + lp)
                _268 = _int(lz)
                _269 = _268 + -1
                _270 = j + 1
                _271 = _int(_270)
                _272 = _271 + -1
                _273 = rfrpth_zp[_269]
                path_aht[_272] = _273
                _pc = 98
            case 98:  # L.662
                j = _int(j + 1)
                _pc = 94
                continue
            case 99:  # __label_000046
                lp = _int(1)
                _274 = card3_len[0]
                _275 = _274 == 1
                _276 = card3_h1[0]
                _277 = card3_h2[0]
                _278 = _276 > _277
                _279 = _275 | _278
                _pc = 100 if _279 != 0 else 101
                continue
            case 100:  # <D.19145>
                lp = _int(0)
                _pc = 101
                continue
            case 101:  # L.665
                D_12100 = _int(jmax)
                j = _int(1)
                _pc = 102
            case 102:  # <D.19148>
                D_12103 = _int(j > D_12100)
                _pc = 107 if D_12103 != 0 else 103
                continue
            case 103:  # <D.19149>
                _280 = _int(j)
                _281 = _280 + -1
                l = _int(sols_lj[_281])
                _282 = sols_jturn[0]
                _pc = 104 if j == _282 else 105
                continue
            case 104:  # <D.19150>
                lp = _int(1)
                _pc = 105
                continue
            case 105:  # L.668
                lz = _int(l + lp)
                _pc = 106
            case 106:  # L.666
                j = _int(j + 1)
                _pc = 102
                continue
            case 107:  # __label_000315
                _283 = cntrl_issgeo[0]
                _pc = 108 if _283 == 1 else 109
                continue
            case 108:  # <D.19153>
                _pc = 117
                continue
            case 109:  # __label_000047
                lp = _int(1)
                _284 = card3_len[0]
                _285 = _284 == 1
                _286 = card3_h1[0]
                _287 = card3_h2[0]
                _288 = _286 > _287
                _289 = _285 | _288
                _pc = 110 if _289 != 0 else 111
                continue
            case 110:  # <D.19155>
                lp = _int(0)
                _pc = 111
                continue
            case 111:  # L.670
                D_12110 = _int(jmax)
                j = _int(1)
                _pc = 112
            case 112:  # <D.19158>
                D_12113 = _int(j > D_12110)
                _pc = 117 if D_12113 != 0 else 113
                continue
            case 113:  # <D.19159>
                _290 = _int(j)
                _291 = _290 + -1
                l = _int(sols_lj[_291])
                _292 = sols_jturn[0]
                _pc = 114 if j == _292 else 115
                continue
            case 114:  # <D.19160>
                lp = _int(1)
                _pc = 115
                continue
            case 115:  # L.673
                lz = _int(l + lp)
                _pc = 116
            case 116:  # L.671
                j = _int(j + 1)
                _pc = 112
                continue
            case 117:  # __label_000320
                _293 = __BLNK___w[6]
                _294 = _293 > 0.0
                _295 = __BLNK___ich[0]
                _296 = _295 <= 7
                _297 = _294 & _296
                _pc = 118 if _297 != 0 else 119
                continue
            case 118:  # <D.19163>
                _298 = __BLNK___w[14]
                _299 = __BLNK___w[6]
                w15 = _f32(_div(_298, _299))
                _pc = 119
                continue
            case 119:  # L.674
                _300 = __BLNK___w[11]
                _301 = _300 > 0.0
                _302 = __BLNK___ich[0]
                _303 = _302 > 7
                _304 = _301 & _303
                _pc = 120 if _304 != 0 else 121
                continue
            case 120:  # <D.19166>
                _305 = __BLNK___w[14]
                _306 = __BLNK___w[11]
                w15 = _f32(_div(_305, _306))
                _pc = 121
                continue
            case 121:  # L.675
                _307 = __BLNK___w[6]
                _308 = _307 > 0.0
                _309 = __BLNK___ich[0]
                _310 = _309 <= 7
                _311 = _308 & _310
                _pc = 122 if _311 != 0 else 123
                continue
            case 122:  # <D.19169>
                _312 = __builtin_expf(w15)
                _313 = 1.0e+2 - _312
                __BLNK___w[14] = _313
                _pc = 123
                continue
            case 123:  # L.676
                _314 = __BLNK___w[11]
                _315 = _314 > 0.0
                _316 = __BLNK___ich[0]
                _317 = _316 > 7
                _318 = _315 & _317
                _pc = 124 if _318 != 0 else 125
                continue
            case 124:  # <D.19172>
                _319 = __builtin_expf(w15)
                _320 = 1.0e+2 - _319
                __BLNK___w[14] = _320
                _pc = 125
                continue
            case 125:  # L.677
                _321 = __BLNK___w[6]
                _322 = _321 <= 0.0
                _323 = __BLNK___ich[0]
                _324 = _323 <= 7
                _325 = _322 & _324
                _pc = 126 if _325 != 0 else 127
                continue
            case 126:  # <D.19175>
                __BLNK___w[14] = 0.0
                _pc = 127
                continue
            case 127:  # L.678
                _326 = __BLNK___w[11]
                _327 = _326 <= 0.0
                _328 = __BLNK___ich[0]
                _329 = _328 > 7
                _330 = _327 & _329
                _pc = 128 if _330 != 0 else 129
                continue
            case 128:  # <D.19178>
                __BLNK___w[14] = 0.0
                _pc = 129
                continue
            case 129:  # L.679
                _331 = cntrl_issgeo[0]
                _pc = 130 if _331 == 1 else 131
                continue
            case 130:  # <D.19181>
                return
            case 131:  # __label_000060
                _332 = maxgeo[0]
                _pc = 132 if jmaxst > _332 else 133
                continue
            case 132:  # __label_000900
                _gfortran_stop_string(b"GEO :JMAXST .GT. MAXGEO", 23, 0)
                _pc = 133
            case 133:  # L.681
                D_12129 = _int(jmaxst)
                ik = _int(1)
                _pc = 134
            case 134:  # <D.19185>
                D_12132 = _int(ik > D_12129)
                _pc = -1 if D_12132 != 0 else 135
                continue
            case 135:  # <D.19186>
                _333 = _int(ik)
                _334 = _333 + -1
                il = _int(sols_lj[_334])
                _335 = _int(il)
                _336 = _335 + -1
                _337 = _int(ik)
                _338 = _337 + -1
                _339 = rfrpth_sp[_336]
                rain_rnpath[_338] = _339
                _340 = _int(il)
                _341 = _340 + -1
                _342 = _int(ik)
                _343 = _342 + -1
                _344 = model_rramt[_341]
                rain_rramtk[_343] = _344
                _pc = 136
            case 136:  # L.682
                ik = _int(ik + 1)
                _pc = 134
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_sctang(_state, anglst, thtst, psist, iarb):
    cnstns_deg = _state.view(246168, '<f4')
    D_19192 = _ZERO32
    psi = _ZERO32
    pthzen = _ZERO32
    sunzen = _ZERO32
    x = _ZERO32
    __result_sctang = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = anglst[0]
                _2 = cnstns_deg[0]
                sunzen = _f32(_div(_1, _2))
                _3 = thtst[0]
                _4 = cnstns_deg[0]
                pthzen = _f32(_div(_3, _4))
                _5 = iarb[0]
                _pc = 1 if _5 == 0 else 2
                continue
            case 1:  # <D.19190>
                _pc = 3
                continue
            case 2:  # L.684
                _6 = __builtin_cosf(sunzen)
                _7 = __builtin_cosf(pthzen)
                _8 = _6 * _7
                _9 = __builtin_acosf(_8)
                _10 = cnstns_deg[0]
                _11 = _9 * _10
                __result_sctang = _f32(_11)
                D_19192 = _f32(__result_sctang)
                return D_19192
            case 3:  # __label_000010
                _12 = psist[0]
                _13 = cnstns_deg[0]
                psi = _f32(_div(_12, _13))
                _14 = __builtin_sinf(sunzen)
                _15 = __builtin_sinf(pthzen)
                _16 = _14 * _15
                _17 = __builtin_cosf(psi)
                _18 = _16 * _17
                _19 = __builtin_cosf(sunzen)
                _20 = __builtin_cosf(pthzen)
                _21 = _19 * _20
                x = _f32(_18 + _21)
                _22 = __builtin_acosf(x)
                _23 = cnstns_deg[0]
                _24 = _22 * _23
                __result_sctang = _f32(_24)
                D_19192 = _f32(__result_sctang)
                return D_19192
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_del(_state, psio, delo, beta, iarbo):
    cnstns_deg = _state.view(246168, '<f4')
    D_19206 = _ZERO32
    betar = _ZERO32
    delor = _ZERO32
    psior = _ZERO32
    x = _ZERO32
    __result_del = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = iarbo[0]
                _pc = 1 if _1 == 0 else 2
                continue
            case 1:  # <D.19195>
                _pc = 9
                continue
            case 2:  # L.685
                _2 = iarbo[0]
                _pc = 3 if _2 == 1 else 4
                continue
            case 3:  # <D.19197>
                _3 = delo[0]
                __result_del = _f32(_3)
                _pc = 4
                continue
            case 4:  # L.686
                _4 = iarbo[0]
                _pc = 5 if _4 == 2 else 6
                continue
            case 5:  # <D.19200>
                _5 = beta[0]
                __result_del = _f32(_5)
                _pc = 6
                continue
            case 6:  # L.687
                _6 = iarbo[0]
                _pc = 7 if _6 == 3 else 8
                continue
            case 7:  # <D.19203>
                __result_del = _f32(0.0)
                _pc = 8
                continue
            case 8:  # L.688
                D_19206 = _f32(__result_del)
                return D_19206
            case 9:  # __label_000010
                _7 = psio[0]
                _8 = cnstns_deg[0]
                psior = _f32(_div(_7, _8))
                _9 = delo[0]
                _10 = cnstns_deg[0]
                delor = _f32(_div(_9, _10))
                _11 = beta[0]
                _12 = cnstns_deg[0]
                betar = _f32(_div(_11, _12))
                _13 = __builtin_cosf(delor)
                _14 = __builtin_cosf(betar)
                _15 = _13 * _14
                _16 = __builtin_sinf(delor)
                _17 = __builtin_sinf(betar)
                _18 = _16 * _17
                _19 = __builtin_cosf(psior)
                _20 = _18 * _19
                x = _f32(_15 + _20)
                _21 = __builtin_acosf(x)
                _22 = cnstns_deg[0]
                _23 = _21 * _22
                __result_del = _f32(_23)
                D_19206 = _f32(__result_del)
                return D_19206
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_psi(_state, psio, delo, beta, iarb, iarbo):
    cnstns_deg = _state.view(246168, '<f4')
    epsiln = _state.view(180328, '<f4')
    D_19213 = _ZERO32
    anumer = _ZERO32
    betar = _ZERO32
    delor = _ZERO32
    denom = _ZERO32
    psior = _ZERO32
    __result_psi = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = delo[0]
                _2 = cnstns_deg[0]
                delor = _f32(_div(_1, _2))
                _3 = beta[0]
                _4 = cnstns_deg[0]
                betar = _f32(_div(_3, _4))
                _5 = iarbo[0]
                _pc = 1 if _5 == 0 else 2
                continue
            case 1:  # <D.19209>
                _pc = 7
                continue
            case 2:  # L.689
                _6 = iarbo[0]
                iarb[0] = _6
                _7 = iarbo[0]
                _8 = _7 == 1
                _9 = iarbo[0]
                _10 = _9 == 3
                _11 = _8 | _10
                _pc = 3 if _11 != 0 else 4
                continue
            case 3:  # <D.19211>
                D_19213 = _f32(__result_psi)
                return D_19213
            case 4:  # L.690
                _12 = beta[0]
                epsiln_415_13 = epsiln[0]
                _pc = 5 if _12 <= epsiln_415_13 else 6
                continue
            case 5:  # <D.19214>
                D_19213 = _f32(__result_psi)
                return D_19213
            case 6:  # L.691
                iarb[0] = 0
                __result_psi = _f32(1.8e+2)
                D_19213 = _f32(__result_psi)
                return D_19213
            case 7:  # __label_000005
                _14 = psio[0]
                _15 = cnstns_deg[0]
                psior = _f32(_div(_14, _15))
                iarb[0] = 0
                _16 = __builtin_sinf(delor)
                _17 = __builtin_sinf(psior)
                anumer = _f32(_16 * _17)
                _18 = __builtin_cosf(betar)
                _19 = __builtin_sinf(delor)
                _20 = _18 * _19
                _21 = __builtin_cosf(psior)
                _22 = _20 * _21
                _23 = __builtin_sinf(betar)
                _24 = __builtin_cosf(delor)
                _25 = _23 * _24
                denom = _f32(_22 - _25)
                _26 = delo[0]
                epsiln_416_27 = epsiln[0]
                _pc = 8 if _26 > epsiln_416_27 else 9
                continue
            case 8:  # <D.19216>
                _pc = 13
                continue
            case 9:  # L.692
                _28 = beta[0]
                epsiln_417_29 = epsiln[0]
                _pc = 10 if _28 > epsiln_417_29 else 11
                continue
            case 10:  # <D.19218>
                _pc = 12
                continue
            case 11:  # L.693
                iarb[0] = 2
                D_19213 = _f32(__result_psi)
                return D_19213
            case 12:  # __label_000010
                __result_psi = _f32(1.8e+2)
                D_19213 = _f32(__result_psi)
                return D_19213
            case 13:  # __label_000020
                _30 = psio[0]
                _31 = abs(_30)
                epsiln_418_32 = epsiln[0]
                _pc = 14 if _31 > epsiln_418_32 else 15
                continue
            case 14:  # <D.19220>
                _pc = 23
                continue
            case 15:  # L.694
                _33 = beta[0]
                _34 = delo[0]
                _35 = _33 - _34
                _36 = abs(_35)
                epsiln_419_37 = epsiln[0]
                _pc = 16 if _36 >= epsiln_419_37 else 17
                continue
            case 16:  # <D.19222>
                _pc = 18
                continue
            case 17:  # L.695
                iarb[0] = 2
                D_19213 = _f32(__result_psi)
                return D_19213
            case 18:  # __label_000030
                _38 = beta[0]
                _39 = delo[0]
                _pc = 19 if _38 < _39 else 20
                continue
            case 19:  # <D.19224>
                __result_psi = _f32(0.0)
                _pc = 20
                continue
            case 20:  # L.696
                _40 = beta[0]
                _41 = delo[0]
                _pc = 21 if _40 > _41 else 22
                continue
            case 21:  # <D.19227>
                __result_psi = _f32(1.8e+2)
                _pc = 22
                continue
            case 22:  # L.697
                D_19213 = _f32(__result_psi)
                return D_19213
            case 23:  # __label_000040
                _42 = psio[0]
                _43 = abs(_42)
                epsiln_420_44 = epsiln[0]
                _45 = 1.8e+2 - epsiln_420_44
                _46 = _45
                _pc = 24 if _43 < _46 else 25
                continue
            case 24:  # <D.19230>
                _pc = 26
                continue
            case 25:  # L.698
                __result_psi = _f32(1.8e+2)
                D_19213 = _f32(__result_psi)
                return D_19213
            case 26:  # __label_000060
                _47 = abs(denom)
                epsiln_421_48 = epsiln[0]
                _pc = 27 if _47 > epsiln_421_48 else 28
                continue
            case 27:  # <D.19232>
                _pc = 33
                continue
            case 28:  # L.699
                _49 = psio[0]
                _pc = 29 if _49 < 0.0 else 30
                continue
            case 29:  # <D.19234>
                __result_psi = _f32(-9.0e+1)
                _pc = 30
                continue
            case 30:  # L.700
                _50 = psio[0]
                _pc = 31 if _50 > 0.0 else 32
                continue
            case 31:  # <D.19237>
                __result_psi = _f32(9.0e+1)
                _pc = 32
                continue
            case 32:  # L.701
                D_19213 = _f32(__result_psi)
                return D_19213
            case 33:  # __label_000080
                _51 = _div(anumer, denom)
                _52 = __builtin_atanf(_51)
                _53 = cnstns_deg[0]
                _54 = _52 * _53
                __result_psi = _f32(_54)
                _55 = psio[0]
                _56 = _55 > 0.0
                __result_psi_422_57 = __result_psi
                _58 = __result_psi_422_57 < 0.0
                _59 = _56 & _58
                _pc = 34 if _59 != 0 else 35
                continue
            case 34:  # <D.19240>
                __result_psi_423_60 = __result_psi
                _61 = __result_psi_423_60 + 1.8e+2
                __result_psi = _f32(_61)
                _pc = 35
                continue
            case 35:  # L.702
                _62 = psio[0]
                _63 = _62 < 0.0
                __result_psi_424_64 = __result_psi
                _65 = __result_psi_424_64 > 0.0
                _66 = _63 & _65
                _pc = 36 if _66 != 0 else 37
                continue
            case 36:  # <D.19243>
                __result_psi_425_67 = __result_psi
                _68 = __result_psi_425_67 - 1.8e+2
                __result_psi = _f32(_68)
                _pc = 37
                continue
            case 37:  # L.703
                D_19213 = _f32(__result_psi)
                return D_19213
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_psidel(_state, thetas, phis, thetao, phio, psipo2, psio, delo, iarbo):
    cnstns_deg = _state.view(246168, '<f4')
    epsiln = _state.view(180332, '<f4')
    anumer = _ZERO32
    cdphi = _ZERO32
    cto = _ZERO32
    cts = _ZERO32
    denom = _ZERO32
    dph = _ZERO32
    dphi = _ZERO32
    dtht = _ZERO32
    psipo = _ZERO32
    psiso = _ZERO32
    sdphi = _ZERO32
    sto = _ZERO32
    sts = _ZERO32
    thto = _ZERO32
    thts = _ZERO32
    tto = _ZERO32
    tts = _ZERO32
    D_12314 = _ZERO32
    D_12315 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = psipo2[0]
                psipo = _f32(9.0e+1 - _1)
                _pc = 1 if psipo > 1.8e+2 else 2
                continue
            case 1:  # <D.19248>
                psipo = _f32(psipo - 3.6e+2)
                _pc = 2
                continue
            case 2:  # L.704
                _2 = phis[0]
                _3 = phio[0]
                dphi = _f32(_2 - _3)
                _4 = thetas[0]
                _5 = thetao[0]
                dtht = _f32(_4 - _5)
                _6 = thetas[0]
                _7 = cnstns_deg[0]
                thts = _f32(_div(_6, _7))
                _8 = thetao[0]
                _9 = cnstns_deg[0]
                thto = _f32(_div(_8, _9))
                _10 = cnstns_deg[0]
                dph = _f32(_div(dphi, _10))
                sts = _f32(__builtin_sinf(thts))
                sto = _f32(__builtin_sinf(thto))
                cts = _f32(__builtin_cosf(thts))
                cto = _f32(__builtin_cosf(thto))
                sdphi = _f32(__builtin_sinf(dph))
                cdphi = _f32(__builtin_cosf(dph))
                tts = _f32(__builtin_tanf(thts))
                tto = _f32(__builtin_tanf(thto))
                _11 = abs(dphi)
                epsiln_426_12 = epsiln[0]
                _pc = 3 if _11 > epsiln_426_12 else 4
                continue
            case 3:  # <D.19251>
                _pc = 5
                continue
            case 4:  # L.705
                _13 = abs(dtht)
                delo[0] = _13
                _pc = 9
                continue
            case 5:  # __label_000010
                _14 = abs(dtht)
                epsiln_427_15 = epsiln[0]
                _pc = 6 if _14 > epsiln_427_15 else 7
                continue
            case 6:  # <D.19253>
                _pc = 8
                continue
            case 7:  # L.706
                _16 = abs(dphi)
                delo[0] = _16
                _pc = 9
                continue
            case 8:  # __label_000020
                _17 = cts * cto
                _18 = cdphi * _17
                _19 = sts * sto
                _20 = _18 + _19
                _21 = __builtin_acosf(_20)
                _22 = cnstns_deg[0]
                _23 = _21 * _22
                delo[0] = _23
                _pc = 9
            case 9:  # __label_000030
                _24 = delo[0]
                epsiln_428_25 = epsiln[0]
                _pc = 10 if _24 <= epsiln_428_25 else 11
                continue
            case 10:  # <D.19255>
                delo[0] = 0.0
                _pc = 11
                continue
            case 11:  # L.707
                _26 = delo[0]
                _pc = 12 if _26 == 0.0 else 13
                continue
            case 12:  # <D.19258>
                _27 = iarbo[0]
                _28 = _27 + 2
                iarbo[0] = _28
                _pc = 13
                continue
            case 13:  # L.708
                _29 = iarbo[0]
                _pc = 14 if _29 == 0 else 15
                continue
            case 14:  # <D.19261>
                _pc = 16
                continue
            case 15:  # L.709
                return
            case 16:  # __label_000040
                _30 = tto * cdphi
                anumer = _f32(_30 - tts)
                D_12314 = _f32(tto)
                D_12315 = _f32(D_12314 * D_12314)
                _31 = D_12315 + 1.0e+0
                _32 = _31
                _33 = cto * _32
                denom = _f32(sdphi * _33)
                _34 = abs(anumer)
                epsiln_429_35 = epsiln[0]
                _pc = 17 if _34 > epsiln_429_35 else 18
                continue
            case 17:  # <D.19263>
                _pc = 21
                continue
            case 18:  # L.710
                psiso = _f32(0.0)
                _pc = 19 if dphi > 0.0 else 20
                continue
            case 19:  # <D.19265>
                psiso = _f32(1.8e+2)
                _pc = 20
                continue
            case 20:  # L.711
                _pc = 37
                continue
            case 21:  # __label_000050
                _36 = abs(denom)
                epsiln_430_37 = epsiln[0]
                _pc = 22 if _36 > epsiln_430_37 else 23
                continue
            case 22:  # <D.19268>
                _pc = 26
                continue
            case 23:  # L.712
                psiso = _f32(9.0e+1)
                _pc = 24 if dtht < 0.0 else 25
                continue
            case 24:  # <D.19270>
                psiso = _f32(-9.0e+1)
                _pc = 25
                continue
            case 25:  # L.713
                _pc = 37
                continue
            case 26:  # __label_000060
                _38 = _div(anumer, denom)
                _39 = __builtin_atanf(_38)
                _40 = cnstns_deg[0]
                psiso = _f32(_39 * _40)
                _pc = 27 if dphi < 0.0 else 28
                continue
            case 27:  # <D.19273>
                _pc = 37
                continue
            case 28:  # L.714
                _pc = 29 if dphi > 0.0 else 30
                continue
            case 29:  # <D.19275>
                _pc = 33
                continue
            case 30:  # L.715
                psiso = _f32(9.0e+1)
                _pc = 31 if dtht < 0.0 else 32
                continue
            case 31:  # <D.19277>
                psiso = _f32(-9.0e+1)
                _pc = 32
                continue
            case 32:  # L.716
                _pc = 37
                continue
            case 33:  # __label_000070
                _pc = 34 if psiso > 0.0 else 35
                continue
            case 34:  # <D.19280>
                _pc = 36
                continue
            case 35:  # L.717
                psiso = _f32(psiso + 1.8e+2)
                _pc = 37
                continue
            case 36:  # __label_000080
                psiso = _f32(psiso - 1.8e+2)
                _pc = 37
            case 37:  # __label_000090
                _41 = phis[0]
                _pc = 38 if _41 > 1.8e+2 else 43
                continue
            case 38:  # <D.19282>
                psipo = _f32(psipo + 1.8e+2)
                _42 = phis[0]
                _pc = 39 if _42 > 3.6e+2 else 40
                continue
            case 39:  # <D.19284>
                psipo = _f32(psipo - 3.6e+2)
                _pc = 40
                continue
            case 40:  # L.719
                _pc = 41 if psiso < 0.0 else 42
                continue
            case 41:  # <D.19287>
                psiso = _f32(1.8e+2 - psiso)
                _pc = 42
                continue
            case 42:  # L.720
                _pc = 43
                continue
            case 43:  # L.718
                _43 = psiso - psipo
                psio[0] = _43
                _44 = psio[0]
                _pc = 44 if _44 < -1.8e+2 else 45
                continue
            case 44:  # <D.19291>
                _45 = psio[0]
                _46 = _45 + 3.6e+2
                psio[0] = _46
                _pc = 45
                continue
            case 45:  # L.721
                _47 = psio[0]
                _pc = 46 if _47 > 1.8e+2 else -1
                continue
            case 46:  # <D.19294>
                _48 = psio[0]
                _49 = _48 - 3.6e+2
                psio[0] = _49
                _pc = -1
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_rfpath(_state, h1, h2, angle, phi, len, hmin, iamt, beta, range, bendng):
    cnstns_ca = _state.view(246164, '<f4')
    cnstns_deg = _state.view(246168, '<f4')
    cntrl_issgeo = _state.view(245624, '<i4')
    parmtr_re = _state.view(245632, '<f4')
    parmtr_ipath = _state.view(245656, '<i4')
    path_pl = _state.view(242144, '<f4')
    path_qtheta = _state.view(242416, '<f4')
    rfrpth_zp = _state.view(246784, '<f4')
    rfrpth_rfndxp = _state.view(247204, '<f4')
    rfrpth_ppsum = _state.view(247484, '<f4')
    rfrpth_tpsum = _state.view(247624, '<f4')
    rfrpth_rhopsm = _state.view(247764, '<f4')
    sols_atheta = _state.view(207696, '<f4')
    sols_adbeta = _state.view(207836, '<f4')
    anglea = _ZERO32
    cosai = _zeros(1, '<f4')
    cpath = _zeros(1, '<f4')
    dbend = _zeros(1, '<f4')
    dbeta = _ZERO32
    ds = _zeros(1, '<f4')
    gamma = _zeros(1, '<f4')
    ha = _zeros(1, '<f4')
    hb = _zeros(1, '<f4')
    ihigh = 0
    ihlow = 0
    iorder = 0
    j = _zeros(1, '<i4')
    j1 = 0
    j2 = 0
    j2a = 0
    j2b = 0
    ja = 0
    jd = 0
    jha = 0
    jmax = 0
    jnext = _zeros(1, '<i4')
    jo = 0
    ka = 0
    v_max = 0
    pbar = _ZERO32
    rhobar = _ZERO32
    s = _ZERO32
    sh = _zeros(1, '<f4')
    sinai = _zeros(1, '<f4')
    tbar = _ZERO32
    theta = _ZERO32
    D_12546 = 0
    D_12549 = 0
    D_12582 = 0
    D_12585 = 0
    D_12589 = 0
    D_12590 = 0
    D_12593 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                v_max = _int(0)
                _1 = h1[0]
                _2 = h2[0]
                _pc = 1 if _1 > _2 else 2
                continue
            case 1:  # <D.19298>
                _pc = 3
                continue
            case 2:  # L.723
                iorder = _int(1)
                _3 = h1[0]
                ha[0] = _3
                _4 = h2[0]
                hb[0] = _4
                anglea = _f32(angle[0])
                _pc = 4
                continue
            case 3:  # __label_000090
                iorder = _int(-1)
                _5 = h2[0]
                ha[0] = _5
                _6 = h1[0]
                hb[0] = _6
                anglea = _f32(phi[0])
                _pc = 4
            case 4:  # __label_000095
                jnext[0] = 1
                _pc = 5
            case 5:  # __label_000020
                _7 = len[0]
                _pc = 6 if _7 == 0 else 7
                continue
            case 6:  # <D.19300>
                _pc = 8
                continue
            case 7:  # L.724
                _ft_fill(_state, hmin, ha, jnext)
                jha = _int(jnext[0])
                _pc = 8
            case 8:  # __label_000100
                ha_431_8 = ha[0]
                hb_432_9 = hb[0]
                _pc = 9 if ha_431_8 == hb_432_9 else 10
                continue
            case 9:  # <D.19302>
                _pc = 11
                continue
            case 10:  # L.725
                _ft_fill(_state, ha, hb, jnext)
                _pc = 11
            case 11:  # __label_000110
                jmax = _int(jnext[0])
                parmtr_ipath[0] = jmax
                _10 = len[0]
                _pc = 12 if _10 == 1 else 13
                continue
            case 12:  # <D.19304>
                _pc = 14
                continue
            case 13:  # L.726
                _ft_findsh(_state, ha, sh, gamma)
                _11 = parmtr_re[0]
                ha_433_12 = ha[0]
                _13 = _11 + ha_433_12
                _14 = _13
                _15 = _ft_andex(_state, ha, sh, gamma)
                _16 = _14 * _15
                _17 = cnstns_deg[0]
                _18 = _div(anglea, _17)
                _19 = __builtin_sinf(_18)
                _20 = _16 * _19
                cpath[0] = _20
                _pc = 15
                continue
            case 14:  # __label_000115
                _ft_findsh(_state, hmin, sh, gamma)
                _21 = hmin[0]
                _22 = parmtr_re[0]
                _23 = _21 + _22
                _24 = _23
                _25 = _ft_andex(_state, hmin, sh, gamma)
                _26 = _24 * _25
                cpath[0] = _26
                _pc = 15
            case 15:  # __label_000116
                beta[0] = 0.0
                s = _f32(0.0)
                bendng[0] = 0.0
                _27 = len[0]
                _pc = 16 if _27 == 0 else 17
                continue
            case 16:  # <D.19306>
                _pc = 31
                continue
            case 17:  # L.727
                ihlow = _int(1)
                _pc = 18 if iorder == -1 else 19
                continue
            case 18:  # <D.19308>
                ihlow = _int(2)
                _pc = 19
                continue
            case 19:  # __label_000024
                sinai[0] = 1.0e+0
                cosai[0] = 0.0
                theta = _f32(9.0e+1)
                j2 = _int(jha + -1)
                D_12546 = _int(j2)
                j[0] = 1
                _pc = 20
            case 20:  # <D.19311>
                j_434_28 = j[0]
                D_12549 = _int(D_12546 < j_434_28)
                _pc = 29 if D_12549 != 0 else 21
                continue
            case 21:  # <D.19312>
                j_435_29 = j[0]
                _30 = j_435_29 + 1
                _31 = _int(_30)
                _32 = _31 + -1
                _33 = rfrpth_rfndxp[_32:]
                j_436_34 = j[0]
                _35 = _int(j_436_34)
                _36 = _35 + -1
                _37 = rfrpth_rfndxp[_36:]
                j_437_38 = j[0]
                _39 = j_437_38 + 1
                _40 = _int(_39)
                _41 = _40 + -1
                _42 = rfrpth_zp[_41:]
                j_438_43 = j[0]
                _44 = _int(j_438_43)
                _45 = _44 + -1
                _46 = rfrpth_zp[_45:]
                _ft_scalht(_state, _46, _42, _37, _33, sh, gamma)
                _ft_layer(_state, j, sinai, cosai, cpath, sh, gamma, iamt, ds, dbend)
                dbend_439_47 = dbend[0]
                _48 = cnstns_deg[0]
                _49 = dbend_439_47 * _48
                dbend[0] = _49
                sinai_440_50 = sinai[0]
                _51 = __builtin_asinf(sinai_440_50)
                _52 = cnstns_deg[0]
                _53 = _51 * _52
                phi[0] = _53
                _54 = phi[0]
                _55 = theta - _54
                dbend_441_56 = dbend[0]
                dbeta = _f32(_55 + dbend_441_56)
                _57 = phi[0]
                _58 = 1.8e+2 - _57
                phi[0] = _58
                ds_442_59 = ds[0]
                s = _f32(s + ds_442_59)
                _60 = bendng[0]
                dbend_443_61 = dbend[0]
                _62 = _60 + dbend_443_61
                bendng[0] = _62
                _63 = beta[0]
                _64 = dbeta + _63
                beta[0] = _64
                _65 = iamt[0]
                _pc = 22 if _65 != 1 else 23
                continue
            case 22:  # <D.19313>
                _pc = 24
                continue
            case 23:  # L.731
                j_444_66 = j[0]
                _67 = _int(j_444_66)
                _68 = _67 + -1
                _69 = rfrpth_ppsum[_68]
                j_445_70 = j[0]
                _71 = _int(j_445_70)
                _72 = _71 + -1
                _73 = rfrpth_rhopsm[_72]
                pbar = _f32(_div(_69, _73))
                j_446_74 = j[0]
                _75 = _int(j_446_74)
                _76 = _75 + -1
                _77 = rfrpth_tpsum[_76]
                j_447_78 = j[0]
                _79 = _int(j_447_78)
                _80 = _79 + -1
                _81 = rfrpth_rhopsm[_80]
                tbar = _f32(_div(_77, _81))
                j_448_82 = j[0]
                _83 = _int(j_448_82)
                _84 = _83 + -1
                _85 = rfrpth_rhopsm[_84]
                ds_449_86 = ds[0]
                rhobar = _f32(_div(_85, ds_449_86))
                j_450_87 = j[0]
                _88 = j2 - j_450_87
                j2a = _int(_88 + 1)
                j_451_89 = j[0]
                j2b = _int(j2 + j_451_89)
                _90 = phi[0]
                _91 = cnstns_ca[0]
                _92 = _int(j2a)
                _93 = _92 + -1
                _94 = _90 * _91
                path_qtheta[_93] = _94
                _95 = cnstns_ca[0]
                _96 = _int(j2b)
                _97 = _96 + -1
                _98 = theta * _95
                path_qtheta[_97] = _98
                v_max = _int(j2b)
                _pc = 24
            case 24:  # __label_000118
                _99 = cntrl_issgeo[0]
                _pc = 25 if _99 == 1 else 26
                continue
            case 25:  # <D.19315>
                _pc = 27
                continue
            case 26:  # L.732
                j_452_100 = j[0]
                _101 = _int(j_452_100)
                _102 = _101 + -1
                sols_atheta[_102] = theta
                j_453_103 = j[0]
                _104 = _int(j_453_103)
                _105 = _104 + -1
                sols_adbeta[_105] = dbeta
                _pc = 27
            case 27:  # __label_000119
                _106 = phi[0]
                theta = _f32(1.8e+2 - _106)
                _pc = 28
            case 28:  # L.729
                j_454_107 = j[0]
                _108 = j_454_107 + 1
                j[0] = _108
                _pc = 20
                continue
            case 29:  # L.730
                _109 = bendng[0]
                _110 = _109 * 2.0e+0
                bendng[0] = _110
                _111 = beta[0]
                _112 = _111 * 2.0e+0
                beta[0] = _112
                s = _f32(s * 2.0e+0)
                _pc = 30
            case 30:  # __label_000026
                jnext[0] = jha
                _pc = 35
                continue
            case 31:  # __label_000140
                jnext[0] = 1
                theta = _f32(anglea)
                _pc = 32 if anglea > 4.5e+1 else 33
                continue
            case 32:  # <D.19317>
                _pc = 34
                continue
            case 33:  # L.733
                _113 = cnstns_deg[0]
                _114 = _div(anglea, _113)
                _115 = __builtin_sinf(_114)
                sinai[0] = _115
                _116 = cnstns_deg[0]
                _117 = _div(anglea, _116)
                _118 = __builtin_cosf(_117)
                _119 = -_118
                cosai[0] = _119
                _pc = 35
                continue
            case 34:  # __label_000145
                _120 = 9.0e+1 - anglea
                _121 = _120
                _122 = cnstns_deg[0]
                _123 = _div(_121, _122)
                _124 = __builtin_cosf(_123)
                sinai[0] = _124
                _125 = 9.0e+1 - anglea
                _126 = _125
                _127 = cnstns_deg[0]
                _128 = _div(_126, _127)
                _129 = __builtin_sinf(_128)
                _130 = -_129
                cosai[0] = _130
                _pc = 35
            case 35:  # __label_000150
                ha_455_131 = ha[0]
                hb_456_132 = hb[0]
                _pc = 36 if ha_455_131 == hb_456_132 else 37
                continue
            case 36:  # <D.19319>
                _pc = 59
                continue
            case 37:  # L.734
                jnext_457_133 = jnext[0]
                _134 = v_max - jnext_457_133
                jo = _int(_134 + 1)
                j1 = _int(jnext[0])
                j2 = _int(jmax + -1)
                _135 = h1[0]
                _136 = h2[0]
                _pc = 38 if _135 > _136 else 43
                continue
            case 38:  # <D.19321>
                _137 = j2 - j1
                jd = _int(_137 + 1)
                D_12582 = _int(v_max)
                j[0] = 1
                _pc = 39
            case 39:  # <D.19323>
                j_458_138 = j[0]
                D_12585 = _int(D_12582 < j_458_138)
                _pc = 42 if D_12585 != 0 else 40
                continue
            case 40:  # <D.19324>
                j_459_139 = j[0]
                _140 = v_max - j_459_139
                ka = _int(_140 + 1)
                ja = _int(ka + jd)
                _141 = _int(ka)
                _142 = _141 + -1
                _143 = _int(ja)
                _144 = _143 + -1
                _145 = path_qtheta[_142]
                path_qtheta[_144] = _145
                _pc = 41
            case 41:  # L.736
                j_460_146 = j[0]
                _147 = j_460_146 + 1
                j[0] = _147
                _pc = 39
                continue
            case 42:  # L.737
                v_max = _int(v_max + jd)
                jo = _int(0)
                _pc = 43
                continue
            case 43:  # L.735
                ihlow = _int(1)
                _pc = 44 if iorder == -1 else 45
                continue
            case 44:  # <D.19326>
                ihlow = _int(2)
                _pc = 45
                continue
            case 45:  # L.738
                _148 = ihlow % 2
                ihigh = _int(_148 + 1)
                _pc = 46
            case 46:  # __label_000028
                D_12589 = _int(j1)
                D_12590 = _int(j2)
                j[0] = D_12589
                _pc = 47
            case 47:  # <D.19329>
                j_461_149 = j[0]
                D_12593 = _int(D_12590 < j_461_149)
                _pc = 59 if D_12593 != 0 else 48
                continue
            case 48:  # <D.19330>
                j_462_150 = j[0]
                _151 = j_462_150 + 1
                _152 = _int(_151)
                _153 = _152 + -1
                _154 = rfrpth_rfndxp[_153:]
                j_463_155 = j[0]
                _156 = _int(j_463_155)
                _157 = _156 + -1
                _158 = rfrpth_rfndxp[_157:]
                j_464_159 = j[0]
                _160 = j_464_159 + 1
                _161 = _int(_160)
                _162 = _161 + -1
                _163 = rfrpth_zp[_162:]
                j_465_164 = j[0]
                _165 = _int(j_465_164)
                _166 = _165 + -1
                _167 = rfrpth_zp[_166:]
                _ft_scalht(_state, _167, _163, _158, _154, sh, gamma)
                _ft_layer(_state, j, sinai, cosai, cpath, sh, gamma, iamt, ds, dbend)
                dbend_466_168 = dbend[0]
                _169 = cnstns_deg[0]
                _170 = dbend_466_168 * _169
                dbend[0] = _170
                sinai_467_171 = sinai[0]
                _172 = __builtin_asinf(sinai_467_171)
                _173 = cnstns_deg[0]
                _174 = _172 * _173
                phi[0] = _174
                _175 = phi[0]
                _176 = theta - _175
                dbend_468_177 = dbend[0]
                dbeta = _f32(_176 + dbend_468_177)
                _178 = phi[0]
                _179 = 1.8e+2 - _178
                phi[0] = _179
                ds_469_180 = ds[0]
                s = _f32(s + ds_469_180)
                j_470_181 = j[0]
                _182 = _int(j_470_181)
                _183 = _182 + -1
                ds_471_184 = ds[0]
                path_pl[_183] = ds_471_184
                _185 = bendng[0]
                dbend_472_186 = dbend[0]
                _187 = _185 + dbend_472_186
                bendng[0] = _187
                _188 = beta[0]
                _189 = dbeta + _188
                beta[0] = _189
                _190 = iamt[0]
                _pc = 49 if _190 != 1 else 50
                continue
            case 49:  # <D.19331>
                _pc = 51
                continue
            case 50:  # L.741
                j_473_191 = j[0]
                _192 = _int(j_473_191)
                _193 = _192 + -1
                _194 = rfrpth_ppsum[_193]
                j_474_195 = j[0]
                _196 = _int(j_474_195)
                _197 = _196 + -1
                _198 = rfrpth_rhopsm[_197]
                pbar = _f32(_div(_194, _198))
                j_475_199 = j[0]
                _200 = _int(j_475_199)
                _201 = _200 + -1
                _202 = rfrpth_tpsum[_201]
                j_476_203 = j[0]
                _204 = _int(j_476_203)
                _205 = _204 + -1
                _206 = rfrpth_rhopsm[_205]
                tbar = _f32(_div(_202, _206))
                j_477_207 = j[0]
                _208 = _int(j_477_207)
                _209 = _208 + -1
                _210 = rfrpth_rhopsm[_209]
                ds_478_211 = ds[0]
                rhobar = _f32(_div(_210, ds_478_211))
                _pc = 51
            case 51:  # __label_000158
                _212 = h2[0]
                _213 = h1[0]
                _pc = 52 if _212 > _213 else 53
                continue
            case 52:  # <D.19333>
                _214 = cnstns_ca[0]
                j_479_215 = j[0]
                _216 = jo + j_479_215
                _217 = _int(_216)
                _218 = _217 + -1
                _219 = theta * _214
                path_qtheta[_218] = _219
                j_480_220 = j[0]
                v_max = _int(jo + j_480_220)
                _pc = 54
                continue
            case 53:  # <D.19334>
                j_481_221 = j[0]
                _222 = j2 - j_481_221
                j2b = _int(_222 + 1)
                _223 = phi[0]
                _224 = cnstns_ca[0]
                _225 = _int(j2b)
                _226 = _225 + -1
                _227 = _223 * _224
                path_qtheta[_226] = _227
                _pc = 54
            case 54:  # L.742
                _228 = cntrl_issgeo[0]
                _pc = 55 if _228 == 1 else 56
                continue
            case 55:  # <D.19336>
                _pc = 57
                continue
            case 56:  # L.743
                j_482_229 = j[0]
                _230 = _int(j_482_229)
                _231 = _230 + -1
                sols_adbeta[_231] = dbeta
                j_483_232 = j[0]
                _233 = _int(j_483_232)
                _234 = _233 + -1
                sols_atheta[_234] = theta
                _pc = 57
            case 57:  # __label_000159
                _235 = phi[0]
                theta = _f32(1.8e+2 - _235)
                _pc = 58
            case 58:  # L.739
                j_484_236 = j[0]
                _237 = j_484_236 + 1
                j[0] = _237
                _pc = 47
                continue
            case 59:  # __label_000170
                _238 = cntrl_issgeo[0]
                _pc = 60 if _238 == 0 else 61
                continue
            case 60:  # <D.19338>
                _239 = _int(jmax)
                _240 = _239 + -1
                sols_atheta[_240] = theta
                _pc = 61
                continue
            case 61:  # L.744
                _pc = 62 if iorder == -1 else 63
                continue
            case 62:  # <D.19341>
                phi[0] = anglea
                _pc = 63
                continue
            case 63:  # L.745
                range[0] = s
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_geoinp(_state, h1, h2, angle, range, beta, itype, len, hmin, phi, ierror):
    cnstns_deg = _state.view(246168, '<f4')
    parmtr_re = _state.view(245632, '<f4')
    parmtr_zmax = _state.view(245640, '<f4')
    erarg1 = _ZERO32
    erarg2 = _ZERO32
    erarg3 = _ZERO32
    h2st = _ZERO32
    iter = _zeros(1, '<i4')
    r1 = _ZERO32
    r2 = _ZERO32
    zarg1 = _ZERO32
    zarg2 = _ZERO32
    zarg3 = _ZERO32
    C_12668 = _array([9.0e+1], '<f4')
    C_12669 = _array([9.0e+1], '<f4')
    D_12697 = _ZERO32
    D_12698 = _ZERO32
    D_12699 = _ZERO32
    D_12700 = _ZERO32
    D_12703 = _ZERO32
    D_12704 = _ZERO32
    D_12705 = _ZERO32
    D_12706 = _ZERO32
    D_12707 = _ZERO32
    D_12708 = _ZERO32
    D_12710 = _ZERO32
    D_12711 = _ZERO32
    D_12712 = _ZERO32
    D_12713 = _ZERO32
    D_12714 = _ZERO32
    D_12715 = _ZERO32
    D_12724 = _ZERO32
    D_12725 = _ZERO32
    D_12726 = _ZERO32
    D_12727 = _ZERO32
    D_12728 = _ZERO32
    D_12729 = _ZERO32
    D_12734 = _ZERO32
    D_12735 = _ZERO32
    D_12736 = _ZERO32
    D_12737 = _ZERO32
    D_12738 = _ZERO32
    D_12739 = _ZERO32
    D_12748 = _ZERO32
    M_31 = _ZERO32
    D_12750 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                iter[0] = 0
                _1 = itype[0]
                _pc = 1 if _1 != 3 else 2
                continue
            case 1:  # <D.19344>
                _pc = 12
                continue
            case 2:  # L.746
                _2 = h2[0]
                _pc = 3 if _2 != 0.0 else 4
                continue
            case 3:  # <D.19346>
                _pc = 7
                continue
            case 4:  # __label_000010
                _3 = parmtr_zmax[0]
                h2[0] = _3
                _ft_fndhmn(_state, h1, angle, h2, len, iter, hmin, phi, ierror)
                _4 = ierror[0]
                _pc = 5 if _4 == -5 else 6
                continue
            case 5:  # <D.19348>
                return
            case 6:  # L.748
                _pc = 59
                continue
            case 7:  # __label_000012
                _5 = h2[0]
                hmin[0] = _5
                _6 = parmtr_zmax[0]
                h2[0] = _6
                _7 = h1[0]
                _8 = hmin[0]
                _pc = 8 if _7 < _8 else 9
                continue
            case 8:  # <D.19350>
                _pc = 68
                continue
            case 9:  # L.749
                _ft_fndhmn(_state, hmin, C_12668, h1, len, iter, hmin, angle, ierror)
                _ft_fndhmn(_state, hmin, C_12669, h2, len, iter, hmin, phi, ierror)
                _9 = hmin[0]
                _10 = h1[0]
                _pc = 10 if _9 < _10 else 11
                continue
            case 10:  # <D.19352>
                len[0] = 1
                _pc = 11
                continue
            case 11:  # L.750
                _pc = 59
                continue
            case 12:  # __label_000120
                _11 = itype[0]
                _pc = 13 if _11 != 2 else 14
                continue
            case 13:  # <D.19355>
                _pc = 69
                continue
            case 14:  # L.751
                _12 = range[0]
                _13 = _12 != 0.0
                _14 = beta[0]
                _15 = _14 != 0.0
                _16 = _13 | _15
                _pc = 15 if _16 != 0 else 16
                continue
            case 15:  # <D.19357>
                _pc = 23
                continue
            case 16:  # __label_000016
                _17 = h1[0]
                _18 = h2[0]
                _19 = _17 >= _18
                _20 = angle[0]
                _21 = _20 <= 9.0e+1
                _22 = _19 & _21
                _pc = 17 if _22 != 0 else 18
                continue
            case 17:  # <D.19359>
                _pc = 71
                continue
            case 18:  # L.753
                _23 = h1[0]
                _24 = _23 == 0.0
                _25 = angle[0]
                _26 = _25 > 9.0e+1
                _27 = _24 & _26
                _pc = 19 if _27 != 0 else 20
                continue
            case 19:  # <D.19361>
                _pc = 72
                continue
            case 20:  # __label_000015
                h2st = _f32(h2[0])
                _ft_fndhmn(_state, h1, angle, h2, len, iter, hmin, phi, ierror)
                _28 = h2[0]
                _pc = 21 if h2st != _28 else 22
                continue
            case 21:  # <D.19363>
                _pc = 72
                continue
            case 22:  # L.755
                _pc = 59
                continue
            case 23:  # __label_000130
                _29 = beta[0]
                _pc = 24 if _29 == 0.0 else 25
                continue
            case 24:  # <D.19365>
                _pc = 26
                continue
            case 25:  # L.756
                _ft_fdbeta(_state, h1, h2, beta, angle, phi, len, hmin, ierror)
                _pc = 59
                continue
            case 26:  # __label_000133
                _30 = angle[0]
                _pc = 27 if _30 == 0.0 else 28
                continue
            case 27:  # <D.19367>
                _pc = 40
                continue
            case 28:  # __label_000018
                _31 = h1[0]
                _32 = parmtr_re[0]
                r1 = _f32(_31 + _32)
                D_12697 = _f32(r1)
                D_12698 = _f32(D_12697 * D_12697)
                D_12699 = _f32(range[0])
                D_12700 = _f32(D_12699 * D_12699)
                _33 = D_12698 + D_12700
                _34 = r1 * 2.0e+0
                _35 = range[0]
                _36 = _34 * _35
                _37 = angle[0]
                _38 = cnstns_deg[0]
                _39 = _div(_37, _38)
                _40 = __builtin_cosf(_39)
                _41 = _36 * _40
                _42 = _33 + _41
                r2 = _f32(__builtin_sqrtf(_42))
                _43 = parmtr_re[0]
                _44 = r2 - _43
                h2[0] = _44
                _45 = h2[0]
                _pc = 29 if _45 >= 0.0 else 30
                continue
            case 29:  # <D.19369>
                _pc = 31
                continue
            case 30:  # L.758
                h2[0] = 0.0
                _46 = h2[0]
                _47 = parmtr_re[0]
                r2 = _f32(_46 + _47)
                D_12703 = _f32(r2)
                D_12704 = _f32(D_12703 * D_12703)
                D_12705 = _f32(r1)
                D_12706 = _f32(D_12705 * D_12705)
                _48 = angle[0]
                _49 = cnstns_deg[0]
                _50 = _div(_48, _49)
                _51 = __builtin_sinf(_50)
                D_12707 = _f32(_51)
                D_12708 = _f32(D_12707 * D_12707)
                _52 = angle[0]
                _53 = cnstns_deg[0]
                _54 = _div(_52, _53)
                _55 = __builtin_cosf(_54)
                _56 = r1 * _55
                _57 = -_56
                _58 = D_12706 * D_12708
                _59 = D_12704 - _58
                _60 = __builtin_sqrtf(_59)
                _61 = _57 - _60
                range[0] = _61
                _pc = 31
            case 31:  # __label_000135
                D_12710 = _f32(r2)
                D_12711 = _f32(D_12710 * D_12710)
                D_12712 = _f32(range[0])
                D_12713 = _f32(D_12712 * D_12712)
                D_12714 = _f32(r1)
                D_12715 = _f32(D_12714 * D_12714)
                _62 = D_12711 + D_12713
                _63 = _62 - D_12715
                _64 = _63
                _65 = r2 * 2.0e+0
                _66 = range[0]
                _67 = _65 * _66
                _68 = _67
                zarg1 = _f32(_div(_64, _68))
                _69 = abs(zarg1)
                erarg1 = _f32(_69 - 1.0e+0)
                _70 = erarg1 > 9.999999974752427078783512115478515625e-7
                _71 = erarg1 < 0.0
                _72 = _70 | _71
                _pc = 32 if _72 != 0 else 33
                continue
            case 32:  # <D.19371>
                _pc = 37
                continue
            case 33:  # L.759
                _pc = 34 if zarg1 < 0.0 else 35
                continue
            case 34:  # <D.19373>
                _pc = 36
                continue
            case 35:  # L.760
                zarg1 = _f32(1.0e+0)
                _pc = 37
                continue
            case 36:  # __label_000138
                zarg1 = _f32(-1.0e+0)
                _pc = 37
            case 37:  # __label_000137
                _73 = __builtin_acosf(zarg1)
                _74 = cnstns_deg[0]
                _75 = _73 * _74
                _76 = 1.8e+2 - _75
                phi[0] = _76
                len[0] = 0
                _77 = angle[0]
                _78 = _77 > 9.0e+1
                _79 = phi[0]
                _80 = _79 > 9.0e+1
                _81 = _78 & _80
                _pc = 38 if _81 != 0 else 39
                continue
            case 38:  # <D.19375>
                len[0] = 1
                _pc = 39
                continue
            case 39:  # L.761
                _ft_fndhmn(_state, h1, angle, h2, len, iter, hmin, phi, ierror)
                _pc = 59
                continue
            case 40:  # __label_000019
                _82 = h1[0]
                _83 = h2[0]
                _84 = _82 - _83
                _85 = abs(_84)
                _86 = range[0]
                _pc = 41 if _85 > _86 else 42
                continue
            case 41:  # <D.19378>
                _pc = 70
                continue
            case 42:  # L.762
                _87 = h1[0]
                _88 = parmtr_re[0]
                r1 = _f32(_87 + _88)
                _89 = h2[0]
                _90 = parmtr_re[0]
                r2 = _f32(_89 + _90)
                D_12724 = _f32(r1)
                D_12725 = _f32(D_12724 * D_12724)
                D_12726 = _f32(range[0])
                D_12727 = _f32(D_12726 * D_12726)
                D_12728 = _f32(r2)
                D_12729 = _f32(D_12728 * D_12728)
                _91 = D_12725 + D_12727
                _92 = _91 - D_12729
                _93 = _92
                _94 = r1 * 2.0e+0
                _95 = range[0]
                _96 = _94 * _95
                _97 = _96
                zarg2 = _f32(_div(_93, _97))
                _98 = abs(zarg2)
                erarg2 = _f32(_98 - 1.0e+0)
                _99 = erarg2 > 9.999999974752427078783512115478515625e-7
                _100 = erarg2 < 0.0
                _101 = _99 | _100
                _pc = 43 if _101 != 0 else 44
                continue
            case 43:  # <D.19380>
                _pc = 48
                continue
            case 44:  # L.763
                _pc = 45 if zarg2 < 0.0 else 46
                continue
            case 45:  # <D.19382>
                _pc = 47
                continue
            case 46:  # L.764
                zarg2 = _f32(1.0e+0)
                _pc = 48
                continue
            case 47:  # __label_000188
                zarg2 = _f32(-1.0e+0)
                _pc = 48
            case 48:  # __label_000187
                _102 = __builtin_acosf(zarg2)
                _103 = cnstns_deg[0]
                _104 = _102 * _103
                _105 = 1.8e+2 - _104
                angle[0] = _105
                D_12734 = _f32(r2)
                D_12735 = _f32(D_12734 * D_12734)
                D_12736 = _f32(range[0])
                D_12737 = _f32(D_12736 * D_12736)
                D_12738 = _f32(r1)
                D_12739 = _f32(D_12738 * D_12738)
                _106 = D_12735 + D_12737
                _107 = _106 - D_12739
                _108 = _107
                _109 = r2 * 2.0e+0
                _110 = range[0]
                _111 = _109 * _110
                _112 = _111
                zarg3 = _f32(_div(_108, _112))
                _113 = abs(zarg3)
                erarg3 = _f32(_113 - 1.0e+0)
                _114 = erarg3 > 9.999999974752427078783512115478515625e-7
                _115 = erarg3 < 0.0
                _116 = _114 | _115
                _pc = 49 if _116 != 0 else 50
                continue
            case 49:  # <D.19384>
                _pc = 54
                continue
            case 50:  # L.765
                _pc = 51 if zarg3 < 0.0 else 52
                continue
            case 51:  # <D.19386>
                _pc = 53
                continue
            case 52:  # L.766
                zarg3 = _f32(1.0e+0)
                _pc = 54
                continue
            case 53:  # __label_000198
                zarg3 = _f32(-1.0e+0)
                _pc = 54
            case 54:  # __label_000197
                _117 = __builtin_acosf(zarg3)
                _118 = cnstns_deg[0]
                _119 = _117 * _118
                _120 = 1.8e+2 - _119
                phi[0] = _120
                # Numerically stable central angle from the chord length.
                # Original Fortran: BETA = PHI + ANGLE - 180.
                # For short slant paths two angles near 180 degrees are
                # subtracted in float32, losing the small central angle.
                # Use double precision for the haversine/chord relation,
                # then store BETA as float32, matching the Fortran patch.
                range_d = float(range[0])
                height_diff_d = float(h2[0]) - float(h1[0])
                denominator_d = 4.0 * float(r1) * float(r2)
                chord_term_d = max(0.0, (range_d**2 - height_diff_d**2) / denominator_d)
                beta[0] = _f32(2.0 * float(cnstns_deg[0]) * math.asin(math.sqrt(chord_term_d)))
                _125 = range[0]
                _126 = _125 > 2.0e+0
                _127 = beta[0]
                _128 = _127 > 0.0
                _129 = _126 & _128
                _pc = 55 if _129 != 0 else 56
                continue
            case 55:  # <D.19388>
                _ft_fdbeta(_state, h1, h2, beta, angle, phi, len, hmin, ierror)
                _pc = 59
                continue
            case 56:  # <D.19389>
                len[0] = 0
                _130 = angle[0]
                _131 = _130 > 9.0e+1
                _132 = phi[0]
                _133 = _132 > 9.0e+1
                _134 = _131 & _133
                _pc = 57 if _134 != 0 else 58
                continue
            case 57:  # <D.19391>
                len[0] = 1
                _pc = 58
                continue
            case 58:  # L.768
                _ft_fndhmn(_state, h1, angle, h2, len, iter, hmin, phi, ierror)
                _pc = 59
            case 59:  # __label_000200
                _135 = ierror[0]
                _pc = 60 if _135 != 0 else 61
                continue
            case 60:  # <D.19394>
                return
            case 61:  # L.769
                len[0] = 0
                D_12748 = _f32(h1[0])
                M_31 = _f32(D_12748)
                D_12750 = _f32(h2[0])
                M_31 = _f32(min(D_12750, M_31))
                _136 = hmin[0]
                _pc = 62 if M_31 > _136 else 63
                continue
            case 62:  # <D.19396>
                len[0] = 1
                _pc = 63
                continue
            case 63:  # L.770
                _137 = hmin[0]
                _138 = parmtr_zmax[0]
                _pc = 64 if _137 >= _138 else 65
                continue
            case 64:  # <D.19399>
                _pc = 73
                continue
            case 65:  # L.771
                _139 = h1[0]
                _140 = parmtr_zmax[0]
                _141 = _139 > _140
                _142 = h2[0]
                _143 = parmtr_zmax[0]
                _144 = _142 > _143
                _145 = _141 | _144
                _pc = 66 if _145 != 0 else 67
                continue
            case 66:  # <D.19401>
                _ft_reduce(_state, h1, h2, angle, phi, iter)
                _pc = 67
                continue
            case 67:  # __label_000020
                return
            case 68:  # __label_000040
                _pc = 73
                continue
            case 69:  # __label_000042
                _pc = 73
                continue
            case 70:  # __label_000043
                _pc = 73
                continue
            case 71:  # __label_000044
                _pc = 73
                continue
            case 72:  # __label_000048
                _pc = 73
                continue
            case 73:  # __label_009900
                ierror[0] = 1
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_reduce(_state, h1, h2, angle, phi, iter):
    cnstns_deg = _state.view(246168, '<f4')
    parmtr_re = _state.view(245632, '<f4')
    parmtr_zmax = _state.view(245640, '<f4')
    angmax = _ZERO32
    cpath = _ZERO32
    czmax = _ZERO32
    gamma = _zeros(1, '<f4')
    sh = _zeros(1, '<f4')
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = h1[0]
                _2 = parmtr_zmax[0]
                _3 = _1 <= _2
                _4 = h2[0]
                _5 = parmtr_zmax[0]
                _6 = _4 <= _5
                _7 = _3 & _6
                _pc = 1 if _7 != 0 else 2
                continue
            case 1:  # <D.19407>
                return
            case 2:  # L.773
                _ft_findsh(_state, h1, sh, gamma)
                _8 = _ft_andex(_state, h1, sh, gamma)
                _9 = h1[0]
                _10 = parmtr_re[0]
                _11 = _9 + _10
                _12 = _11
                _13 = _8 * _12
                _14 = angle[0]
                _15 = cnstns_deg[0]
                _16 = _div(_14, _15)
                _17 = __builtin_sinf(_16)
                cpath = _f32(_13 * _17)
                _ft_findsh(_state, parmtr_zmax, sh, gamma)
                _18 = _ft_andex(_state, parmtr_zmax, sh, gamma)
                _19 = parmtr_re[0]
                _20 = parmtr_zmax[0]
                _21 = _19 + _20
                _22 = _21
                czmax = _f32(_18 * _22)
                _23 = _div(cpath, czmax)
                _24 = __builtin_asinf(_23)
                _25 = cnstns_deg[0]
                _26 = _24 * _25
                angmax = _f32(1.8e+2 - _26)
                _27 = h1[0]
                _28 = parmtr_zmax[0]
                _pc = 3 if _27 <= _28 else 4
                continue
            case 3:  # <D.19409>
                _pc = 5
                continue
            case 4:  # L.774
                _29 = parmtr_zmax[0]
                h1[0] = _29
                angle[0] = angmax
                _pc = 5
            case 5:  # __label_000120
                _30 = h2[0]
                _31 = parmtr_zmax[0]
                _pc = 6 if _30 <= _31 else 7
                continue
            case 6:  # <D.19411>
                _pc = -1
                continue
            case 7:  # L.775
                _32 = parmtr_zmax[0]
                h2[0] = _32
                phi[0] = angmax
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_andex(_state, h, sh, gamma):
    cnstns_bigexp = _state.view(246180, '<f4')
    D_19422 = _ZERO32
    hsh = _ZERO32
    __result_andex = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = sh[0]
                _pc = 1 if _1 == 0.0 else 2
                continue
            case 1:  # <D.19416>
                _pc = 7
                continue
            case 2:  # L.776
                _2 = h[0]
                _pc = 3 if _2 <= 0.0 else 4
                continue
            case 3:  # <D.19418>
                _pc = 7
                continue
            case 4:  # L.777
                _3 = h[0]
                _4 = sh[0]
                hsh = _f32(_div(_3, _4))
                _5 = cnstns_bigexp[0]
                _pc = 5 if hsh > _5 else 6
                continue
            case 5:  # <D.19420>
                _pc = 8
                continue
            case 6:  # L.778
                _6 = gamma[0]
                _7 = -hsh
                _8 = __builtin_expf(_7)
                _9 = _6 * _8
                _10 = _9 + 1.0e+0
                __result_andex = _f32(_10)
                D_19422 = _f32(__result_andex)
                return D_19422
            case 7:  # __label_000010
                _11 = gamma[0]
                _12 = _11 + 1.0e+0
                __result_andex = _f32(_12)
                D_19422 = _f32(__result_andex)
                return D_19422
            case 8:  # __label_000020
                __result_andex = _f32(1.0e+0)
                D_19422 = _f32(__result_andex)
                return D_19422
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_findsh(_state, h, sh, gamma):
    model_z = _state.view(231904, '<f4')
    model_rfndx = _state.view(232312, '<f4')
    parmtr_imod = _state.view(245648, '<i4')
    i1 = 0
    i2 = 0
    im = 0
    D_12892 = 0
    D_12895 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                D_12892 = _int(parmtr_imod[0])
                im = _int(2)
                _pc = 1
            case 1:  # <D.19425>
                D_12895 = _int(im > D_12892)
                _pc = 5 if D_12895 != 0 else 2
                continue
            case 2:  # <D.19426>
                i2 = _int(im)
                _1 = _int(im)
                _2 = _1 + -1
                _3 = model_z[_2]
                _4 = h[0]
                _pc = 3 if _3 >= _4 else 4
                continue
            case 3:  # <D.19427>
                _pc = 6
                continue
            case 4:  # L.779
                im = _int(im + 1)
                _pc = 1
                continue
            case 5:  # L.780
                i2 = _int(parmtr_imod[0])
                _pc = 6
            case 6:  # __label_000110
                i1 = _int(i2 + -1)
                _5 = _int(i2)
                _6 = _5 + -1
                _7 = model_rfndx[_6:]
                _8 = _int(i1)
                _9 = _8 + -1
                _10 = model_rfndx[_9:]
                _11 = _int(i2)
                _12 = _11 + -1
                _13 = model_z[_12:]
                _14 = _int(i1)
                _15 = _14 + -1
                _16 = model_z[_15:]
                _ft_scalht(_state, _16, _13, _10, _7, sh, gamma)
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_fndhmn(_state, h1, angle, h2, len, iter, hmin, phi, ierror):
    cnstns_deg = _state.view(246168, '<f4')
    cntrl_issgeo = _state.view(245624, '<i4')
    parmtr_re = _state.view(245632, '<f4')
    dh = _state.view(180340, '<f4')
    eta = _state.view(180344, '<f4')
    ch2 = _ZERO32
    cmin = _ZERO32
    cpath = _ZERO32
    ct1 = _ZERO32
    ct2 = _ZERO32
    ct3 = _ZERO32
    dc = _ZERO32
    gamma = _zeros(1, '<f4')
    ht = _ZERO32
    ht1 = _zeros(1, '<f4')
    ht2 = _zeros(1, '<f4')
    ht3 = _zeros(1, '<f4')
    n = 0
    sh = _zeros(1, '<f4')
    h_32 = _zeros(1, '<f4')
    h_33 = _zeros(1, '<f4')
    C_12978 = _array([0.0], '<f4')
    h_34 = _zeros(1, '<f4')
    h_35 = _zeros(1, '<f4')
    h_36 = _zeros(1, '<f4')
    h_37 = _zeros(1, '<f4')
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                n = _int(0)
                _ft_findsh(_state, h1, sh, gamma)
                _1 = h1[0]
                h_32[0] = _1
                _2 = parmtr_re[0]
                h_485_3 = h_32[0]
                _4 = _2 + h_485_3
                _5 = _4
                _6 = _ft_andex(_state, h_32, sh, gamma)
                _7 = _5 * _6
                _8 = angle[0]
                _9 = cnstns_deg[0]
                _10 = _div(_8, _9)
                _11 = __builtin_sinf(_10)
                cpath = _f32(_7 * _11)
                _ft_findsh(_state, h2, sh, gamma)
                _12 = h2[0]
                h_33[0] = _12
                _13 = parmtr_re[0]
                h_486_14 = h_33[0]
                _15 = _13 + h_486_14
                _16 = _15
                _17 = _ft_andex(_state, h_33, sh, gamma)
                ch2 = _f32(_16 * _17)
                _18 = _div(cpath, ch2)
                _19 = abs(_18)
                _pc = 1 if _19 > 1.0e+0 else 2
                continue
            case 1:  # <D.19429>
                _pc = 29
                continue
            case 2:  # L.782
                _20 = angle[0]
                _pc = 3 if _20 > 9.0e+1 else 4
                continue
            case 3:  # <D.19431>
                _pc = 5
                continue
            case 4:  # L.783
                len[0] = 0
                _21 = h1[0]
                hmin[0] = _21
                _pc = 26
                continue
            case 5:  # __label_000100
                _22 = h1[0]
                _23 = h2[0]
                _pc = 6 if _22 <= _23 else 7
                continue
            case 6:  # <D.19433>
                len[0] = 1
                _pc = 7
                continue
            case 7:  # L.784
                _24 = len[0]
                _pc = 8 if _24 == 1 else 9
                continue
            case 8:  # <D.19436>
                _pc = 10
                continue
            case 9:  # L.785
                len[0] = 0
                _25 = h2[0]
                hmin[0] = _25
                _pc = 26
                continue
            case 10:  # __label_000110
                _ft_findsh(_state, C_12978, sh, gamma)
                h_34[0] = 0.0
                _26 = parmtr_re[0]
                h_487_27 = h_34[0]
                _28 = _26 + h_487_27
                _29 = _28
                _30 = _ft_andex(_state, h_34, sh, gamma)
                cmin = _f32(_29 * _30)
                _31 = iter[0]
                _32 = _31 == 0
                _33 = cpath < cmin
                _34 = _32 & _33
                _pc = 11 if _34 != 0 else 12
                continue
            case 11:  # <D.19438>
                _pc = 22
                continue
            case 12:  # L.786
                _35 = h1[0]
                _36 = parmtr_re[0]
                _37 = _35 + _36
                _38 = _37
                _39 = angle[0]
                _40 = cnstns_deg[0]
                _41 = _div(_39, _40)
                _42 = __builtin_sinf(_41)
                _43 = _38 * _42
                _44 = parmtr_re[0]
                _45 = _43 - _44
                ht1[0] = _45
                _ft_findsh(_state, ht1, sh, gamma)
                ht1_488_46 = ht1[0]
                h_35[0] = ht1_488_46
                _47 = parmtr_re[0]
                h_489_48 = h_35[0]
                _49 = _47 + h_489_48
                _50 = _49
                _51 = _ft_andex(_state, h_35, sh, gamma)
                ct1 = _f32(_50 * _51)
                ht1_490_52 = ht1[0]
                dh_491_53 = dh[0]
                _54 = ht1_490_52 - dh_491_53
                ht2[0] = _54
                _ft_findsh(_state, ht2, sh, gamma)
                ht2_492_55 = ht2[0]
                h_36[0] = ht2_492_55
                _56 = parmtr_re[0]
                h_493_57 = h_36[0]
                _58 = _56 + h_493_57
                _59 = _58
                _60 = _ft_andex(_state, h_36, sh, gamma)
                ct2 = _f32(_59 * _60)
                n = _int(2)
                _pc = 13
            case 13:  # __label_000120
                _pc = 14 if ct2 == ct1 else 15
                continue
            case 14:  # <D.19440>
                _pc = 20
                continue
            case 15:  # L.787
                n = _int(n + 1)
                ht2_494_61 = ht2[0]
                ht1_495_62 = ht1[0]
                _63 = ht2_494_61 - ht1_495_62
                _64 = _63
                _65 = cpath - ct2
                _66 = _65
                _67 = _64 * _66
                _68 = ct2 - ct1
                _69 = _68
                _70 = _div(_67, _69)
                ht2_496_71 = ht2[0]
                _72 = _70 + ht2_496_71
                ht3[0] = _72
                _ft_findsh(_state, ht3, sh, gamma)
                ht3_497_73 = ht3[0]
                h_37[0] = ht3_497_73
                _74 = parmtr_re[0]
                h_498_75 = h_37[0]
                _76 = _74 + h_498_75
                _77 = _76
                _78 = _ft_andex(_state, h_37, sh, gamma)
                ct3 = _f32(_77 * _78)
                dc = _f32(cpath - ct3)
                _79 = cpath - ct3
                _80 = _79
                _81 = _div(_80, cpath)
                _82 = abs(_81)
                eta_499_83 = eta[0]
                _pc = 16 if _82 < eta_499_83 else 17
                continue
            case 16:  # <D.19442>
                _pc = 21
                continue
            case 17:  # L.788
                _pc = 18 if n > 15 else 19
                continue
            case 18:  # <D.19444>
                _pc = 30
                continue
            case 19:  # L.789
                ht2_500_84 = ht2[0]
                ht1[0] = ht2_500_84
                ct1 = _f32(ct2)
                ht3_501_85 = ht3[0]
                ht2[0] = ht3_501_85
                ct2 = _f32(ct3)
                _pc = 13
                continue
            case 20:  # __label_000125
                ht2_502_86 = ht2[0]
                ht3[0] = ht2_502_86
                _pc = 21
            case 21:  # __label_000130
                ht = _f32(ht3[0])
                hmin[0] = ht
                _pc = 26
                continue
            case 22:  # __label_000150
                _87 = cntrl_issgeo[0]
                _pc = 23 if _87 == 0 else 24
                continue
            case 23:  # <D.19446>
                _pc = 25
                continue
            case 24:  # L.790
                ierror[0] = -5
                return
            case 25:  # __label_000155
                h2[0] = 0.0
                hmin[0] = 0.0
                len[0] = 0
                ch2 = _f32(cmin)
                _pc = 26
            case 26:  # __label_000160
                _88 = _div(cpath, ch2)
                _89 = __builtin_asinf(_88)
                _90 = cnstns_deg[0]
                _91 = _89 * _90
                phi[0] = _91
                _92 = angle[0]
                _93 = _92 <= 9.0e+1
                _94 = len[0]
                _95 = _94 == 1
                _96 = _93 | _95
                _pc = 27 if _96 != 0 else 28
                continue
            case 27:  # <D.19448>
                _97 = phi[0]
                _98 = 1.8e+2 - _97
                phi[0] = _98
                _pc = 28
                continue
            case 28:  # L.791
                return
            case 29:  # __label_000020
                ierror[0] = 2
                return
            case 30:  # __label_000210
                dc = _f32(cpath - ct3)
                _pc = 31
            case 31:  # __label_000024
                _gfortran_stop_numeric(20, 0)
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_fdbeta(_state, h1, h2, betas, angle, phi, len, hmin, ierror):
    cnstns_deg = _state.view(246168, '<f4')
    parmtr_re = _state.view(245632, '<f4')
    betd = _state.view(180348, '<f4')
    itermx = _state.view(180356, '<i4')
    tolrnc = _state.view(180352, '<f4')
    angle1 = _ZERO64
    angle2 = _ZERO64
    anglep = _zeros(1, '<f4')
    angls1 = _zeros(1, '<f4')
    angls2 = _zeros(1, '<f4')
    bendng = _zeros(1, '<f4')
    beta = _ZERO64
    beta1 = _zeros(1, '<f4')
    beta2 = _zeros(1, '<f4')
    betap = _zeros(1, '<f4')
    dang = _ZERO32
    dbeta = _ZERO64
    dc = _ZERO32
    ha = _zeros(1, '<f4')
    hb = _zeros(1, '<f4')
    hming = _ZERO32
    iamtb = _zeros(1, '<i4')
    iflag = 0
    iorder = 0
    iter = _zeros(1, '<i4')
    ra = _ZERO64
    range = _zeros(1, '<f4')
    rb = _ZERO64
    sg = _ZERO64
    temp = _ZERO32
    D_13067 = _ZERO64
    D_13068 = _ZERO64
    D_13069 = _ZERO64
    D_13070 = _ZERO64
    D_13071 = _ZERO64
    D_13072 = _ZERO64
    D_13073 = _ZERO64
    D_13074 = _ZERO64
    D_13075 = _ZERO64
    D_13076 = _ZERO64
    D_13079 = _ZERO64
    D_13080 = _ZERO64
    D_13081 = _ZERO64
    D_13082 = _ZERO64
    D_13083 = _ZERO64
    D_13084 = _ZERO64
    D_13085 = _ZERO64
    D_13086 = _ZERO64
    D_13087 = _ZERO64
    D_13088 = _ZERO64
    C_13091 = _array([9.0e+1], '<f4')
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = betas[0]
                beta = _f64(_f64(_1))
                iflag = _int(0)
                _2 = h1[0]
                _3 = h2[0]
                _pc = 1 if _2 > _3 else 2
                continue
            case 1:  # <D.19453>
                _pc = 3
                continue
            case 2:  # L.792
                iorder = _int(1)
                _4 = h1[0]
                ha[0] = _4
                _5 = h2[0]
                hb[0] = _5
                _pc = 4
                continue
            case 3:  # __label_000100
                iorder = _int(-1)
                _6 = h2[0]
                ha[0] = _6
                _7 = h1[0]
                hb[0] = _7
                _pc = 4
            case 4:  # __label_000120
                iamtb[0] = 2
                _pc = 5
            case 5:  # __label_000024
                iter[0] = 0
                _8 = parmtr_re[0]
                ha_503_9 = ha[0]
                _10 = _8 + ha_503_9
                ra = _f64(_f64(_10))
                _11 = parmtr_re[0]
                hb_504_12 = hb[0]
                _13 = _11 + hb_504_12
                rb = _f64(_f64(_13))
                D_13067 = _f64(ra)
                D_13068 = _f64(D_13067 * D_13067)
                D_13069 = _f64(rb)
                D_13070 = _f64(D_13069 * D_13069)
                _14 = D_13068 + D_13070
                _15 = ra * 2.0e+0
                _16 = rb * _15
                _17 = cnstns_deg[0]
                _18 = _f64(_17)
                _19 = _div(beta, _18)
                _20 = __builtin_cos(_19)
                _21 = _16 * _20
                _22 = _14 - _21
                sg = _f64(__builtin_sqrt(_22))
                D_13071 = _f64(ra)
                D_13072 = _f64(D_13071 * D_13071)
                D_13073 = _f64(sg)
                D_13074 = _f64(D_13073 * D_13073)
                D_13075 = _f64(rb)
                D_13076 = _f64(D_13075 * D_13075)
                _23 = D_13072 + D_13074
                _24 = _23 - D_13076
                _25 = _24
                _26 = ra * 2.0e+0
                _27 = sg * _26
                _28 = _27
                _29 = _div(_25, _28)
                _30 = __builtin_acos(_29)
                _31 = cnstns_deg[0]
                _32 = _f64(_31)
                _33 = _30 * _32
                angle1 = _f64(1.8e+2 - _33)
                ha_505_34 = ha[0]
                hmin[0] = ha_505_34
                _pc = 6 if angle1 > 9.0e+1 else 7
                continue
            case 6:  # <D.19455>
                _35 = cnstns_deg[0]
                _36 = _f64(_35)
                _37 = _div(angle1, _36)
                _38 = __builtin_sin(_37)
                _39 = ra * _38
                _40 = parmtr_re[0]
                _41 = _f64(_40)
                _42 = _39 - _41
                _43 = _f32(_42)
                hmin[0] = _43
                _pc = 7
                continue
            case 7:  # L.793
                hming = _f32(hmin[0])
                _44 = _f32(angle1)
                angls1[0] = _44
                _ft_fndhmn(_state, ha, angls1, hb, len, iter, hmin, phi, ierror)
                len[0] = 0
                _45 = hmin[0]
                ha_506_46 = ha[0]
                _pc = 8 if _45 < ha_506_46 else 9
                continue
            case 8:  # <D.19458>
                len[0] = 1
                _pc = 9
                continue
            case 9:  # L.794
                _ft_rfpath(_state, ha, hb, angls1, phi, len, hmin, iamtb, beta1, range, bendng)
                D_13079 = _f64(ra)
                D_13080 = _f64(D_13079 * D_13079)
                D_13081 = _f64(rb)
                D_13082 = _f64(D_13081 * D_13081)
                _47 = D_13080 + D_13082
                _48 = ra * 2.0e+0
                _49 = rb * _48
                betd_507_50 = betd[0]
                _51 = _f64(betd_507_50)
                _52 = beta + _51
                _53 = _52
                _54 = cnstns_deg[0]
                _55 = _f64(_54)
                _56 = _div(_53, _55)
                _57 = __builtin_cos(_56)
                _58 = _49 * _57
                _59 = _47 - _58
                sg = _f64(__builtin_sqrt(_59))
                D_13083 = _f64(ra)
                D_13084 = _f64(D_13083 * D_13083)
                D_13085 = _f64(sg)
                D_13086 = _f64(D_13085 * D_13085)
                D_13087 = _f64(rb)
                D_13088 = _f64(D_13087 * D_13087)
                _60 = D_13084 + D_13086
                _61 = _60 - D_13088
                _62 = _61
                _63 = ra * 2.0e+0
                _64 = sg * _63
                _65 = _64
                _66 = _div(_62, _65)
                _67 = __builtin_acos(_66)
                _68 = cnstns_deg[0]
                _69 = _f64(_68)
                _70 = _67 * _69
                _71 = 1.8e+2 - _70
                _72 = _f32(_71)
                anglep[0] = _72
                anglep_508_73 = anglep[0]
                _74 = _f64(anglep_508_73)
                _75 = angle1 - _74
                dang = _f32(_f32(_75))
                _76 = hmin[0]
                _pc = 10 if _76 >= 0.0 else 11
                continue
            case 10:  # <D.19461>
                _pc = 12
                continue
            case 11:  # L.795
                iflag = _int(1)
                hmin[0] = 0.0
                _ft_fndhmn(_state, hmin, C_13091, ha, len, iter, hmin, angls1, ierror)
                _pc = 12
            case 12:  # __label_000310
                iter[0] = 1
                len[0] = 0
                _pc = 13 if angle1 > 9.0e+1 else 14
                continue
            case 13:  # <D.19463>
                len[0] = 1
                _pc = 14
                continue
            case 14:  # L.796
                _ft_fndhmn(_state, ha, angls1, hb, len, iter, hmin, phi, ierror)
                len[0] = 0
                _77 = hmin[0]
                ha_509_78 = ha[0]
                _pc = 15 if _77 < ha_509_78 else 16
                continue
            case 15:  # <D.19466>
                len[0] = 1
                _pc = 16
                continue
            case 16:  # L.797
                _ft_rfpath(_state, ha, hb, angls1, phi, len, hmin, iamtb, beta1, range, bendng)
                beta1_510_79 = beta1[0]
                _80 = _f64(beta1_510_79)
                dbeta = _f64(beta - _80)
                _pc = 17
            case 17:  # __label_000026
                _81 = iflag == 1
                beta1_511_82 = beta1[0]
                _83 = _f64(beta1_511_82)
                _84 = beta > _83
                _85 = _81 & _84
                _pc = 18 if _85 != 0 else 19
                continue
            case 18:  # <D.19469>
                _pc = 43
                continue
            case 19:  # __label_000320
                _86 = _f64(dang)
                _87 = angle1 - _86
                _88 = _f32(_87)
                anglep[0] = _88
                len[0] = 0
                anglep_512_89 = anglep[0]
                _pc = 20 if anglep_512_89 > 9.0e+1 else 21
                continue
            case 20:  # <D.19471>
                len[0] = 1
                _pc = 21
                continue
            case 21:  # L.799
                _ft_fndhmn(_state, ha, anglep, hb, len, iter, hmin, phi, ierror)
                len[0] = 0
                _90 = hmin[0]
                ha_513_91 = ha[0]
                _pc = 22 if _90 < ha_513_91 else 23
                continue
            case 22:  # <D.19474>
                len[0] = 1
                _pc = 23
                continue
            case 23:  # L.800
                _ft_rfpath(_state, ha, hb, anglep, phi, len, hmin, iamtb, betap, range, bendng)
                beta1_514_92 = beta1[0]
                betap_515_93 = betap[0]
                _94 = beta1_514_92 - betap_515_93
                _95 = abs(_94)
                tolrnc_516_96 = tolrnc[0]
                _pc = 24 if _95 < tolrnc_516_96 else 25
                continue
            case 24:  # <D.19477>
                _pc = 36
                continue
            case 25:  # L.801
                iter_517_97 = iter[0]
                _98 = iter_517_97 + 1
                iter[0] = _98
                betap_518_99 = betap[0]
                beta1_519_100 = beta1[0]
                dc = _f32(betap_518_99 - beta1_519_100)
                anglep_520_101 = anglep[0]
                _102 = _f64(anglep_520_101)
                _103 = angle1 - _102
                _104 = _103
                beta1_521_105 = beta1[0]
                _106 = _f64(beta1_521_105)
                _107 = beta - _106
                _108 = _107
                _109 = _104 * _108
                beta1_522_110 = beta1[0]
                betap_523_111 = betap[0]
                _112 = beta1_522_110 - betap_523_111
                _113 = _112
                _114 = _f64(_113)
                _115 = _div(_109, _114)
                angle2 = _f64(angle1 + _115)
                len[0] = 0
                _pc = 26 if angle2 > 9.0e+1 else 27
                continue
            case 26:  # <D.19479>
                len[0] = 1
                _pc = 27
                continue
            case 27:  # L.802
                _116 = _f32(angle2)
                angls2[0] = _116
                _ft_fndhmn(_state, ha, angls2, hb, len, iter, hmin, phi, ierror)
                len[0] = 0
                _117 = hmin[0]
                ha_524_118 = ha[0]
                _pc = 28 if _117 < ha_524_118 else 29
                continue
            case 28:  # <D.19482>
                len[0] = 1
                _pc = 29
                continue
            case 29:  # L.803
                _ft_rfpath(_state, ha, hb, angls2, phi, len, hmin, iamtb, beta2, range, bendng)
                beta2_525_119 = beta2[0]
                _120 = _f64(beta2_525_119)
                dbeta = _f64(beta - _120)
                beta2_526_121 = beta2[0]
                _122 = _f64(beta2_526_121)
                _123 = beta > _122
                _124 = hmin[0]
                _125 = _124 < 0.0
                _126 = _123 & _125
                _pc = 30 if _126 != 0 else 31
                continue
            case 30:  # <D.19485>
                _pc = 43
                continue
            case 31:  # L.804
                angle1 = _f64(angle2)
                _127 = _f32(angle1)
                angls1[0] = _127
                beta2_527_128 = beta2[0]
                beta1[0] = beta2_527_128
                beta2_528_129 = beta2[0]
                _130 = _f64(beta2_528_129)
                _131 = beta - _130
                _132 = abs(_131)
                tolrnc_529_133 = tolrnc[0]
                _134 = _f64(tolrnc_529_133)
                _pc = 32 if _132 < _134 else 33
                continue
            case 32:  # <D.19487>
                _pc = 37
                continue
            case 33:  # L.805
                iter_530_135 = iter[0]
                itermx_531_136 = itermx[0]
                _pc = 34 if iter_530_135 > itermx_531_136 else 35
                continue
            case 34:  # <D.19489>
                _pc = 44
                continue
            case 35:  # L.806
                _pc = 19
                continue
            case 36:  # __label_000330
                anglep_532_137 = anglep[0]
                angle2 = _f64(_f64(anglep_532_137))
                _138 = _f32(angle2)
                angls2[0] = _138
                betap_533_139 = betap[0]
                beta = _f64(_f64(betap_533_139))
                _pc = 37
            case 37:  # __label_000340
                _140 = hmin[0]
                _pc = 38 if _140 < 0.0 else 39
                continue
            case 38:  # <D.19491>
                _pc = 43
                continue
            case 39:  # L.807
                _141 = _f32(angle2)
                angle[0] = _141
                beta2_534_142 = beta2[0]
                beta = _f64(_f64(beta2_534_142))
                _pc = 40 if iorder == 1 else 41
                continue
            case 40:  # <D.19493>
                _pc = 42
                continue
            case 41:  # L.808
                temp = _f32(phi[0])
                _143 = angle[0]
                phi[0] = _143
                angle[0] = temp
                _pc = 42
            case 42:  # __label_000350
                _144 = _f32(beta)
                betas[0] = _144
                return
            case 43:  # __label_000045
                _pc = 44
                continue
            case 44:  # __label_009900
                ierror[0] = 1
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_layer(_state, j, sinai, cosai, cpath, sh, gamma, iamt, s, bend):
    cnstns_gcair = _state.view(246172, '<f4')
    cnstns_bigexp = _state.view(246180, '<f4')
    cntrl_kmax = _state.view(245600, '<i4')
    parmtr_re = _state.view(245632, '<f4')
    parmtr_deltas = _state.view(245636, '<f4')
    rfrpth_zp = _state.view(246784, '<f4')
    rfrpth_pp = _state.view(246924, '<f4')
    rfrpth_tp = _state.view(247064, '<f4')
    rfrpth_sp = _state.view(247344, '<f4')
    rfrpth_ppsum = _state.view(247484, '<f4')
    rfrpth_tpsum = _state.view(247624, '<f4')
    rfrpth_rhopsm = _state.view(247764, '<f4')
    rfrpth_denp = _state.view(247904, '<f4')
    rfrpth_amtp = _state.view(256724, '<f4')
    epsiln = _state.view(180360, '<f4')
    cosai1 = _ZERO32
    cosai2 = _ZERO32
    cosai3 = _ZERO32
    d21 = _ZERO32
    d31 = _ZERO32
    d32 = _ZERO32
    dbend = _ZERO32
    dbndx1 = _ZERO32
    dbndx2 = _ZERO32
    dbndx3 = _ZERO32
    dena = _zeros(63, '<f4')
    denb = _zeros(63, '<f4')
    dh = _ZERO32
    dhhp = _ZERO32
    dhmin = _ZERO32
    dhrh = _ZERO32
    ds = _ZERO32
    dsdx1 = _ZERO32
    dsdx2 = _ZERO32
    dsdx3 = _ZERO32
    dsdz = _ZERO32
    dx = _ZERO32
    dz = _ZERO32
    h1 = _zeros(1, '<f4')
    h2 = _zeros(1, '<f4')
    h3 = _zeros(1, '<f4')
    h3z1 = _ZERO32
    hden = _zeros(63, '<f4')
    hp = _ZERO32
    hrho = _ZERO32
    k = 0
    n = 0
    pa = _ZERO32
    pb = _ZERO32
    r1 = _ZERO32
    r2 = _ZERO32
    r3 = _ZERO32
    ratio1 = _ZERO32
    ratio2 = _ZERO32
    ratio3 = _ZERO32
    rhoa = _ZERO32
    rhob = _ZERO32
    sinai1 = _ZERO32
    sinai2 = _ZERO32
    sinai3 = _ZERO32
    ta = _ZERO32
    tb = _ZERO32
    w1 = _ZERO32
    w2 = _ZERO32
    w3 = _ZERO32
    x1 = _ZERO32
    x2 = _ZERO32
    x3 = _ZERO32
    y1 = _ZERO32
    y3 = _ZERO32
    z1 = _ZERO32
    z2 = _ZERO32
    D_13248 = _ZERO32
    D_13249 = _ZERO32
    D_13250 = _ZERO32
    D_13251 = _ZERO32
    D_13252 = _ZERO32
    D_13253 = _ZERO32
    D_13259 = _ZERO32
    D_13260 = _ZERO32
    D_13266 = 0
    D_13269 = 0
    D_13279 = _ZERO32
    D_13280 = _ZERO32
    D_13282 = _ZERO32
    D_13283 = _ZERO32
    D_13284 = _ZERO32
    D_13285 = _ZERO32
    D_13288 = _ZERO32
    D_13289 = _ZERO32
    D_13290 = _ZERO32
    D_13291 = _ZERO32
    D_13292 = _ZERO32
    D_13300 = 0
    D_13303 = 0
    D_13309 = 0
    D_13312 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                n = _int(0)
                _1 = j[0]
                _2 = _int(_1)
                _3 = _2 + -1
                z1 = _f32(rfrpth_zp[_3])
                _4 = j[0]
                _5 = _4 + 1
                _6 = _int(_5)
                _7 = _6 + -1
                z2 = _f32(rfrpth_zp[_7])
                h1[0] = z1
                _8 = parmtr_re[0]
                h1_535_9 = h1[0]
                r1 = _f32(_8 + h1_535_9)
                D_13248 = _f32(parmtr_deltas[0])
                D_13249 = _f32(D_13248 * D_13248)
                _10 = r1 * 2.0e+0
                _11 = _10
                dhmin = _f32(_div(D_13249, _11))
                sinai1 = _f32(sinai[0])
                cosai1 = _f32(cosai[0])
                D_13250 = _f32(cosai1)
                D_13251 = _f32(D_13250 * D_13250)
                D_13252 = _f32(cosai1)
                D_13253 = _f32(cosai1)
                _12 = _div(D_13251, 2.0e+0)
                _13 = __builtin_powif(D_13252, 4)
                _14 = _div(_13, 8.0e+0)
                _15 = _12 + _14
                _16 = __builtin_powif(D_13253, 6)
                _17 = _16 * 3.0e+0
                _18 = _div(_17, 4.8e+1)
                y1 = _f32(_15 + _18)
                y3 = _f32(0.0)
                _19 = r1 * cosai1
                x1 = _f32(-_19)
                _20 = _ft_radref(_state, h1, sh, gamma)
                ratio1 = _f32(_div(r1, _20))
                D_13259 = _f32(sinai1)
                D_13260 = _f32(D_13259 * D_13259)
                _21 = ratio1 * D_13260
                _22 = 1.0e+0 - _21
                _23 = _22
                dsdx1 = _f32(_div(1.0e+0, _23))
                _24 = dsdx1 * sinai1
                _25 = ratio1 * _24
                dbndx1 = _f32(_div(_25, r1))
                s[0] = 0.0
                bend[0] = 0.0
                _26 = iamt[0]
                _pc = 1 if _26 == 2 else 2
                continue
            case 1:  # <D.19498>
                _pc = 15
                continue
            case 2:  # L.809
                _27 = j[0]
                _28 = _int(_27)
                _29 = _28 + -1
                pa = _f32(rfrpth_pp[_29])
                _30 = j[0]
                _31 = _30 + 1
                _32 = _int(_31)
                _33 = _32 + -1
                pb = _f32(rfrpth_pp[_33])
                _34 = j[0]
                _35 = _int(_34)
                _36 = _35 + -1
                ta = _f32(rfrpth_tp[_36])
                _37 = j[0]
                _38 = _37 + 1
                _39 = _int(_38)
                _40 = _39 + -1
                tb = _f32(rfrpth_tp[_40])
                _41 = cnstns_gcair[0]
                _42 = ta * _41
                _43 = _42
                rhoa = _f32(_div(pa, _43))
                _44 = cnstns_gcair[0]
                _45 = tb * _44
                _46 = _45
                rhob = _f32(_div(pb, _46))
                _47 = j[0]
                _48 = _47 + 1
                _49 = _int(_48)
                _50 = _49 + -1
                _51 = rfrpth_zp[_50]
                _52 = j[0]
                _53 = _int(_52)
                _54 = _53 + -1
                _55 = rfrpth_zp[_54]
                dz = _f32(_51 - _55)
                _56 = _div(pb, pa)
                _57 = __builtin_logf(_56)
                _58 = _div(dz, _57)
                hp = _f32(-_58)
                _59 = _div(rhob, rhoa)
                _60 = _59 - 1.0e+0
                _61 = abs(_60)
                epsiln_536_62 = epsiln[0]
                _pc = 3 if _61 < epsiln_536_62 else 4
                continue
            case 3:  # <D.19500>
                _pc = 5
                continue
            case 4:  # L.810
                _63 = _div(rhob, rhoa)
                _64 = __builtin_logf(_63)
                _65 = _div(dz, _64)
                hrho = _f32(-_65)
                _pc = 6
                continue
            case 5:  # __label_000090
                hrho = _f32(1.00000001504746621987668885504e+30)
                _pc = 6
            case 6:  # __label_000095
                D_13266 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 7
            case 7:  # <D.19502>
                D_13269 = _int(k > D_13266)
                _pc = 15 if D_13269 != 0 else 8
                continue
            case 8:  # <D.19503>
                _66 = j[0]
                _67 = _int(_66)
                _68 = _67 * 63
                _69 = _int(k)
                _70 = _68 + _69
                _71 = _70 + -64
                _72 = _int(k)
                _73 = _72 + -1
                _74 = rfrpth_denp[_71]
                dena[_73] = _74
                _75 = j[0]
                _76 = _75 + 1
                _77 = _int(_76)
                _78 = _77 * 63
                _79 = _int(k)
                _80 = _78 + _79
                _81 = _80 + -64
                _82 = _int(k)
                _83 = _82 + -1
                _84 = rfrpth_denp[_81]
                denb[_83] = _84
                _85 = _int(k)
                _86 = _85 + -1
                _87 = dena[_86]
                _88 = _87 <= 0.0
                _89 = _int(k)
                _90 = _89 + -1
                _91 = denb[_90]
                _92 = _91 <= 0.0
                _93 = _88 | _92
                _pc = 9 if _93 != 0 else 10
                continue
            case 9:  # <D.19504>
                _pc = 13
                continue
            case 10:  # L.813
                _94 = _int(k)
                _95 = _94 + -1
                _96 = dena[_95]
                _97 = _int(k)
                _98 = _97 + -1
                _99 = denb[_98]
                _100 = _div(_96, _99)
                _101 = 1.0e+0 - _100
                _102 = abs(_101)
                epsiln_537_103 = epsiln[0]
                _pc = 11 if _102 <= epsiln_537_103 else 12
                continue
            case 11:  # <D.19506>
                _pc = 13
                continue
            case 12:  # L.814
                _104 = _int(k)
                _105 = _104 + -1
                _106 = denb[_105]
                _107 = _int(k)
                _108 = _107 + -1
                _109 = dena[_108]
                _110 = _div(_106, _109)
                _111 = __builtin_logf(_110)
                _112 = _div(dz, _111)
                _113 = _int(k)
                _114 = _113 + -1
                _115 = -_112
                hden[_114] = _115
                _pc = 14
                continue
            case 13:  # __label_000100
                _116 = _int(k)
                _117 = _116 + -1
                hden[_117] = 0.0
                _pc = 14
            case 14:  # L.811
                k = _int(k + 1)
                _pc = 7
                continue
            case 15:  # __label_000115
                n = _int(n + 1)
                _118 = parmtr_deltas[0]
                _119 = cosai1 * _118
                dh = _f32(-_119)
                _pc = 16 if dh < dhmin else 17
                continue
            case 16:  # <D.19508>
                dh = _f32(dhmin)
                _pc = 17
                continue
            case 17:  # L.815
                h1_538_120 = h1[0]
                _121 = dh + h1_538_120
                h3[0] = _121
                h3_539_122 = h3[0]
                _pc = 18 if z2 < h3_539_122 else 19
                continue
            case 18:  # <D.19511>
                h3[0] = z2
                _pc = 19
                continue
            case 19:  # L.816
                h3_540_123 = h3[0]
                h1_541_124 = h1[0]
                dh = _f32(h3_540_123 - h1_541_124)
                _125 = parmtr_re[0]
                h3_542_126 = h3[0]
                r3 = _f32(_125 + h3_542_126)
                _127 = _div(dh, 2.0e+0)
                h1_543_128 = h1[0]
                _129 = _127 + h1_543_128
                h2[0] = _129
                _130 = parmtr_re[0]
                h2_544_131 = h2[0]
                r2 = _f32(_130 + h2_544_131)
                _132 = cpath[0]
                _133 = _ft_andex(_state, h2, sh, gamma)
                _134 = r2 * _133
                _135 = _134
                sinai2 = _f32(_div(_132, _135))
                _136 = cpath[0]
                _137 = _ft_andex(_state, h3, sh, gamma)
                _138 = r3 * _137
                _139 = _138
                sinai3 = _f32(_div(_136, _139))
                _140 = _ft_radref(_state, h2, sh, gamma)
                ratio2 = _f32(_div(r2, _140))
                _141 = _ft_radref(_state, h3, sh, gamma)
                ratio3 = _f32(_div(r3, _141))
                _142 = 1.0e+0 - sinai2
                _143 = _142
                epsiln_545_144 = epsiln[0]
                _pc = 20 if _143 > epsiln_545_144 else 21
                continue
            case 20:  # <D.19514>
                _pc = 22
                continue
            case 21:  # L.817
                _145 = 1.0e+0 - ratio1
                _146 = _145
                _147 = sinai1 * _146
                _148 = _div(_147, r1)
                _149 = sinai2 * 4.0e+0
                _150 = 1.0e+0 - ratio2
                _151 = _150
                _152 = _149 * _151
                _153 = _div(_152, r2)
                _154 = _148 + _153
                _155 = 1.0e+0 - ratio3
                _156 = _155
                _157 = sinai3 * _156
                _158 = _div(_157, r3)
                _159 = _154 + _158
                _160 = _159
                _161 = dh * _160
                _162 = _div(_161, 6.0e+0)
                y3 = _f32(y1 + _162)
                D_13279 = _f32(y3)
                D_13280 = _f32(D_13279 * D_13279)
                _163 = y3 * 2.0e+0
                _164 = _163 - D_13280
                _165 = __builtin_sqrtf(_164)
                cosai3 = _f32(-_165)
                _166 = r3 * cosai3
                x3 = _f32(-_166)
                dx = _f32(x3 - x1)
                w1 = _f32(dx * 5.0e-1)
                w2 = _f32(0.0)
                w3 = _f32(dx * 5.0e-1)
                _pc = 26
                continue
            case 22:  # __label_000116
                D_13282 = _f32(sinai2)
                D_13283 = _f32(D_13282 * D_13282)
                _167 = 1.0e+0 - D_13283
                _168 = __builtin_sqrtf(_167)
                cosai2 = _f32(-_168)
                D_13284 = _f32(sinai3)
                D_13285 = _f32(D_13284 * D_13284)
                _169 = 1.0e+0 - D_13285
                _170 = __builtin_sqrtf(_169)
                cosai3 = _f32(-_170)
                _171 = r2 * cosai2
                x2 = _f32(-_171)
                _172 = r3 * cosai3
                x3 = _f32(-_172)
                d31 = _f32(x3 - x1)
                d32 = _f32(x3 - x2)
                d21 = _f32(x2 - x1)
                _173 = d32 == 0.0
                _174 = d21 == 0.0
                _175 = _173 | _174
                _pc = 23 if _175 != 0 else 24
                continue
            case 23:  # <D.19516>
                _pc = 25
                continue
            case 24:  # L.818
                _176 = _div(d32, d21)
                _177 = 2.0e+0 - _176
                _178 = _177
                _179 = d31 * _178
                w1 = _f32(_div(_179, 6.0e+0))
                D_13288 = _f32(d31)
                _180 = __builtin_powif(D_13288, 3)
                _181 = d32 * d21
                _182 = _181 * 6.0e+0
                _183 = _182
                w2 = _f32(_div(_180, _183))
                _184 = _div(d21, d32)
                _185 = 2.0e+0 - _184
                _186 = _185
                _187 = d31 * _186
                w3 = _f32(_div(_187, 6.0e+0))
                _pc = 26
                continue
            case 25:  # __label_000117
                w1 = _f32(d31 * 5.0e-1)
                w2 = _f32(0.0)
                w3 = _f32(d31 * 5.0e-1)
                _pc = 26
            case 26:  # __label_000118
                D_13289 = _f32(sinai2)
                D_13290 = _f32(D_13289 * D_13289)
                _188 = ratio2 * D_13290
                _189 = 1.0e+0 - _188
                _190 = _189
                dsdx2 = _f32(_div(1.0e+0, _190))
                D_13291 = _f32(sinai3)
                D_13292 = _f32(D_13291 * D_13291)
                _191 = ratio3 * D_13292
                _192 = 1.0e+0 - _191
                _193 = _192
                dsdx3 = _f32(_div(1.0e+0, _193))
                _194 = dsdx2 * sinai2
                _195 = ratio2 * _194
                dbndx2 = _f32(_div(_195, r2))
                _196 = dsdx3 * sinai3
                _197 = ratio3 * _196
                dbndx3 = _f32(_div(_197, r3))
                _198 = w1 * dsdx1
                _199 = w2 * dsdx2
                _200 = _198 + _199
                _201 = w3 * dsdx3
                ds = _f32(_200 + _201)
                _202 = s[0]
                _203 = ds + _202
                s[0] = _203
                _204 = w1 * dbndx1
                _205 = w2 * dbndx2
                _206 = _204 + _205
                _207 = w3 * dbndx3
                dbend = _f32(_206 + _207)
                _208 = bend[0]
                _209 = dbend + _208
                bend[0] = _209
                _210 = iamt[0]
                _pc = 27 if _210 == 2 else 28
                continue
            case 27:  # <D.19518>
                _pc = 54
                continue
            case 28:  # L.819
                dsdz = _f32(_div(ds, dh))
                dhhp = _f32(_div(dh, hp))
                _211 = cnstns_bigexp[0]
                _pc = 29 if dhhp <= _211 else 30
                continue
            case 29:  # <D.19520>
                _212 = -dhhp
                _213 = __builtin_expf(_212)
                pb = _f32(pa * _213)
                _pc = 31
                continue
            case 30:  # <D.19521>
                pb = _f32(0.0)
                _pc = 31
            case 31:  # L.820
                dhrh = _f32(_div(dh, hrho))
                _214 = cnstns_bigexp[0]
                _pc = 32 if dhrh <= _214 else 33
                continue
            case 32:  # <D.19523>
                _215 = -dhrh
                _216 = __builtin_expf(_215)
                rhob = _f32(rhoa * _216)
                _pc = 34
                continue
            case 33:  # <D.19524>
                rhob = _f32(0.0)
                _pc = 34
            case 34:  # L.821
                _217 = _div(dh, hrho)
                _218 = _217
                epsiln_546_219 = epsiln[0]
                _pc = 35 if _218 < epsiln_546_219 else 36
                continue
            case 35:  # <D.19526>
                _pc = 37
                continue
            case 36:  # L.822
                _220 = j[0]
                _221 = _int(_220)
                _222 = _221 + -1
                _223 = rfrpth_ppsum[_222]
                _224 = _div(hp, hrho)
                _225 = _224 + 1.0e+0
                _226 = _225
                _227 = _div(hp, _226)
                _228 = _227
                _229 = dsdz * _228
                _230 = pa * rhoa
                _231 = pb * rhob
                _232 = _230 - _231
                _233 = _232
                _234 = _229 * _233
                _235 = j[0]
                _236 = _int(_235)
                _237 = _236 + -1
                _238 = _223 + _234
                rfrpth_ppsum[_237] = _238
                _239 = j[0]
                _240 = _int(_239)
                _241 = _240 + -1
                _242 = rfrpth_tpsum[_241]
                _243 = dsdz * hp
                _244 = pa - pb
                _245 = _244
                _246 = _243 * _245
                _247 = cnstns_gcair[0]
                _248 = _div(_246, _247)
                _249 = j[0]
                _250 = _int(_249)
                _251 = _250 + -1
                _252 = _242 + _248
                rfrpth_tpsum[_251] = _252
                _253 = j[0]
                _254 = _int(_253)
                _255 = _254 + -1
                _256 = rfrpth_rhopsm[_255]
                _257 = dsdz * hrho
                _258 = rhoa - rhob
                _259 = _258
                _260 = _257 * _259
                _261 = j[0]
                _262 = _int(_261)
                _263 = _262 + -1
                _264 = _256 + _260
                rfrpth_rhopsm[_263] = _264
                _pc = 38
                continue
            case 37:  # __label_000120
                _265 = j[0]
                _266 = _int(_265)
                _267 = _266 + -1
                _268 = rfrpth_ppsum[_267]
                _269 = ds * 5.0e-1
                _270 = pa * rhoa
                _271 = pb * rhob
                _272 = _270 + _271
                _273 = _272
                _274 = _269 * _273
                _275 = j[0]
                _276 = _int(_275)
                _277 = _276 + -1
                _278 = _268 + _274
                rfrpth_ppsum[_277] = _278
                _279 = j[0]
                _280 = _int(_279)
                _281 = _280 + -1
                _282 = rfrpth_tpsum[_281]
                _283 = ds * 5.0e-1
                _284 = pa + pb
                _285 = _284
                _286 = _283 * _285
                _287 = cnstns_gcair[0]
                _288 = _div(_286, _287)
                _289 = j[0]
                _290 = _int(_289)
                _291 = _290 + -1
                _292 = _282 + _288
                rfrpth_tpsum[_291] = _292
                _293 = j[0]
                _294 = _int(_293)
                _295 = _294 + -1
                _296 = rfrpth_rhopsm[_295]
                _297 = ds * 5.0e-1
                _298 = rhoa + rhob
                _299 = _298
                _300 = _297 * _299
                _301 = j[0]
                _302 = _int(_301)
                _303 = _302 + -1
                _304 = _296 + _300
                rfrpth_rhopsm[_303] = _304
                _pc = 38
            case 38:  # __label_000125
                D_13300 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 39
            case 39:  # <D.19528>
                D_13303 = _int(k > D_13300)
                _pc = 50 if D_13303 != 0 else 40
                continue
            case 40:  # <D.19529>
                _305 = _int(k)
                _306 = _305 + -1
                _307 = hden[_306]
                _pc = 41 if _307 == 0.0 else 42
                continue
            case 41:  # <D.19530>
                _pc = 48
                continue
            case 42:  # L.825
                _308 = _int(k)
                _309 = _308 + -1
                _310 = hden[_309]
                _311 = _div(dh, _310)
                _312 = _311
                epsiln_547_313 = epsiln[0]
                _pc = 43 if _312 < epsiln_547_313 else 44
                continue
            case 43:  # <D.19532>
                _pc = 48
                continue
            case 44:  # L.826
                h3_548_314 = h3[0]
                _315 = h3_548_314 - z1
                _316 = _315
                _317 = _int(k)
                _318 = _317 + -1
                _319 = hden[_318]
                h3z1 = _f32(_div(_316, _319))
                _320 = cnstns_bigexp[0]
                _pc = 45 if h3z1 <= _320 else 46
                continue
            case 45:  # <D.19534>
                _321 = j[0]
                _322 = _int(_321)
                _323 = _322 * 63
                _324 = _int(k)
                _325 = _323 + _324
                _326 = _325 + -64
                _327 = rfrpth_denp[_326]
                _328 = -h3z1
                _329 = __builtin_expf(_328)
                _330 = _int(k)
                _331 = _330 + -1
                _332 = _327 * _329
                denb[_331] = _332
                _pc = 47
                continue
            case 46:  # <D.19535>
                _333 = _int(k)
                _334 = _333 + -1
                denb[_334] = 0.0
                _pc = 47
            case 47:  # L.827
                _335 = j[0]
                _336 = _int(_335)
                _337 = _336 * 63
                _338 = _int(k)
                _339 = _337 + _338
                _340 = _339 + -64
                _341 = rfrpth_amtp[_340]
                _342 = _int(k)
                _343 = _342 + -1
                _344 = hden[_343]
                _345 = dsdz * _344
                _346 = _int(k)
                _347 = _346 + -1
                _348 = dena[_347]
                _349 = _int(k)
                _350 = _349 + -1
                _351 = denb[_350]
                _352 = _348 - _351
                _353 = _352
                _354 = _345 * _353
                _355 = j[0]
                _356 = _int(_355)
                _357 = _356 * 63
                _358 = _int(k)
                _359 = _357 + _358
                _360 = _359 + -64
                _361 = _341 + _354
                rfrpth_amtp[_360] = _361
                _pc = 49
                continue
            case 48:  # __label_000130
                _362 = j[0]
                _363 = _int(_362)
                _364 = _363 * 63
                _365 = _int(k)
                _366 = _364 + _365
                _367 = _366 + -64
                _368 = rfrpth_denp[_367]
                _369 = j[0]
                _370 = _369 + 1
                _371 = _int(_370)
                _372 = _371 * 63
                _373 = _int(k)
                _374 = _372 + _373
                _375 = _374 + -64
                _376 = rfrpth_denp[_375]
                _377 = j[0]
                _378 = _int(_377)
                _379 = _378 * 63
                _380 = _int(k)
                _381 = _379 + _380
                _382 = _381 + -64
                _383 = rfrpth_denp[_382]
                _384 = _376 - _383
                _385 = _384
                h3_549_386 = h3[0]
                _387 = h3_549_386 - z1
                _388 = _387
                _389 = _385 * _388
                _390 = _div(_389, dz)
                _391 = _int(k)
                _392 = _391 + -1
                _393 = _368 + _390
                denb[_392] = _393
                _394 = j[0]
                _395 = _int(_394)
                _396 = _395 * 63
                _397 = _int(k)
                _398 = _396 + _397
                _399 = _398 + -64
                _400 = rfrpth_amtp[_399]
                _401 = _int(k)
                _402 = _401 + -1
                _403 = dena[_402]
                _404 = _int(k)
                _405 = _404 + -1
                _406 = denb[_405]
                _407 = _403 + _406
                _408 = _407
                _409 = _408 * 5.0e-1
                _410 = ds * _409
                _411 = j[0]
                _412 = _int(_411)
                _413 = _412 * 63
                _414 = _int(k)
                _415 = _413 + _414
                _416 = _415 + -64
                _417 = _400 + _410
                rfrpth_amtp[_416] = _417
                _pc = 49
            case 49:  # L.823
                k = _int(k + 1)
                _pc = 39
                continue
            case 50:  # L.824
                pa = _f32(pb)
                rhoa = _f32(rhob)
                D_13309 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 51
            case 51:  # <D.19537>
                D_13312 = _int(k > D_13309)
                _pc = 54 if D_13312 != 0 else 52
                continue
            case 52:  # __label_000145
                _418 = _int(k)
                _419 = _418 + -1
                _420 = _int(k)
                _421 = _420 + -1
                _422 = denb[_419]
                dena[_421] = _422
                _pc = 53
            case 53:  # L.828
                k = _int(k + 1)
                _pc = 51
                continue
            case 54:  # __label_000150
                h3_550_423 = h3[0]
                _pc = 55 if z2 <= h3_550_423 else 56
                continue
            case 55:  # <D.19539>
                _pc = 57
                continue
            case 56:  # L.830
                h3_551_424 = h3[0]
                h1[0] = h3_551_424
                r1 = _f32(r3)
                sinai1 = _f32(sinai3)
                ratio1 = _f32(ratio3)
                y1 = _f32(y3)
                cosai1 = _f32(cosai3)
                x1 = _f32(x3)
                dsdx1 = _f32(dsdx3)
                dbndx1 = _f32(dbndx3)
                _pc = 15
                continue
            case 57:  # __label_000160
                sinai[0] = sinai3
                cosai[0] = cosai3
                _425 = j[0]
                _426 = _int(_425)
                _427 = _426 + -1
                _428 = s[0]
                rfrpth_sp[_427] = _428
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_scalht(_state, z1, z2, rfndx1, rfndx2, sh, gamma):
    ratio = _ZERO32
    rf1 = _ZERO32
    rf2 = _ZERO32
    D_13321 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = rfndx1[0]
                rf1 = _f32(_1 + 9.9999996826552253889678874634872052240552875446155667305e-21)
                _2 = rfndx2[0]
                rf2 = _f32(_2 + 9.9999996826552253889678874634872052240552875446155667305e-21)
                ratio = _f32(_div(rf1, rf2))
                _3 = ratio - 1.0e+0
                _4 = abs(_3)
                _pc = 1 if _4 < 9.99999974737875163555145263671875e-6 else 2
                continue
            case 1:  # <D.19541>
                _pc = 3
                continue
            case 2:  # L.831
                _5 = z2[0]
                _6 = z1[0]
                _7 = _5 - _6
                _8 = _7
                _9 = __builtin_logf(ratio)
                _10 = _div(_8, _9)
                sh[0] = _10
                _11 = _div(rf2, rf1)
                D_13321 = _f32(_11)
                _12 = z1[0]
                _13 = z2[0]
                _14 = z1[0]
                _15 = _13 - _14
                _16 = _15
                _17 = _div(_12, _16)
                _18 = -_17
                _19 = _18
                _20 = __builtin_powf(D_13321, _19)
                _21 = rf1 * _20
                gamma[0] = _21
                _pc = -1
                continue
            case 3:  # __label_000100
                sh[0] = 0.0
                _22 = rfndx1[0]
                gamma[0] = _22
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_radref(_state, h, sh, gamma):
    cnstns_bignum = _state.view(246176, '<f4')
    cnstns_bigexp = _state.view(246180, '<f4')
    D_19547 = _ZERO32
    hsh = _ZERO32
    __result_radref = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = sh[0]
                _pc = 1 if _1 == 0.0 else 2
                continue
            case 1:  # <D.19543>
                _pc = 5
                continue
            case 2:  # L.832
                _2 = h[0]
                _3 = sh[0]
                hsh = _f32(_div(_2, _3))
                _4 = cnstns_bigexp[0]
                _pc = 3 if hsh > _4 else 4
                continue
            case 3:  # <D.19545>
                _pc = 5
                continue
            case 4:  # L.833
                _5 = sh[0]
                _6 = __builtin_expf(hsh)
                _7 = gamma[0]
                _8 = _div(_6, _7)
                _9 = _8 + 1.0e+0
                _10 = _9
                _11 = _5 * _10
                __result_radref = _f32(_11)
                D_19547 = _f32(__result_radref)
                return D_19547
            case 5:  # __label_000020
                _12 = cnstns_bignum[0]
                __result_radref = _f32(_12)
                D_19547 = _f32(__result_radref)
                return D_19547
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_fill(_state, ha, hb, jnext):
    cntrl_kmax = _state.view(245600, '<i4')
    model_z = _state.view(231904, '<f4')
    model_p = _state.view(232040, '<f4')
    model_t = _state.view(232176, '<f4')
    model_rfndx = _state.view(232312, '<f4')
    model_densty = _state.view(232448, '<f4')
    parmtr_imax = _state.view(245644, '<i4')
    rfrpth_zp = _state.view(246784, '<f4')
    rfrpth_pp = _state.view(246924, '<f4')
    rfrpth_tp = _state.view(247064, '<f4')
    rfrpth_rfndxp = _state.view(247204, '<f4')
    rfrpth_denp = _state.view(247904, '<f4')
    a = _zeros(1, '<f4')
    i = 0
    i1 = 0
    i2 = 0
    ia = 0
    ib = 0
    k = 0
    D_13459 = 0
    D_13462 = 0
    D_13467 = 0
    D_13468 = 0
    D_13471 = 0
    D_13476 = 0
    D_13479 = 0
    D_13483 = 0
    D_13484 = 0
    D_13487 = 0
    D_13488 = 0
    D_13491 = 0
    D_13495 = 0
    D_13498 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = ha[0]
                _2 = hb[0]
                _pc = 1 if _1 < _2 else 2
                continue
            case 1:  # <D.19550>
                _pc = 3
                continue
            case 2:  # __label_000022
                _gfortran_stop_string(0, 0, 0)
                _pc = 3
            case 3:  # __label_000090
                D_13459 = _int(parmtr_imax[0])
                i = _int(1)
                _pc = 4
            case 4:  # <D.19552>
                D_13462 = _int(i > D_13459)
                _pc = 9 if D_13462 != 0 else 5
                continue
            case 5:  # <D.19553>
                _3 = ha[0]
                _4 = _int(i)
                _5 = _4 + -1
                _6 = model_z[_5]
                _pc = 6 if _3 >= _6 else 7
                continue
            case 6:  # <D.19554>
                _pc = 8
                continue
            case 7:  # L.837
                ia = _int(i)
                _pc = 10
                continue
            case 8:  # L.835
                i = _int(i + 1)
                _pc = 4
                continue
            case 9:  # L.836
                _7 = parmtr_imax[0]
                ia = _int(_7 + 1)
                ib = _int(ia)
                _pc = 17
                continue
            case 10:  # __label_000110
                D_13467 = _int(ia)
                D_13468 = _int(parmtr_imax[0])
                i = _int(D_13467)
                _pc = 11
            case 11:  # <D.19556>
                D_13471 = _int(i > D_13468)
                _pc = 16 if D_13471 != 0 else 12
                continue
            case 12:  # <D.19557>
                _8 = hb[0]
                _9 = _int(i)
                _10 = _9 + -1
                _11 = model_z[_10]
                _12 = _8 - _11
                _pc = 13 if _12 > 9.99999974737875163555145263671875e-5 else 14
                continue
            case 13:  # <D.19558>
                _pc = 15
                continue
            case 14:  # L.840
                ib = _int(i)
                _pc = 17
                continue
            case 15:  # L.838
                i = _int(i + 1)
                _pc = 11
                continue
            case 16:  # L.839
                _13 = parmtr_imax[0]
                ib = _int(_13 + 1)
                _pc = 17
            case 17:  # __label_000130
                _14 = jnext[0]
                _15 = _int(_14)
                _16 = _15 + -1
                _17 = ha[0]
                rfrpth_zp[_16] = _17
                i2 = _int(ia)
                _pc = 18 if i2 == 1 else 19
                continue
            case 18:  # <D.19560>
                i2 = _int(2)
                _pc = 19
                continue
            case 19:  # L.841
                _18 = parmtr_imax[0]
                _pc = 20 if i2 > _18 else 21
                continue
            case 20:  # <D.19563>
                i2 = _int(parmtr_imax[0])
                _pc = 21
                continue
            case 21:  # L.842
                i1 = _int(i2 + -1)
                _19 = ha[0]
                _20 = _int(i1)
                _21 = _20 + -1
                _22 = model_z[_21]
                _23 = _19 - _22
                _24 = _23
                _25 = _int(i2)
                _26 = _25 + -1
                _27 = model_z[_26]
                _28 = _int(i1)
                _29 = _28 + -1
                _30 = model_z[_29]
                _31 = _27 - _30
                _32 = _31
                _33 = _div(_24, _32)
                a[0] = _33
                _34 = _int(i2)
                _35 = _34 + -1
                _36 = model_p[_35:]
                _37 = _int(i1)
                _38 = _37 + -1
                _39 = model_p[_38:]
                _40 = jnext[0]
                _41 = _int(_40)
                _42 = _41 + -1
                _43 = rfrpth_pp[_42:]
                _ft_expint(_state, _43, _39, _36, a)
                _44 = _int(i1)
                _45 = _44 + -1
                _46 = model_t[_45]
                _47 = _int(i2)
                _48 = _47 + -1
                _49 = model_t[_48]
                _50 = _int(i1)
                _51 = _50 + -1
                _52 = model_t[_51]
                _53 = _49 - _52
                _54 = _53
                a_552_55 = a[0]
                _56 = _54 * a_552_55
                _57 = jnext[0]
                _58 = _int(_57)
                _59 = _58 + -1
                _60 = _46 + _56
                rfrpth_tp[_59] = _60
                _61 = _int(i2)
                _62 = _61 + -1
                _63 = model_rfndx[_62:]
                _64 = _int(i1)
                _65 = _64 + -1
                _66 = model_rfndx[_65:]
                _67 = jnext[0]
                _68 = _int(_67)
                _69 = _68 + -1
                _70 = rfrpth_rfndxp[_69:]
                _ft_expint(_state, _70, _66, _63, a)
                D_13476 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 22
            case 22:  # <D.19566>
                D_13479 = _int(k > D_13476)
                _pc = 25 if D_13479 != 0 else 23
                continue
            case 23:  # <D.19567>
                _71 = _int(i2)
                _72 = _71 * 63
                _73 = _int(k)
                _74 = _72 + _73
                _75 = _74 + -64
                _76 = model_densty[_75:]
                _77 = _int(i1)
                _78 = _77 * 63
                _79 = _int(k)
                _80 = _78 + _79
                _81 = _80 + -64
                _82 = model_densty[_81:]
                _83 = jnext[0]
                _84 = _int(_83)
                _85 = _84 * 63
                _86 = _int(k)
                _87 = _85 + _86
                _88 = _87 + -64
                _89 = rfrpth_denp[_88:]
                _ft_expint(_state, _89, _82, _76, a)
                _pc = 24
            case 24:  # L.843
                k = _int(k + 1)
                _pc = 22
                continue
            case 25:  # L.844
                _pc = 26 if ia == ib else 27
                continue
            case 26:  # <D.19568>
                _pc = 34
                continue
            case 27:  # L.845
                i1 = _int(ia)
                i2 = _int(ib + -1)
                D_13483 = _int(i1)
                D_13484 = _int(i2)
                i = _int(D_13483)
                _pc = 28
            case 28:  # <D.19570>
                D_13487 = _int(i > D_13484)
                _pc = 34 if D_13487 != 0 else 29
                continue
            case 29:  # <D.19571>
                _90 = jnext[0]
                _91 = _90 + 1
                jnext[0] = _91
                _92 = _int(i)
                _93 = _92 + -1
                _94 = jnext[0]
                _95 = _int(_94)
                _96 = _95 + -1
                _97 = model_z[_93]
                rfrpth_zp[_96] = _97
                _98 = _int(i)
                _99 = _98 + -1
                _100 = jnext[0]
                _101 = _int(_100)
                _102 = _101 + -1
                _103 = model_p[_99]
                rfrpth_pp[_102] = _103
                _104 = _int(i)
                _105 = _104 + -1
                _106 = jnext[0]
                _107 = _int(_106)
                _108 = _107 + -1
                _109 = model_t[_105]
                rfrpth_tp[_108] = _109
                _110 = _int(i)
                _111 = _110 + -1
                _112 = jnext[0]
                _113 = _int(_112)
                _114 = _113 + -1
                _115 = model_rfndx[_111]
                rfrpth_rfndxp[_114] = _115
                D_13488 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 30
            case 30:  # <D.19572>
                D_13491 = _int(k > D_13488)
                _pc = 33 if D_13491 != 0 else 31
                continue
            case 31:  # <D.19573>
                _116 = _int(i)
                _117 = _116 * 63
                _118 = _int(k)
                _119 = _117 + _118
                _120 = _119 + -64
                _121 = jnext[0]
                _122 = _int(_121)
                _123 = _122 * 63
                _124 = _int(k)
                _125 = _123 + _124
                _126 = _125 + -64
                _127 = model_densty[_120]
                rfrpth_denp[_126] = _127
                _pc = 32
            case 32:  # L.848
                k = _int(k + 1)
                _pc = 30
                continue
            case 33:  # L.846
                i = _int(i + 1)
                _pc = 28
                continue
            case 34:  # __label_000160
                _128 = jnext[0]
                _129 = _128 + 1
                jnext[0] = _129
                _130 = jnext[0]
                _131 = _int(_130)
                _132 = _131 + -1
                _133 = hb[0]
                rfrpth_zp[_132] = _133
                i2 = _int(ib)
                _pc = 35 if i2 == 1 else 36
                continue
            case 35:  # <D.19574>
                i2 = _int(2)
                _pc = 36
                continue
            case 36:  # L.850
                _134 = parmtr_imax[0]
                _pc = 37 if i2 > _134 else 38
                continue
            case 37:  # <D.19577>
                i2 = _int(parmtr_imax[0])
                _pc = 38
                continue
            case 38:  # L.851
                i1 = _int(i2 + -1)
                _135 = hb[0]
                _136 = _int(i1)
                _137 = _136 + -1
                _138 = model_z[_137]
                _139 = _135 - _138
                _140 = _139
                _141 = _int(i2)
                _142 = _141 + -1
                _143 = model_z[_142]
                _144 = _int(i1)
                _145 = _144 + -1
                _146 = model_z[_145]
                _147 = _143 - _146
                _148 = _147
                _149 = _div(_140, _148)
                a[0] = _149
                _150 = _int(i2)
                _151 = _150 + -1
                _152 = model_p[_151:]
                _153 = _int(i1)
                _154 = _153 + -1
                _155 = model_p[_154:]
                _156 = jnext[0]
                _157 = _int(_156)
                _158 = _157 + -1
                _159 = rfrpth_pp[_158:]
                _ft_expint(_state, _159, _155, _152, a)
                _160 = _int(i1)
                _161 = _160 + -1
                _162 = model_t[_161]
                _163 = _int(i2)
                _164 = _163 + -1
                _165 = model_t[_164]
                _166 = _int(i1)
                _167 = _166 + -1
                _168 = model_t[_167]
                _169 = _165 - _168
                _170 = _169
                a_553_171 = a[0]
                _172 = _170 * a_553_171
                _173 = jnext[0]
                _174 = _int(_173)
                _175 = _174 + -1
                _176 = _162 + _172
                rfrpth_tp[_175] = _176
                _177 = _int(i2)
                _178 = _177 + -1
                _179 = model_rfndx[_178:]
                _180 = _int(i1)
                _181 = _180 + -1
                _182 = model_rfndx[_181:]
                _183 = jnext[0]
                _184 = _int(_183)
                _185 = _184 + -1
                _186 = rfrpth_rfndxp[_185:]
                _ft_expint(_state, _186, _182, _179, a)
                D_13495 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 39
            case 39:  # <D.19580>
                D_13498 = _int(k > D_13495)
                _pc = -1 if D_13498 != 0 else 40
                continue
            case 40:  # <D.19581>
                _187 = _int(i2)
                _188 = _187 * 63
                _189 = _int(k)
                _190 = _188 + _189
                _191 = _190 + -64
                _192 = model_densty[_191:]
                _193 = _int(i1)
                _194 = _193 * 63
                _195 = _int(k)
                _196 = _194 + _195
                _197 = _196 + -64
                _198 = model_densty[_197:]
                _199 = jnext[0]
                _200 = _int(_199)
                _201 = _200 * 63
                _202 = _int(k)
                _203 = _201 + _202
                _204 = _203 + -64
                _205 = rfrpth_denp[_204:]
                _ft_expint(_state, _205, _198, _192, a)
                _pc = 41
            case 41:  # L.852
                k = _int(k + 1)
                _pc = 39
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_expint(_state, x, x1, x2, a):
    D_13502 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = x1[0]
                _2 = _1 == 0.0
                _3 = x2[0]
                _4 = _3 == 0.0
                _5 = _2 | _4
                _pc = 1 if _5 != 0 else 2
                continue
            case 1:  # <D.19582>
                _pc = 3
                continue
            case 2:  # L.854
                _6 = x2[0]
                _7 = x1[0]
                _8 = _div(_6, _7)
                D_13502 = _f32(_8)
                _9 = x1[0]
                _10 = a[0]
                _11 = __builtin_powf(D_13502, _10)
                _12 = _9 * _11
                x[0] = _12
                return
            case 3:  # __label_000100
                _13 = x1[0]
                _14 = x2[0]
                _15 = x1[0]
                _16 = _14 - _15
                _17 = _16
                _18 = a[0]
                _19 = _17 * _18
                _20 = _13 + _19
                x[0] = _20
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_stdmdl(_state):
    __BLNK___relhum = _state.view(265568, '<f4')
    __BLNK___hstor = _state.view(265704, '<f4')
    __BLNK___ich = _state.view(265840, '<i4')
    card2_icld = _state.view(231760, '<i4')
    card4_v1 = _state.view(286864, '<f4')
    card4_v2 = _state.view(286868, '<f4')
    cntrl_ml = _state.view(245616, '<i4')
    ifil_npr = _state.view(243020, '<i4')
    mdata_p = _state.view(149320, '<f4')
    mdata_t = _state.view(149520, '<f4')
    mdata_wh = _state.view(149720, '<f4')
    mdata_wco2 = _state.view(149920, '<f4')
    mdata_wo = _state.view(150120, '<f4')
    mdata_wn2o = _state.view(150320, '<f4')
    mdata_wco = _state.view(150520, '<f4')
    mdata_wch4 = _state.view(150720, '<f4')
    mdata_wo2 = _state.view(150920, '<f4')
    mdata1_wno = _state.view(286880, '<f4')
    mdata1_wso2 = _state.view(287080, '<f4')
    mdata1_wno2 = _state.view(287280, '<f4')
    mdata1_wnh3 = _state.view(287480, '<f4')
    mdata1_wair = _state.view(287680, '<f4')
    model_zm = _state.view(231904, '<f4')
    model_pm = _state.view(232040, '<f4')
    model_tm = _state.view(232176, '<f4')
    model_rfndx = _state.view(232312, '<f4')
    model_densty = _state.view(232448, '<f4')
    model_rramt = _state.view(241152, '<f4')
    a0 = _state.view(180400, '<f4')
    a1 = _state.view(180396, '<f4')
    a2 = _state.view(180404, '<f4')
    b1 = _state.view(180384, '<f4')
    b2 = _state.view(180388, '<f4')
    c0 = _state.view(180408, '<f4')
    c1 = _state.view(180392, '<f4')
    con = _state.view(180372, '<f4')
    pzero = _state.view(180364, '<f4')
    rv = _state.view(180380, '<f4')
    tzero = _state.view(180368, '<f4')
    xlosch = _state.view(180376, '<f4')
    avw = _ZERO32
    conch4 = _ZERO32
    conco = _ZERO32
    conco2 = _ZERO32
    conh2o = _ZERO32
    conjoe = _ZERO32
    conn2o = _ZERO32
    connh3 = _ZERO32
    conno = _ZERO32
    conno2 = _ZERO32
    cono2 = _ZERO32
    cono3 = _ZERO32
    conso2 = _ZERO32
    dt = _ZERO32
    f1 = _ZERO32
    f2 = _ZERO32
    i = 0
    pp = _ZERO32
    ppw = _ZERO32
    pss = _ZERO32
    relh = _ZERO32
    rhlog = _ZERO32
    rhoair = _ZERO32
    rhofrn = _ZERO32
    rhoh2o = _ZERO32
    rhzero = _ZERO32
    ts = _ZERO32
    tss = _ZERO32
    tt = _ZERO32
    wo2d = _ZERO32
    wtemp = _ZERO32
    D_13765 = 0
    D_13768 = 0
    D_13771 = _ZERO32
    D_13772 = _ZERO32
    D_13776 = _ZERO32
    D_13778 = _ZERO32
    D_13779 = _ZERO32
    D_13780 = _ZERO32
    D_13781 = _ZERO32
    D_13782 = _ZERO32
    D_13783 = _ZERO32
    D_13784 = _ZERO32
    D_13785 = _ZERO32
    D_13786 = _ZERO32
    D_13787 = _ZERO32
    D_13788 = _ZERO32
    D_13789 = _ZERO32
    D_13790 = _ZERO32
    D_13791 = _ZERO32
    D_13792 = _ZERO32
    D_13793 = _ZERO32
    D_13794 = _ZERO32
    D_13795 = _ZERO32
    D_13796 = _ZERO32
    D_13797 = _ZERO32
    D_13798 = _ZERO32
    D_13799 = _ZERO32
    D_13800 = _ZERO32
    D_13801 = _ZERO32
    D_13802 = _ZERO32
    D_13803 = _ZERO32
    D_13804 = _ZERO32
    D_13805 = _ZERO32
    D_13806 = _ZERO32
    D_13807 = _ZERO32
    D_13808 = _ZERO32
    D_13809 = _ZERO32
    D_13810 = _ZERO32
    D_13811 = _ZERO32
    D_13812 = _ZERO32
    D_13813 = _ZERO32
    D_13814 = _ZERO32
    D_13815 = _ZERO32
    D_13816 = _ZERO32
    D_13817 = _ZERO32
    D_13818 = _ZERO32
    D_13819 = _ZERO32
    D_13820 = _ZERO32
    D_13821 = _ZERO32
    D_13822 = _ZERO32
    D_13823 = _ZERO32
    D_13824 = _ZERO32
    D_13825 = _ZERO32
    D_13826 = _ZERO32
    D_13827 = _ZERO32
    D_13828 = _ZERO32
    D_13829 = _ZERO32
    D_13830 = _ZERO32
    D_13831 = _ZERO32
    D_13832 = _ZERO32
    D_13833 = _ZERO32
    D_13834 = _ZERO32
    D_13835 = _ZERO32
    D_13836 = _ZERO32
    D_13837 = _ZERO32
    D_13838 = _ZERO32
    D_13839 = _ZERO32
    D_13840 = _ZERO32
    D_13841 = _ZERO32
    D_13842 = _ZERO32
    D_13843 = _ZERO32
    D_13844 = _ZERO32
    D_13845 = _ZERO32
    D_13846 = _ZERO32
    D_13847 = _ZERO32
    D_13848 = _ZERO32
    D_13849 = _ZERO32
    D_13850 = _ZERO32
    D_13851 = _ZERO32
    D_13852 = _ZERO32
    D_13853 = _ZERO32
    D_13854 = _ZERO32
    D_13855 = _ZERO32
    D_13856 = _ZERO32
    D_13857 = _ZERO32
    D_13858 = _ZERO32
    D_13859 = _ZERO32
    D_13860 = _ZERO32
    D_13861 = _ZERO32
    D_13862 = _ZERO32
    D_13863 = _ZERO32
    D_13864 = _ZERO32
    D_13865 = _ZERO32
    D_13869 = 0
    D_13872 = 0
    D_13874 = 0
    D_13877 = 0
    D_13879 = 0
    D_13882 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                conjoe = _f32(3.71939985288621612110533686847146928045049207867123186588e-21)
                rhzero = _f32(9.22804057598114013671875e-1)
                D_13765 = _int(cntrl_ml[0])
                i = _int(1)
                _pc = 1
            case 1:  # <D.19585>
                D_13768 = _int(i > D_13765)
                _pc = 15 if D_13768 != 0 else 2
                continue
            case 2:  # <D.19586>
                _1 = _int(i)
                _2 = _1 + -1
                _3 = _int(i)
                _4 = _3 + -1
                _5 = mdata_p[_2]
                model_pm[_4] = _5
                _6 = _int(i)
                _7 = _6 + -1
                _8 = _int(i)
                _9 = _8 + -1
                _10 = mdata_t[_7]
                model_tm[_9] = _10
                _11 = _int(i)
                _12 = _11 + -1
                pp = _f32(model_pm[_12])
                _13 = _int(i)
                _14 = _13 + -1
                tt = _f32(model_tm[_14])
                pzero_554_15 = pzero[0]
                pss = _f32(_div(pp, pzero_554_15))
                tzero_555_16 = tzero[0]
                tss = _f32(_div(tzero_555_16, tt))
                pzero_556_17 = pzero[0]
                _18 = _div(pp, pzero_556_17)
                _19 = _18
                tzero_557_20 = tzero[0]
                _21 = _div(tt, tzero_557_20)
                _22 = _21
                f1 = _f32(_div(_19, _22))
                pzero_558_23 = pzero[0]
                _24 = _div(pp, pzero_558_23)
                _25 = _24
                tzero_559_26 = tzero[0]
                _27 = _div(tzero_559_26, tt)
                _28 = __builtin_sqrtf(_27)
                f2 = _f32(_25 * _28)
                _29 = _int(i)
                _30 = _29 + -1
                wtemp = _f32(mdata_wh[_30])
                _31 = _int(i)
                _32 = _31 + -1
                _33 = model_zm[_32]
                _pc = 3 if _33 > 2.0e+0 else 4
                continue
            case 3:  # <D.19587>
                _pc = 5
                continue
            case 4:  # L.857
                tzero_560_34 = tzero[0]
                ts = _f32(_div(tzero_560_34, tt))
                _pc = 5
            case 5:  # __label_000015
                _35 = _int(i)
                _36 = _35 + -1
                _37 = mdata1_wair[_36]
                _38 = conjoe * _37
                _39 = _int(i)
                _40 = _39 + -1
                _41 = mdata_wo[_40]
                _42 = _int(i)
                _43 = _42 * 63
                _44 = _43 + -56
                _45 = _38 * _41
                model_densty[_44] = _45
                _46 = f1 * 7.8100001811981201171875e-1
                _47 = _int(i)
                _48 = _47 * 63
                _49 = _48 + -60
                _50 = f2 * _46
                model_densty[_49] = _50
                rhoair = _f32(f1)
                con_561_51 = con[0]
                _52 = wtemp * con_561_51
                xlosch_562_53 = xlosch[0]
                rhoh2o = _f32(_div(_52, xlosch_562_53))
                rhofrn = _f32(rhoair - rhoh2o)
                D_13771 = _f32(rhoh2o)
                D_13772 = _f32(D_13771 * D_13771)
                xlosch_563_54 = xlosch[0]
                _55 = D_13772 * xlosch_563_54
                _56 = _int(i)
                _57 = _56 * 63
                _58 = _57 + -59
                _59 = _div(_55, rhzero)
                model_densty[_58] = _59
                xlosch_564_60 = xlosch[0]
                _61 = rhoh2o * xlosch_564_60
                _62 = rhofrn * _61
                _63 = _int(i)
                _64 = _63 * 63
                _65 = _64 + -54
                _66 = _div(_62, rhzero)
                model_densty[_65] = _66
                _67 = _int(i)
                _68 = _67 * 63
                _69 = _68 + -58
                model_densty[_69] = f1
                _70 = _int(i)
                _71 = _70 + -1
                relh = _f32(__BLNK___relhum[_71])
                _72 = _int(i)
                _73 = _72 + -1
                _74 = __BLNK___relhum[_73]
                _pc = 6 if _74 > 9.9e+1 else 7
                continue
            case 6:  # <D.19589>
                relh = _f32(9.9e+1)
                _pc = 7
                continue
            case 7:  # L.858
                _75 = 1.0e+2 - relh
                rhlog = _f32(__builtin_logf(_75))
                _76 = _int(i)
                _77 = _76 * 63
                _78 = _77 + -57
                _79 = model_densty[_78]
                _80 = _int(i)
                _81 = _80 * 63
                _82 = _81 + -49
                _83 = rhlog * _79
                model_densty[_82] = _83
                _84 = _int(i)
                _85 = _84 * 63
                _86 = _85 + -55
                model_densty[_86] = 0.0
                _87 = __BLNK___ich[0]
                _pc = 8 if _87 > 7 else 9
                continue
            case 8:  # <D.19592>
                _88 = _int(i)
                _89 = _88 * 63
                _90 = _89 + -52
                _91 = model_densty[_90]
                _92 = _int(i)
                _93 = _92 * 63
                _94 = _93 + -49
                _95 = rhlog * _91
                model_densty[_94] = _95
                _pc = 9
                continue
            case 9:  # L.859
                _96 = _int(i)
                _97 = _96 + -1
                _98 = __BLNK___hstor[_97]
                _99 = f1 * _98
                _100 = _int(i)
                _101 = _100 * 63
                _102 = _101 + -53
                _103 = _99 * 9.99999974737875163555145263671875e-5
                model_densty[_102] = _103
                dt = _f32(tt - 2.2e+2)
                _104 = _int(i)
                _105 = _104 + -1
                _106 = mdata1_wair[_105]
                _107 = conjoe * _106
                _108 = _int(i)
                _109 = _108 + -1
                _110 = mdata_wo2[_109]
                _111 = _107 * _110
                wo2d = _f32(pss * _111)
                _112 = _int(i)
                _113 = _112 + -1
                _114 = _113 * 63
                _115 = wo2d * tt
                model_densty[_114] = _115
                _116 = wo2d * dt
                _117 = _int(i)
                _118 = _117 * 63
                _119 = _118 + -62
                _120 = dt * _116
                model_densty[_119] = _120
                _121 = _int(i)
                _122 = _121 * 63
                _123 = _122 + -1
                model_densty[_123] = wo2d
                _124 = _int(i)
                _125 = _124 * 63
                _126 = _125 + -61
                model_densty[_126] = 0.0
                _127 = _int(i)
                _128 = _127 * 63
                _129 = _128 + -3
                model_densty[_129] = 0.0
                _130 = _int(i)
                _131 = _130 * 63
                _132 = _131 + -2
                model_densty[_132] = 0.0
                _133 = _int(i)
                _134 = _133 + -1
                _135 = model_rramt[_134]
                _pc = 10 if _135 != 0.0 else 11
                continue
            case 10:  # <D.19595>
                _136 = _int(i)
                _137 = _136 + -1
                D_13776 = _f32(model_rramt[_137])
                _138 = _int(i)
                _139 = _138 * 63
                _140 = _139 + -61
                _141 = __builtin_powf(D_13776, 6.2999999523162841796875e-1)
                model_densty[_140] = _141
                _142 = _int(i)
                _143 = _142 * 63
                _144 = _143 + -61
                _145 = model_densty[_144]
                _146 = _int(i)
                _147 = _146 + -1
                _148 = mdata_t[_147]
                _149 = _int(i)
                _150 = _149 * 63
                _151 = _150 + -3
                _152 = _145 * _148
                model_densty[_151] = _152
                _153 = _int(i)
                _154 = _153 * 63
                _155 = _154 + -2
                model_densty[_155] = 1.0e+0
                _pc = 11
                continue
            case 11:  # L.860
                _156 = card2_icld[0]
                _pc = 12 if _156 <= 17 else 13
                continue
            case 12:  # <D.19598>
                _157 = _int(i)
                _158 = _157 * 63
                _159 = _158 + -48
                model_densty[_159] = 0.0
                _pc = 13
                continue
            case 13:  # L.861
                _160 = _int(i)
                _161 = _160 + -1
                _162 = mdata_wh[_161]
                conh2o = _f32(_162 * 1.00000001490116119384765625e-1)
                D_13778 = _f32(pss)
                D_13779 = _f32(tss)
                _163 = __builtin_powf(D_13778, 9.81000006198883056640625e-1)
                _164 = conh2o * _163
                _165 = __builtin_powf(D_13779, 3.323999941349029541015625e-1)
                _166 = _int(i)
                _167 = _166 * 63
                _168 = _167 + -47
                _169 = _164 * _165
                model_densty[_168] = _169
                D_13780 = _f32(pss)
                D_13781 = _f32(tss)
                _170 = __builtin_powf(D_13780, 1.1405999660491943359375e+0)
                _171 = conh2o * _170
                _172 = __builtin_powf(D_13781, -2.6342999935150146484375e+0)
                _173 = _int(i)
                _174 = _173 * 63
                _175 = _174 + -46
                _176 = _171 * _172
                model_densty[_175] = _176
                D_13782 = _f32(pss)
                D_13783 = _f32(tss)
                _177 = __builtin_powf(D_13782, 9.8339998722076416015625e-1)
                _178 = conh2o * _177
                _179 = __builtin_powf(D_13783, -2.5294001102447509765625e+0)
                _180 = _int(i)
                _181 = _180 * 63
                _182 = _181 + -45
                _183 = _178 * _179
                model_densty[_182] = _183
                D_13784 = _f32(pss)
                D_13785 = _f32(tss)
                _184 = __builtin_powf(D_13784, 1.04429996013641357421875e+0)
                _185 = conh2o * _184
                _186 = __builtin_powf(D_13785, -2.4358999729156494140625e+0)
                _187 = _int(i)
                _188 = _187 * 63
                _189 = _188 + -44
                _190 = _185 * _186
                model_densty[_189] = _190
                D_13786 = _f32(pss)
                D_13787 = _f32(tss)
                _191 = __builtin_powf(D_13786, 9.68100011348724365234375e-1)
                _192 = conh2o * _191
                _193 = __builtin_powf(D_13787, -1.95369994640350341796875e+0)
                _194 = _int(i)
                _195 = _194 * 63
                _196 = _195 + -43
                _197 = _192 * _193
                model_densty[_196] = _197
                D_13788 = _f32(pss)
                D_13789 = _f32(tss)
                _198 = __builtin_powf(D_13788, 9.5550000667572021484375e-1)
                _199 = conh2o * _198
                _200 = __builtin_powf(D_13789, -1.53779995441436767578125e+0)
                _201 = _int(i)
                _202 = _201 * 63
                _203 = _202 + -42
                _204 = _199 * _200
                model_densty[_203] = _204
                D_13790 = _f32(pss)
                D_13791 = _f32(tss)
                _205 = __builtin_powf(D_13790, 9.3620002269744873046875e-1)
                _206 = conh2o * _205
                _207 = __builtin_powf(D_13791, -1.633800029754638671875e+0)
                _208 = _int(i)
                _209 = _208 * 63
                _210 = _209 + -41
                _211 = _206 * _207
                model_densty[_210] = _211
                D_13792 = _f32(pss)
                D_13793 = _f32(tss)
                _212 = __builtin_powf(D_13792, 9.233000278472900390625e-1)
                _213 = conh2o * _212
                _214 = __builtin_powf(D_13793, -9.398000240325927734375e-1)
                _215 = _int(i)
                _216 = _215 * 63
                _217 = _216 + -40
                _218 = _213 * _214
                model_densty[_217] = _218
                D_13794 = _f32(pss)
                D_13795 = _f32(tss)
                _219 = __builtin_powf(D_13794, 8.6580002307891845703125e-1)
                _220 = conh2o * _219
                _221 = __builtin_powf(D_13795, -1.03399999439716339111328125e-1)
                _222 = _int(i)
                _223 = _222 * 63
                _224 = _223 + -39
                _225 = _220 * _221
                model_densty[_224] = _225
                D_13796 = _f32(pss)
                D_13797 = _f32(tss)
                _226 = __builtin_powf(D_13796, 8.87399971485137939453125e-1)
                _227 = conh2o * _226
                _228 = __builtin_powf(D_13797, -2.57600009441375732421875e-1)
                _229 = _int(i)
                _230 = _229 * 63
                _231 = _230 + -38
                _232 = _227 * _228
                model_densty[_231] = _232
                D_13798 = _f32(pss)
                D_13799 = _f32(tss)
                _233 = __builtin_powf(D_13798, 7.9820001125335693359375e-1)
                _234 = conh2o * _233
                _235 = __builtin_powf(D_13799, 5.88000006973743438720703125e-2)
                _236 = _int(i)
                _237 = _236 * 63
                _238 = _237 + -37
                _239 = _234 * _235
                model_densty[_238] = _239
                D_13800 = _f32(pss)
                D_13801 = _f32(tss)
                _240 = __builtin_powf(D_13800, 8.087999820709228515625e-1)
                _241 = conh2o * _240
                _242 = __builtin_powf(D_13801, 2.8159999847412109375e-1)
                _243 = _int(i)
                _244 = _243 * 63
                _245 = _244 + -36
                _246 = _241 * _242
                model_densty[_245] = _246
                D_13802 = _f32(pss)
                D_13803 = _f32(tss)
                _247 = __builtin_powf(D_13802, 6.64200007915496826171875e-1)
                _248 = conh2o * _247
                _249 = __builtin_powf(D_13803, 2.763999998569488525390625e-1)
                _250 = _int(i)
                _251 = _250 * 63
                _252 = _251 + -35
                _253 = _248 * _249
                model_densty[_252] = _253
                D_13804 = _f32(pss)
                D_13805 = _f32(tss)
                _254 = __builtin_powf(D_13804, 6.65600001811981201171875e-1)
                _255 = conh2o * _254
                _256 = __builtin_powf(D_13805, 5.06099998950958251953125e-1)
                _257 = _int(i)
                _258 = _257 * 63
                _259 = _258 + -34
                _260 = _255 * _256
                model_densty[_259] = _260
                _261 = _int(i)
                _262 = _261 + -1
                _263 = mdata1_wair[_262]
                _264 = conjoe * _263
                _265 = _int(i)
                _266 = _265 + -1
                _267 = mdata_wo[_266]
                cono3 = _f32(_264 * _267)
                D_13806 = _f32(pss)
                D_13807 = _f32(tss)
                _268 = __builtin_powf(D_13806, 4.199999868869781494140625e-1)
                _269 = cono3 * _268
                _270 = __builtin_powf(D_13807, 1.39090001583099365234375e+0)
                _271 = _int(i)
                _272 = _271 * 63
                _273 = _272 + -33
                _274 = _269 * _270
                model_densty[_273] = _274
                D_13808 = _f32(pss)
                D_13809 = _f32(tss)
                _275 = __builtin_powf(D_13808, 4.22100007534027099609375e-1)
                _276 = cono3 * _275
                _277 = __builtin_powf(D_13809, 7.6779997348785400390625e-1)
                _278 = _int(i)
                _279 = _278 * 63
                _280 = _279 + -32
                _281 = _276 * _277
                model_densty[_280] = _281
                D_13810 = _f32(pss)
                D_13811 = _f32(tss)
                _282 = __builtin_powf(D_13810, 3.73899996280670166015625e-1)
                _283 = cono3 * _282
                _284 = __builtin_powf(D_13811, 1.22500002384185791015625e-1)
                _285 = _int(i)
                _286 = _285 * 63
                _287 = _286 + -31
                _288 = _283 * _284
                model_densty[_287] = _288
                D_13812 = _f32(pss)
                D_13813 = _f32(tss)
                _289 = __builtin_powf(D_13812, 1.7700000107288360595703125e-1)
                _290 = cono3 * _289
                _291 = __builtin_powf(D_13813, 9.8269999027252197265625e-1)
                _292 = _int(i)
                _293 = _292 * 63
                _294 = _293 + -30
                _295 = _290 * _291
                model_densty[_294] = _295
                D_13814 = _f32(pss)
                D_13815 = _f32(tss)
                _296 = __builtin_powf(D_13814, 3.921000063419342041015625e-1)
                _297 = cono3 * _296
                _298 = __builtin_powf(D_13815, 1.9419999420642852783203125e-1)
                _299 = _int(i)
                _300 = _299 * 63
                _301 = _300 + -29
                _302 = _297 * _298
                model_densty[_301] = _302
                _303 = _int(i)
                _304 = _303 + -1
                _305 = mdata1_wair[_304]
                _306 = conjoe * _305
                _307 = _int(i)
                _308 = _307 + -1
                _309 = mdata_wco2[_308]
                conco2 = _f32(_306 * _309)
                D_13816 = _f32(pss)
                D_13817 = _f32(tss)
                _310 = __builtin_powf(D_13816, 6.70499980449676513671875e-1)
                _311 = conco2 * _310
                _312 = __builtin_powf(D_13817, -2.256000041961669921875e+0)
                _313 = _int(i)
                _314 = _313 * 63
                _315 = _314 + -28
                _316 = _311 * _312
                model_densty[_315] = _316
                D_13818 = _f32(pss)
                D_13819 = _f32(tss)
                _317 = __builtin_powf(D_13818, 7.03800022602081298828125e-1)
                _318 = conco2 * _317
                _319 = __builtin_powf(D_13819, -5.076799869537353515625e+0)
                _320 = _int(i)
                _321 = _320 * 63
                _322 = _321 + -27
                _323 = _318 * _319
                model_densty[_322] = _323
                D_13820 = _f32(pss)
                D_13821 = _f32(tss)
                _324 = __builtin_powf(D_13820, 7.25799977779388427734375e-1)
                _325 = conco2 * _324
                _326 = __builtin_powf(D_13821, -1.6740000247955322265625e+0)
                _327 = _int(i)
                _328 = _327 * 63
                _329 = _328 + -26
                _330 = _325 * _326
                model_densty[_329] = _330
                D_13822 = _f32(pss)
                D_13823 = _f32(tss)
                _331 = __builtin_powf(D_13822, 6.981999874114990234375e-1)
                _332 = conco2 * _331
                _333 = __builtin_powf(D_13823, -1.81070005893707275390625e+0)
                _334 = _int(i)
                _335 = _334 * 63
                _336 = _335 + -25
                _337 = _332 * _333
                model_densty[_336] = _337
                D_13824 = _f32(pss)
                D_13825 = _f32(tss)
                _338 = __builtin_powf(D_13824, 8.86699974536895751953125e-1)
                _339 = conco2 * _338
                _340 = __builtin_powf(D_13825, -5.32700002193450927734375e-1)
                _341 = _int(i)
                _342 = _341 * 63
                _343 = _342 + -24
                _344 = _339 * _340
                model_densty[_343] = _344
                D_13826 = _f32(pss)
                D_13827 = _f32(tss)
                _345 = __builtin_powf(D_13826, 7.88299977779388427734375e-1)
                _346 = conco2 * _345
                _347 = __builtin_powf(D_13827, -1.3243999481201171875e+0)
                _348 = _int(i)
                _349 = _348 * 63
                _350 = _349 + -23
                _351 = _346 * _347
                model_densty[_350] = _351
                D_13828 = _f32(pss)
                D_13829 = _f32(tss)
                _352 = __builtin_powf(D_13828, 6.89899981021881103515625e-1)
                _353 = conco2 * _352
                _354 = __builtin_powf(D_13829, -8.1519997119903564453125e-1)
                _355 = _int(i)
                _356 = _355 * 63
                _357 = _356 + -22
                _358 = _353 * _354
                model_densty[_357] = _358
                D_13830 = _f32(pss)
                D_13831 = _f32(tss)
                _359 = __builtin_powf(D_13830, 6.0350000858306884765625e-1)
                _360 = conco2 * _359
                _361 = __builtin_powf(D_13831, 6.0259997844696044921875e-1)
                _362 = _int(i)
                _363 = _362 * 63
                _364 = _363 + -21
                _365 = _360 * _361
                model_densty[_364] = _365
                _366 = _int(i)
                _367 = _366 + -1
                _368 = mdata1_wair[_367]
                _369 = conjoe * _368
                _370 = _int(i)
                _371 = _370 + -1
                _372 = mdata_wco[_371]
                conco = _f32(_369 * _372)
                D_13832 = _f32(pss)
                D_13833 = _f32(tss)
                _373 = __builtin_powf(D_13832, 7.58899986743927001953125e-1)
                _374 = conco * _373
                _375 = __builtin_powf(D_13833, 6.9110000133514404296875e-1)
                _376 = _int(i)
                _377 = _376 * 63
                _378 = _377 + -20
                _379 = _374 * _375
                model_densty[_378] = _379
                D_13834 = _f32(pss)
                D_13835 = _f32(tss)
                _380 = __builtin_powf(D_13834, 9.2669999599456787109375e-1)
                _381 = conco * _380
                _382 = __builtin_powf(D_13835, 1.7159999907016754150390625e-1)
                _383 = _int(i)
                _384 = _383 * 63
                _385 = _384 + -19
                _386 = _381 * _382
                model_densty[_385] = _386
                _387 = _int(i)
                _388 = _387 + -1
                _389 = mdata1_wair[_388]
                _390 = conjoe * _389
                _391 = _int(i)
                _392 = _391 + -1
                _393 = mdata_wch4[_392]
                conch4 = _f32(_390 * _393)
                D_13836 = _f32(pss)
                D_13837 = _f32(tss)
                _394 = __builtin_powf(D_13836, 7.13900029659271240234375e-1)
                _395 = conch4 * _394
                _396 = __builtin_powf(D_13837, -4.18500006198883056640625e-1)
                _397 = _int(i)
                _398 = _397 * 63
                _399 = _398 + -18
                _400 = _395 * _396
                model_densty[_399] = _400
                _401 = _int(i)
                _402 = _401 + -1
                _403 = mdata1_wair[_402]
                _404 = conjoe * _403
                _405 = _int(i)
                _406 = _405 + -1
                _407 = mdata_wn2o[_406]
                conn2o = _f32(_404 * _407)
                D_13838 = _f32(pss)
                D_13839 = _f32(tss)
                _408 = __builtin_powf(D_13838, 3.78300011157989501953125e-1)
                _409 = conn2o * _408
                _410 = __builtin_powf(D_13839, 9.39899981021881103515625e-1)
                _411 = _int(i)
                _412 = _411 * 63
                _413 = _412 + -17
                _414 = _409 * _410
                model_densty[_413] = _414
                D_13840 = _f32(pss)
                D_13841 = _f32(tss)
                _415 = __builtin_powf(D_13840, 7.20300018787384033203125e-1)
                _416 = conn2o * _415
                _417 = __builtin_powf(D_13841, -1.8359999358654022216796875e-1)
                _418 = _int(i)
                _419 = _418 * 63
                _420 = _419 + -16
                _421 = _416 * _417
                model_densty[_420] = _421
                D_13842 = _f32(pss)
                D_13843 = _f32(tss)
                _422 = __builtin_powf(D_13842, 7.76400029659271240234375e-1)
                _423 = conn2o * _422
                _424 = __builtin_powf(D_13843, 1.1930999755859375e+0)
                _425 = _int(i)
                _426 = _425 * 63
                _427 = _426 + -15
                _428 = _423 * _424
                model_densty[_427] = _428
                _429 = _int(i)
                _430 = _429 + -1
                _431 = mdata1_wair[_430]
                _432 = conjoe * _431
                _433 = _int(i)
                _434 = _433 + -1
                _435 = mdata_wo2[_434]
                cono2 = _f32(_432 * _435)
                D_13844 = _f32(pss)
                D_13845 = _f32(tss)
                _436 = __builtin_powf(D_13844, 1.18789994716644287109375e+0)
                _437 = cono2 * _436
                _438 = __builtin_powf(D_13845, 2.9737999439239501953125e+0)
                _439 = _int(i)
                _440 = _439 * 63
                _441 = _440 + -14
                _442 = _437 * _438
                model_densty[_441] = _442
                D_13846 = _f32(pss)
                D_13847 = _f32(tss)
                _443 = __builtin_powf(D_13846, 9.3529999256134033203125e-1)
                _444 = cono2 * _443
                _445 = __builtin_powf(D_13847, 1.93599998950958251953125e-1)
                _446 = _int(i)
                _447 = _446 * 63
                _448 = _447 + -13
                _449 = _444 * _445
                model_densty[_448] = _449
                _450 = _int(i)
                _451 = _450 + -1
                _452 = mdata1_wair[_451]
                _453 = conjoe * _452
                _454 = _int(i)
                _455 = _454 + -1
                _456 = mdata1_wnh3[_455]
                connh3 = _f32(_453 * _456)
                D_13848 = _f32(pss)
                D_13849 = _f32(tss)
                _457 = __builtin_powf(D_13848, 8.02299976348876953125e-1)
                _458 = connh3 * _457
                _459 = __builtin_powf(D_13849, -9.11099970340728759765625e-1)
                _460 = _int(i)
                _461 = _460 * 63
                _462 = _461 + -12
                _463 = _458 * _459
                model_densty[_462] = _463
                D_13850 = _f32(pss)
                D_13851 = _f32(tss)
                _464 = __builtin_powf(D_13850, 6.967999935150146484375e-1)
                _465 = connh3 * _464
                _466 = __builtin_powf(D_13851, 3.3770000934600830078125e-1)
                _467 = _int(i)
                _468 = _467 * 63
                _469 = _468 + -11
                _470 = _465 * _466
                model_densty[_469] = _470
                _471 = _int(i)
                _472 = _471 + -1
                _473 = mdata1_wair[_472]
                _474 = conjoe * _473
                _475 = _int(i)
                _476 = _475 + -1
                _477 = mdata1_wno[_476]
                conno = _f32(_474 * _477)
                D_13852 = _f32(pss)
                D_13853 = _f32(tss)
                _478 = __builtin_powf(D_13852, 5.264999866485595703125e-1)
                _479 = conno * _478
                _480 = __builtin_powf(D_13853, -4.70200002193450927734375e-1)
                _481 = _int(i)
                _482 = _481 * 63
                _483 = _482 + -10
                _484 = _479 * _480
                model_densty[_483] = _484
                _485 = _int(i)
                _486 = _485 + -1
                _487 = mdata1_wair[_486]
                _488 = conjoe * _487
                _489 = _int(i)
                _490 = _489 + -1
                _491 = mdata1_wno2[_490]
                conno2 = _f32(_488 * _491)
                D_13854 = _f32(pss)
                D_13855 = _f32(tss)
                _492 = __builtin_powf(D_13854, 3.955999910831451416015625e-1)
                _493 = conno2 * _492
                _494 = __builtin_powf(D_13855, -5.449999868869781494140625e-2)
                _495 = _int(i)
                _496 = _495 * 63
                _497 = _496 + -9
                _498 = _493 * _494
                model_densty[_497] = _498
                _499 = _int(i)
                _500 = _499 + -1
                _501 = mdata1_wair[_500]
                _502 = conjoe * _501
                _503 = _int(i)
                _504 = _503 + -1
                _505 = mdata1_wso2[_504]
                conso2 = _f32(_502 * _505)
                D_13856 = _f32(pss)
                D_13857 = _f32(tss)
                _506 = __builtin_powf(D_13856, 2.942999899387359619140625e-1)
                _507 = conso2 * _506
                _508 = __builtin_powf(D_13857, 1.2316000461578369140625e+0)
                _509 = _int(i)
                _510 = _509 * 63
                _511 = _510 + -8
                _512 = _507 * _508
                model_densty[_511] = _512
                D_13858 = _f32(pss)
                D_13859 = _f32(tss)
                _513 = __builtin_powf(D_13858, 2.134999930858612060546875e-1)
                _514 = conso2 * _513
                _515 = __builtin_powf(D_13859, 7.3299996554851531982421875e-2)
                _516 = _int(i)
                _517 = _516 * 63
                _518 = _517 + -7
                _519 = _514 * _515
                model_densty[_518] = _519
                _520 = f1 * 8.29999983310699462890625e-1
                _521 = _520 + 1.0e+0
                _522 = _521
                _523 = _int(i)
                _524 = _523 * 63
                _525 = _524 + -6
                _526 = cono2 * _522
                model_densty[_525] = _526
                _527 = _int(i)
                _528 = _527 * 63
                _529 = _528 + -5
                model_densty[_529] = 0.0
                _530 = _int(i)
                _531 = _530 * 63
                _532 = _531 + -4
                model_densty[_532] = 0.0
                rv_565_533 = rv[0]
                _534 = wtemp * rv_565_533
                ppw = _f32(tt * _534)
                _535 = card4_v1[0]
                _536 = card4_v2[0]
                _537 = _535 + _536
                _538 = _537
                avw = _f32(_538 * 5.0e-1)
                b1_566_539 = b1[0]
                _540 = _div(avw, b1_566_539)
                D_13860 = _f32(_540)
                D_13861 = _f32(D_13860 * D_13860)
                b2_567_541 = b2[0]
                _542 = _div(avw, b2_567_541)
                D_13862 = _f32(_542)
                D_13863 = _f32(D_13862 * D_13862)
                c1_568_543 = c1[0]
                _544 = _div(avw, c1_568_543)
                D_13864 = _f32(_544)
                D_13865 = _f32(D_13864 * D_13864)
                a1_569_545 = a1[0]
                _546 = 1.0e+0 - D_13861
                _547 = _546
                _548 = _div(a1_569_545, _547)
                a0_570_549 = a0[0]
                _550 = _548 + a0_570_549
                a2_571_551 = a2[0]
                _552 = 1.0e+0 - D_13863
                _553 = _552
                _554 = _div(a2_571_551, _553)
                _555 = _550 + _554
                _556 = _555
                pzero_572_557 = pzero[0]
                _558 = _div(pp, pzero_572_557)
                _559 = _558
                _560 = _556 * _559
                tzero_573_561 = tzero[0]
                _562 = tzero_573_561 + 1.5e+1
                _563 = _562
                _564 = _560 * _563
                _565 = _div(_564, tt)
                c0_574_566 = c0[0]
                _567 = c0_574_566 - D_13865
                _568 = _567
                _569 = ppw * _568
                pzero_575_570 = pzero[0]
                _571 = _div(_569, pzero_575_570)
                _572 = _565 - _571
                _573 = _572
                _574 = _int(i)
                _575 = _574 + -1
                _576 = _573 * 9.999999974752427078783512115478515625e-7
                model_rfndx[_575] = _576
                _pc = 14
            case 14:  # L.855
                i = _int(i + 1)
                _pc = 1
                continue
            case 15:  # L.856
                _577 = ifil_npr[0]
                _pc = 16 if _577 == 1 else 17
                continue
            case 16:  # <D.19601>
                _pc = 26
                continue
            case 17:  # L.862
                D_13869 = _int(cntrl_ml[0])
                i = _int(1)
                _pc = 18
            case 18:  # <D.19603>
                D_13872 = _int(i > D_13869)
                _pc = 20 if D_13872 != 0 else 19
                continue
            case 19:  # L.863
                i = _int(i + 1)
                _pc = 18
                continue
            case 20:  # L.864
                D_13874 = _int(cntrl_ml[0])
                i = _int(1)
                _pc = 21
            case 21:  # <D.19605>
                D_13877 = _int(i > D_13874)
                _pc = 23 if D_13877 != 0 else 22
                continue
            case 22:  # L.865
                i = _int(i + 1)
                _pc = 21
                continue
            case 23:  # L.866
                D_13879 = _int(cntrl_ml[0])
                i = _int(1)
                _pc = 24
            case 24:  # <D.19607>
                D_13882 = _int(i > D_13879)
                _pc = 26 if D_13882 != 0 else 25
                continue
            case 25:  # L.867
                i = _int(i + 1)
                _pc = 24
                continue
            case 26:  # __label_000040
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_subsol(_state, thetas, phis, time, iday):
    dec = _state.view(180672, '<f4')
    eqt = _state.view(180544, '<f4')
    nday = _state.view(180416, '<i4')
    decang = _ZERO32
    eqtime = _ZERO32
    i = 0
    D_13947 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = iday[0]
                _2 = _1 <= 0
                _3 = iday[0]
                _4 = _3 > 366
                _5 = _2 | _4
                _pc = 1 if _5 != 0 else 2
                continue
            case 1:  # <D.19610>
                _pc = 16
                continue
            case 2:  # L.869
                _6 = time[0]
                _7 = _6 < 0.0
                _8 = time[0]
                _9 = _8 > 2.4e+1
                _10 = _7 | _9
                _pc = 3 if _10 != 0 else 4
                continue
            case 3:  # <D.19612>
                _pc = 17
                continue
            case 4:  # L.870
                i = _int(1)
                _pc = 5
            case 5:  # <D.19614>
                D_13947 = _int(i > 25)
                _pc = 11 if D_13947 != 0 else 6
                continue
            case 6:  # <D.19615>
                _11 = _int(i)
                _12 = _11 + -1
                _13 = nday[_12]
                _14 = iday[0]
                _pc = 7 if _13 == _14 else 8
                continue
            case 7:  # <D.19616>
                _pc = 12
                continue
            case 8:  # __label_000010
                _15 = _int(i)
                _16 = _15 + -1
                _17 = nday[_16]
                _18 = iday[0]
                _pc = 9 if _17 > _18 else 10
                continue
            case 9:  # <D.19618>
                _pc = 11
                continue
            case 10:  # L.871
                i = _int(i + 1)
                _pc = 5
                continue
            case 11:  # __label_000020
                i = _int(i + -1)
                _19 = _int(i)
                _20 = _19 + -1
                _21 = eqt[_20]
                _22 = i + 1
                _23 = _int(_22)
                _24 = _23 + -1
                _25 = eqt[_24]
                _26 = _int(i)
                _27 = _26 + -1
                _28 = eqt[_27]
                _29 = _25 - _28
                _30 = _29
                _31 = iday[0]
                _32 = _int(i)
                _33 = _32 + -1
                _34 = nday[_33]
                _35 = _31 - _34
                _36 = _f32(_35)
                _37 = _30 * _36
                _38 = i + 1
                _39 = _int(_38)
                _40 = _39 + -1
                _41 = nday[_40]
                _42 = _int(i)
                _43 = _42 + -1
                _44 = nday[_43]
                _45 = _41 - _44
                _46 = _f32(_45)
                _47 = _div(_37, _46)
                eqtime = _f32(_21 + _47)
                _48 = _int(i)
                _49 = _48 + -1
                _50 = dec[_49]
                _51 = i + 1
                _52 = _int(_51)
                _53 = _52 + -1
                _54 = dec[_53]
                _55 = _int(i)
                _56 = _55 + -1
                _57 = dec[_56]
                _58 = _54 - _57
                _59 = _58
                _60 = iday[0]
                _61 = _int(i)
                _62 = _61 + -1
                _63 = nday[_62]
                _64 = _60 - _63
                _65 = _f32(_64)
                _66 = _59 * _65
                _67 = i + 1
                _68 = _int(_67)
                _69 = _68 + -1
                _70 = nday[_69]
                _71 = _int(i)
                _72 = _71 + -1
                _73 = nday[_72]
                _74 = _70 - _73
                _75 = _f32(_74)
                _76 = _div(_66, _75)
                decang = _f32(_50 + _76)
                _pc = 13
                continue
            case 12:  # __label_000030
                _77 = _int(i)
                _78 = _77 + -1
                eqtime = _f32(eqt[_78])
                _79 = _int(i)
                _80 = _79 + -1
                decang = _f32(dec[_80])
                _pc = 13
            case 13:  # __label_000040
                thetas[0] = decang
                eqtime = _f32(_div(eqtime, 6.0e+1))
                _81 = time[0]
                _82 = eqtime + _81
                _83 = _82
                _84 = _83 * 1.5e+1
                _85 = _84 - 1.8e+2
                phis[0] = _85
                _86 = phis[0]
                _pc = 14 if _86 < 0.0 else 15
                continue
            case 14:  # <D.19620>
                _87 = phis[0]
                _88 = _87 + 3.6e+2
                phis[0] = _88
                _pc = 15
                continue
            case 15:  # L.875
                return
            case 16:  # __label_000901
                _gfortran_stop_string(0, 0, 0)
                _pc = 17
            case 17:  # __label_000902
                _gfortran_stop_string(0, 0, 0)
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_rdexa(_state, python):
    card2d_ireg = _state.view(214080, '<i4')
    ihc = 0
    D_14023 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 1
            case 1:  # __label_001210
                ihc = _int(1)
                _pc = 2
            case 2:  # <D.19624>
                D_14023 = _int(ihc > 4)
                _pc = -1 if D_14023 != 0 else 3
                continue
            case 3:  # <D.19625>
                _1 = _int(ihc)
                _2 = _1 + -1
                _3 = card2d_ireg[_2]
                _pc = 4 if _3 == 0 else 5
                continue
            case 4:  # <D.19626>
                _pc = 9
                continue
            case 5:  # L.878
                _4 = python[0]
                _5 = not _4
                _pc = 6 if _5 != 0 else 7
                continue
            case 6:  # <D.19628>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 7
            case 7:  # __label_001250
                _6 = python[0]
                _7 = not _6
                _pc = 8 if _7 != 0 else 9
                continue
            case 8:  # <D.19630>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 9
            case 9:  # L.876
                ihc = _int(ihc + 1)
                _pc = 2
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_cirrus(_state, cthik, calt, iseed, cprob, cext):
    _pc = 0
    while True:
        match _pc:
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_ranfun(_state):
    D_19681 = _ZERO32
    __result_ranfun = _zeros(1, '<f4')
    _gfortran_random_r4(__result_ranfun)
    D_19681 = _f32(__result_ranfun[0])
    return D_19681


def _ft_aernsm(_state, jprt, gndalt, python):
    __BLNK___relhum = _state.view(265568, '<f4')
    __BLNK___whno3 = _state.view(265704, '<f4')
    __BLNK___ich = _state.view(265840, '<i4')
    __BLNK___absc = _state.view(283836, '<f4')
    __BLNK___extc = _state.view(284776, '<f4')
    card1_model = _state.view(209568, '<i4')
    card1_m1 = _state.view(209580, '<i4')
    card1_m2 = _state.view(209584, '<i4')
    card1_m3 = _state.view(209588, '<i4')
    card1_im = _state.view(209592, '<i4')
    card1a_m4 = _state.view(189424, '<i4')
    card1a_m5 = _state.view(189428, '<i4')
    card1a_m6 = _state.view(189432, '<i4')
    card1a_mdef = _state.view(189436, '<i4')
    card1a_ird1 = _state.view(189440, '<i4')
    card1a_ird2 = _state.view(189444, '<i4')
    card1b_junit = _state.view(209632, '<i4')
    card1b_wmol = _state.view(209692, '<f4')
    card1b_wair1 = _state.view(209740, '<f4')
    card1b_jlow = _state.view(209744, '<i4')
    card2_ihaze = _state.view(231744, '<i4')
    card2_iseasn = _state.view(231748, '<i4')
    card2_ivulcn = _state.view(231752, '<i4')
    card2_icstl = _state.view(231756, '<i4')
    card2_icld = _state.view(231760, '<i4')
    card2_ivsa = _state.view(231764, '<i4')
    card2_vis = _state.view(231768, '<f4')
    card2_wss = _state.view(231772, '<f4')
    card2_whh = _state.view(231776, '<f4')
    card2_rainrt = _state.view(231780, '<f4')
    card2a_cthik = _state.view(209616, '<f4')
    card2a_calt = _state.view(209620, '<f4')
    card2a_cext = _state.view(209624, '<f4')
    card2d_ireg = _state.view(214080, '<i4')
    card2d_altb = _state.view(214096, '<f4')
    card2d_iregc = _state.view(214112, '<i4')
    cntrl_ml = _state.view(245616, '<i4')
    mart_rhh = _state.view(241568, '<f4')
    mdata_z = _state.view(149120, '<f4')
    mdata_p = _state.view(149320, '<f4')
    mdata_t = _state.view(149520, '<f4')
    mdata_wh = _state.view(149720, '<f4')
    mdata_wco2 = _state.view(149920, '<f4')
    mdata_wo = _state.view(150120, '<f4')
    mdata_wn2o = _state.view(150320, '<f4')
    mdata_wco = _state.view(150520, '<f4')
    mdata_wch4 = _state.view(150720, '<f4')
    mdata_wo2 = _state.view(150920, '<f4')
    mdata1_wno = _state.view(286880, '<f4')
    mdata1_wso2 = _state.view(287080, '<f4')
    mdata1_wno2 = _state.view(287280, '<f4')
    mdata1_wnh3 = _state.view(287480, '<f4')
    mdata1_wair = _state.view(287680, '<f4')
    mdlz_hmdlz = _state.view(231808, '<f4')
    model_zmdl = _state.view(231904, '<f4')
    model_densty = _state.view(232448, '<f4')
    model_cldamt = _state.view(241016, '<f4')
    model_rramt = _state.view(241152, '<f4')
    model_hazec = _state.view(241424, '<f4')
    titl_hz = _state.view(59392, 'S4')
    titl_seasn = _state.view(59712, 'S4')
    titl_blank = _state.view(59912, 'S4')
    zvsaly_zvsa = _state.view(245664, '<f4')
    zvsaly_rhvsa = _state.view(245704, '<f4')
    zvsaly_ahvsa = _state.view(245744, '<f4')
    zvsaly_ihvsa = _state.view(245784, '<i4')
    ahahol = _state.view(181056, 'S4')
    ahlvsa = _state.view(181328, 'S4')
    ahus = _state.view(181360, 'S4')
    cldtop = _state.view(180992, '<f4')
    ahast = _zeros(34, '<f4')
    ahaze = _zeros(1, '<f4')
    ahol1 = _zeros(5, 'S4')
    ahol2 = _zeros(5, 'S4')
    ahol3 = _zeros(5, 'S4')
    asc = _ZERO32
    bl = _zeros(1, 'S1')
    cld0 = _ZERO32
    cld1 = _ZERO32
    cld2 = _ZERO32
    cldd = _ZERO32
    con = _ZERO32
    eqlwcz = _zeros(1, '<f4')
    fac = _ZERO32
    haz1 = _zeros(1, '<f4')
    haz2 = _zeros(1, '<f4')
    haze = _ZERO32
    hhol = _zeros(5, 'S4')
    i = 0
    ic1 = _zeros(1, '<i4')
    ichr = 0
    icl = 0
    icld1 = _zeros(1, '<i4')
    icldc = 0
    icldl = 0
    iclds = 0
    iconv = 0
    idsr = 0
    ih1 = _zeros(34, '<i4')
    iha1 = _zeros(1, '<i4')
    ihh = 0
    ii = 0
    ij = 0
    ird0 = 0
    is1 = _zeros(34, '<i4')
    isea1 = _zeros(1, '<i4')
    ity1 = _zeros(34, '<i4')
    ityaer = 0
    ivl1 = _zeros(34, '<i4')
    ivul1 = _zeros(1, '<i4')
    j = _zeros(1, '<i4')
    jchar = _zeros(15, 'S1')
    k = _zeros(1, '<i4')
    kk = 0
    km = 0
    l = _zeros(1, '<i4')
    n = 0
    nn = _zeros(1, '<i4')
    rh = _zeros(1, '<f4')
    rratz = _zeros(1, '<f4')
    t0 = _ZERO32
    ta = _ZERO32
    ts = _ZERO32
    vis1 = _zeros(1, '<f4')
    wtemp = _ZERO32
    zgn = _zeros(34, '<f4')
    zsc = _ZERO32
    D_14710 = 0
    D_14713 = 0
    D_14717 = 0
    D_14723 = 0
    D_14726 = 0
    D_14729 = 0
    D_14752 = 0
    C_14775 = _array([1], '<i4')
    C_14781 = _array([2], '<i4')
    a_39 = _ZERO32
    a_40 = _ZERO32
    D_14937 = _ZERO32
    D_14946 = 0
    D_14953 = 0
    D_14956 = 0
    D_14959 = 0
    D_14968 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                card2d_iregc[0] = 0
                card2d_iregc[1] = 0
                card2d_iregc[2] = 0
                card2d_iregc[3] = 0
                iconv = _int(1)
                ird0 = _int(1)
                icldl = _int(card2_icld[0])
                _1 = card1_model[0]
                _2 = _f32(_1)
                _3 = _2 == 0.0
                _4 = card1_model[0]
                _5 = _4 == 7
                _6 = _3 | _5
                _pc = 1 if _6 != 0 else 4
                continue
            case 1:  # <D.19684>
                _7 = card1_im[0]
                _pc = 2 if _7 != 1 else 3
                continue
            case 2:  # <D.19686>
                return
            case 3:  # L.906
                _pc = 4
                continue
            case 4:  # L.905
                _8 = card1_model[0]
                _9 = _f32(_8)
                _10 = _9 > 0.0
                _11 = card1_model[0]
                _12 = _11 <= 6
                _13 = _10 & _12
                _pc = 5 if _13 != 0 else 6
                continue
            case 5:  # <D.19689>
                ird0 = _int(0)
                _pc = 6
                continue
            case 6:  # L.907
                _14 = ird0 == 1
                _15 = card2_ivsa[0]
                _16 = _15 == 1
                _17 = _14 & _16
                _pc = 7 if _17 != 0 else 13
                continue
            case 7:  # <D.19692>
                ird0 = _int(0)
                card1a_ird1[0] = 0
                card1a_ird2[0] = 0
                iconv = _int(0)
                _18 = cntrl_ml[0]
                _19 = _18 + 10
                _20 = card1b_jlow[0]
                _21 = _19 - _20
                cntrl_ml[0] = _21
                _22 = cntrl_ml[0]
                _pc = 8 if _22 > 34 else 9
                continue
            case 8:  # <D.19694>
                cntrl_ml[0] = 34
                _pc = 9
                continue
            case 9:  # L.909
                _23 = zvsaly_zvsa[8]
                _24 = _23 + 9.99999977648258209228515625e-3
                zvsaly_zvsa[9] = _24
                zvsaly_rhvsa[9] = 0.0
                zvsaly_ahvsa[9] = 0.0
                zvsaly_ihvsa[9] = 0
                _pc = 10
            case 10:  # __label_000900
                _25 = card1_model[0]
                _pc = 11 if _25 == 0 else 12
                continue
            case 11:  # <D.19697>
                _gfortran_stop_string(0, 0, 0)
                _pc = 12
            case 12:  # __label_000910
                _pc = 13
                continue
            case 13:  # L.908
                icl = _int(0)
                idsr = _int(0)
                _26 = card2_icld[0]
                _27 = _26 == 18
                _28 = card2_icld[0]
                _29 = _28 == 19
                _30 = _27 | _29
                _pc = 14 if _30 != 0 else 17
                continue
            case 14:  # <D.19700>
                _ft_cirr18(_state)
                _31 = card2a_cthik[0]
                cldd = _f32(_31 * 1.00000001490116119384765625e-1)
                _32 = card2a_calt[0]
                _33 = cldd * 5.0e-1
                cld0 = _f32(_32 - _33)
                _pc = 15 if cld0 <= 0.0 else 16
                continue
            case 15:  # <D.19702>
                cld0 = _f32(0.0)
                _pc = 16
                continue
            case 16:  # L.912
                cld1 = _f32(cld0 + cldd)
                _34 = card2a_cthik[0]
                _35 = cld1 + _34
                cld2 = _f32(_35 - cldd)
                _pc = 17
                continue
            case 17:  # L.911
                _ft_flayz(_state, cntrl_ml, card1_model, card2_icld, model_zmdl, gndalt, card2_ivsa)
                jprt[0] = 1
                _36 = card1_model[0]
                _37 = _36 == 0
                _38 = card1_model[0]
                _39 = _38 == 7
                _40 = _37 | _39
                _pc = 18 if _40 != 0 else 19
                continue
            case 18:  # <D.19706>
                jprt[0] = 0
                _pc = 19
                continue
            case 19:  # L.913
                _41 = card2_ivsa[0]
                _pc = 20 if _41 == 1 else 21
                continue
            case 20:  # <D.19709>
                jprt[0] = 0
                _pc = 21
                continue
            case 21:  # L.914
                _42 = card2_icld[0]
                _43 = _42 > 0
                _44 = card2_icld[0]
                _45 = _44 <= 19
                _46 = _43 & _45
                _pc = 22 if _46 != 0 else 23
                continue
            case 22:  # <D.19712>
                jprt[0] = 0
                _pc = 23
                continue
            case 23:  # L.915
                _47 = card2_rainrt[0]
                _pc = 24 if _47 > 0.0 else 25
                continue
            case 24:  # <D.19715>
                jprt[0] = 0
                _pc = 25
                continue
            case 25:  # L.916
                _48 = gndalt[0]
                _pc = 26 if _48 > 0.0 else 27
                continue
            case 26:  # <D.19718>
                jprt[0] = 0
                _pc = 27
                continue
            case 27:  # L.917
                D_14710 = _int(cntrl_ml[0])
                i = _int(1)
                _pc = 28
            case 28:  # <D.19721>
                D_14713 = _int(i > D_14710)
                _pc = 31 if D_14713 != 0 else 29
                continue
            case 29:  # <D.19722>
                _49 = _int(i)
                _50 = _49 + -1
                model_hazec[_50] = 0.0
                _pc = 30
            case 30:  # L.918
                i = _int(i + 1)
                _pc = 28
                continue
            case 31:  # L.919
                ii = _int(1)
                _pc = 32
            case 32:  # <D.19723>
                D_14717 = _int(ii > 4)
                _pc = 35 if D_14717 != 0 else 33
                continue
            case 33:  # __label_000006
                _51 = _int(ii)
                _52 = _51 + -1
                card2d_altb[_52] = 0.0
                _pc = 34
            case 34:  # L.920
                ii = _int(ii + 1)
                _pc = 32
                continue
            case 35:  # L.921
                t0 = _f32(2.73149993896484375e+2)
                ic1[0] = 1
                n = _int(7)
                _53 = card2_ivulcn[0]
                _pc = 36 if _53 <= 0 else 37
                continue
            case 36:  # <D.19725>
                card2_ivulcn[0] = 1
                _pc = 37
                continue
            case 37:  # L.922
                _54 = card2_iseasn[0]
                _pc = 38 if _54 <= 0 else 39
                continue
            case 38:  # <D.19728>
                card2_iseasn[0] = 1
                _pc = 39
                continue
            case 39:  # L.923
                _55 = jprt[0]
                _pc = 40 if _55 == 0 else 41
                continue
            case 40:  # __label_000094
                _pc = 41
                continue
            case 41:  # L.924
                D_14723 = _int(cntrl_ml[0])
                k[0] = 1
                _pc = 42
            case 42:  # <D.19734>
                k_576_56 = k[0]
                D_14726 = _int(D_14723 < k_576_56)
                _pc = 286 if D_14726 != 0 else 43
                continue
            case 43:  # <D.19735>
                rh[0] = 0.0
                k_577_57 = k[0]
                _58 = _int(k_577_57)
                _59 = _58 + -1
                mdata_wh[_59] = 0.0
                k_578_60 = k[0]
                _61 = _int(k_578_60)
                _62 = _61 + -1
                mdata_wo[_62] = 0.0
                iha1[0] = 0
                icld1[0] = 0
                isea1[0] = 0
                ivul1[0] = 0
                vis1[0] = 0.0
                ahaze[0] = 0.0
                eqlwcz[0] = 0.0
                rratz[0] = 0.0
                ichr = _int(0)
                k_579_63 = k[0]
                _64 = _int(k_579_63)
                _65 = _64 + -1
                mdata1_wair[_65] = 0.0
                k_580_66 = k[0]
                _67 = _int(k_580_66)
                _68 = _67 + -1
                mdata_wco2[_68] = 0.0
                k_581_69 = k[0]
                _70 = _int(k_581_69)
                _71 = _70 + -1
                mdata_wco[_71] = 0.0
                k_582_72 = k[0]
                _73 = _int(k_582_72)
                _74 = _73 + -1
                mdata_wch4[_74] = 0.0
                k_583_75 = k[0]
                _76 = _int(k_583_75)
                _77 = _76 + -1
                mdata_wn2o[_77] = 0.0
                k_584_78 = k[0]
                _79 = _int(k_584_78)
                _80 = _79 + -1
                mdata_wo2[_80] = 0.0
                k_585_81 = k[0]
                _82 = _int(k_585_81)
                _83 = _82 + -1
                mdata1_wnh3[_83] = 0.0
                k_586_84 = k[0]
                _85 = _int(k_586_84)
                _86 = _85 + -1
                mdata1_wno[_86] = 0.0
                k_587_87 = k[0]
                _88 = _int(k_587_87)
                _89 = _88 + -1
                mdata1_wno2[_89] = 0.0
                k_588_90 = k[0]
                _91 = _int(k_588_90)
                _92 = _91 + -1
                mdata1_wso2[_92] = 0.0
                k_589_93 = k[0]
                _94 = _int(k_589_93)
                _95 = _94 + -1
                __BLNK___whno3[_95] = 0.0
                km = _int(1)
                _pc = 44
            case 44:  # <D.19736>
                D_14729 = _int(km > 15)
                _pc = 50 if D_14729 != 0 else 45
                continue
            case 45:  # <D.19737>
                _96 = _int(km)
                _97 = _96 + -1
                jchar[_97:].view("u1")[1 - 1] = 32
                _pc = 46 if km > 12 else 47
                continue
            case 46:  # <D.19738>
                _pc = 49
                continue
            case 47:  # L.929
                _98 = python[0]
                _99 = not _98
                _pc = 48 if _99 != 0 else 49
                continue
            case 48:  # <D.19740>
                _100 = _int(km)
                _101 = _100 + -1
                card1b_wmol[_101] = 0.0
                _pc = 49
                continue
            case 49:  # L.927
                km = _int(km + 1)
                _pc = 44
                continue
            case 50:  # L.928
                _pc = 51 if ird0 == 1 else 54
                continue
            case 51:  # <D.19743>
                _102 = python[0]
                _103 = not _102
                _pc = 52 if _103 != 0 else 53
                continue
            case 52:  # <D.19745>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 53
            case 53:  # __label_000081
                _pc = 54
                continue
            case 54:  # L.931
                _104 = card1a_ird1[0]
                _pc = 55 if _104 == 1 else 58
                continue
            case 55:  # <D.19748>
                _105 = python[0]
                _106 = not _105
                _pc = 56 if _106 != 0 else 57
                continue
            case 56:  # <D.19750>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 57
            case 57:  # __label_000084
                _pc = 58
                continue
            case 58:  # L.933
                _107 = card1a_ird2[0]
                _pc = 59 if _107 == 1 else 62
                continue
            case 59:  # <D.19753>
                _108 = python[0]
                _109 = not _108
                _pc = 60 if _109 != 0 else 61
                continue
            case 60:  # <D.19755>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 61
            case 61:  # __label_000082
                _pc = 64
                continue
            case 62:  # <D.19754>
                _110 = card2_rainrt[0]
                rratz[0] = _110
                k_590_111 = k[0]
                _112 = _int(k_590_111)
                _113 = _112 + -1
                _114 = model_zmdl[_113]
                _pc = 63 if _114 > 6.0e+0 else 64
                continue
            case 63:  # <D.19758>
                rratz[0] = 0.0
                _pc = 64
                continue
            case 64:  # L.935
                iclds = _int(icld1[0])
                _pc = 65 if ichr == 1 else 72
                continue
            case 65:  # <D.19761>
                iha1_591_115 = iha1[0]
                _pc = 66 if iha1_591_115 == 0 else 69
                continue
            case 66:  # <D.19763>
                icld1_592_116 = icld1[0]
                _pc = 67 if icld1_592_116 != 11 else 68
                continue
            case 67:  # <D.19765>
                ichr = _int(0)
                _pc = 68
                continue
            case 68:  # L.940
                _pc = 71
                continue
            case 69:  # <D.19764>
                iha1_593_117 = iha1[0]
                _pc = 70 if iha1_593_117 != 7 else 71
                continue
            case 70:  # <D.19769>
                ichr = _int(0)
                _pc = 71
                continue
            case 71:  # L.939
                _pc = 72
                continue
            case 72:  # L.938
                _118 = card1_model[0]
                _pc = 73 if _118 == 0 else 74
                continue
            case 73:  # <D.19773>
                k_594_119 = k[0]
                _120 = _int(k_594_119)
                _121 = _120 + -1
                _122 = model_zmdl[_121]
                mdlz_hmdlz[0] = _122
                k_595_123 = k[0]
                _124 = _int(k_595_123)
                _125 = _124 + -1
                _126 = mdata_p[_125]
                mdlz_hmdlz[1] = _126
                k_596_127 = k[0]
                _128 = _int(k_596_127)
                _129 = _128 + -1
                _130 = mdata_t[_129]
                mdlz_hmdlz[2] = _130
                _131 = card1b_wmol[0]
                mdlz_hmdlz[3] = _131
                _132 = card1b_wmol[1]
                mdlz_hmdlz[4] = _132
                _133 = card1b_wmol[2]
                mdlz_hmdlz[5] = _133
                ahaze_597_134 = ahaze[0]
                mdlz_hmdlz[6] = ahaze_597_134
                _pc = 74
                continue
            case 74:  # L.942
                km = _int(1)
                _pc = 75
            case 75:  # <D.19776>
                D_14752 = _int(km > 15)
                _pc = 79 if D_14752 != 0 else 76
                continue
            case 76:  # __label_000012
                _135 = python[0]
                _136 = not _135
                _pc = 77 if _136 != 0 else 78
                continue
            case 77:  # <D.19778>
                _137 = _int(km)
                _138 = _137 + -1
                _139 = jchar[_138:]
                _140 = _int(km)
                _141 = _140 + -1
                _142 = _ft_jou(_state, _139, 1)
                card1b_junit[_141] = _142
                _pc = 78
                continue
            case 78:  # L.943
                km = _int(km + 1)
                _pc = 75
                continue
            case 79:  # L.944
                _pc = 80 if ird0 == 0 else 81
                continue
            case 80:  # <D.19781>
                _143 = card1_m1[0]
                card1b_junit[0] = _143
                _144 = card1_m1[0]
                card1b_junit[1] = _144
                _145 = card1_m2[0]
                card1b_junit[2] = _145
                card1b_junit[3] = 6
                _146 = card1_m3[0]
                card1b_junit[4] = _146
                _147 = card1a_m5[0]
                card1b_junit[5] = _147
                _148 = card1a_m6[0]
                card1b_junit[6] = _148
                _149 = card1a_m4[0]
                card1b_junit[7] = _149
                card1b_junit[8] = 6
                card1b_junit[9] = 6
                card1b_junit[10] = 6
                card1b_junit[11] = 6
                card1b_junit[12] = 6
                card1b_junit[13] = 6
                card1b_junit[14] = 6
                _pc = 109
                continue
            case 81:  # <D.19782>
                bl.view("u1")[1 - 1] = 32
                _150 = card1_m1[0]
                _151 = _150 > 0
                _152 = _read_char(jchar[0:], 1 - 1)
                _153 = _read_char(bl, 1 - 1)
                _154 = _152 == _153
                _155 = _151 & _154
                _pc = 82 if _155 != 0 else 83
                continue
            case 82:  # <D.19784>
                _156 = card1_m1[0]
                card1b_junit[0] = _156
                _pc = 83
                continue
            case 83:  # L.947
                _157 = card1_m1[0]
                _158 = _157 > 0
                _159 = _read_char(jchar[1:], 1 - 1)
                _160 = _read_char(bl, 1 - 1)
                _161 = _159 == _160
                _162 = _158 & _161
                _pc = 84 if _162 != 0 else 85
                continue
            case 84:  # <D.19787>
                _163 = card1_m1[0]
                card1b_junit[1] = _163
                _pc = 85
                continue
            case 85:  # L.948
                _164 = card1_m2[0]
                _165 = _164 > 0
                _166 = _read_char(jchar[2:], 1 - 1)
                _167 = _read_char(bl, 1 - 1)
                _168 = _166 == _167
                _169 = _165 & _168
                _pc = 86 if _169 != 0 else 87
                continue
            case 86:  # <D.19790>
                _170 = card1_m2[0]
                card1b_junit[2] = _170
                _pc = 87
                continue
            case 87:  # L.949
                _171 = card1a_mdef[0]
                _172 = _171 > 0
                _173 = _read_char(jchar[3:], 1 - 1)
                _174 = _read_char(bl, 1 - 1)
                _175 = _173 == _174
                _176 = _172 & _175
                _pc = 88 if _176 != 0 else 89
                continue
            case 88:  # <D.19793>
                card1b_junit[3] = 6
                _pc = 89
                continue
            case 89:  # L.950
                _177 = card1_m3[0]
                _178 = _177 > 0
                _179 = _read_char(jchar[4:], 1 - 1)
                _180 = _read_char(bl, 1 - 1)
                _181 = _179 == _180
                _182 = _178 & _181
                _pc = 90 if _182 != 0 else 91
                continue
            case 90:  # <D.19796>
                _183 = card1_m3[0]
                card1b_junit[4] = _183
                _pc = 91
                continue
            case 91:  # L.951
                _184 = card1a_m5[0]
                _185 = _184 > 0
                _186 = _read_char(jchar[5:], 1 - 1)
                _187 = _read_char(bl, 1 - 1)
                _188 = _186 == _187
                _189 = _185 & _188
                _pc = 92 if _189 != 0 else 93
                continue
            case 92:  # <D.19799>
                _190 = card1a_m5[0]
                card1b_junit[5] = _190
                _pc = 93
                continue
            case 93:  # L.952
                _191 = card1a_m6[0]
                _192 = _191 > 0
                _193 = _read_char(jchar[6:], 1 - 1)
                _194 = _read_char(bl, 1 - 1)
                _195 = _193 == _194
                _196 = _192 & _195
                _pc = 94 if _196 != 0 else 95
                continue
            case 94:  # <D.19802>
                _197 = card1a_m6[0]
                card1b_junit[6] = _197
                _pc = 95
                continue
            case 95:  # L.953
                _198 = card1a_m4[0]
                _199 = _198 > 0
                _200 = _read_char(jchar[7:], 1 - 1)
                _201 = _read_char(bl, 1 - 1)
                _202 = _200 == _201
                _203 = _199 & _202
                _pc = 96 if _203 != 0 else 97
                continue
            case 96:  # <D.19805>
                _204 = card1a_m4[0]
                card1b_junit[7] = _204
                _pc = 97
                continue
            case 97:  # L.954
                _205 = card1a_mdef[0]
                _206 = _205 > 0
                _207 = _read_char(jchar[8:], 1 - 1)
                _208 = _read_char(bl, 1 - 1)
                _209 = _207 == _208
                _210 = _206 & _209
                _pc = 98 if _210 != 0 else 99
                continue
            case 98:  # <D.19808>
                card1b_junit[8] = 6
                _pc = 99
                continue
            case 99:  # L.955
                _211 = card1a_mdef[0]
                _212 = _211 > 0
                _213 = _read_char(jchar[9:], 1 - 1)
                _214 = _read_char(bl, 1 - 1)
                _215 = _213 == _214
                _216 = _212 & _215
                _pc = 100 if _216 != 0 else 101
                continue
            case 100:  # <D.19811>
                card1b_junit[9] = 6
                _pc = 101
                continue
            case 101:  # L.956
                _217 = card1a_mdef[0]
                _218 = _217 > 0
                _219 = _read_char(jchar[10:], 1 - 1)
                _220 = _read_char(bl, 1 - 1)
                _221 = _219 == _220
                _222 = _218 & _221
                _pc = 102 if _222 != 0 else 103
                continue
            case 102:  # <D.19814>
                card1b_junit[10] = 6
                _pc = 103
                continue
            case 103:  # L.957
                _223 = card1a_mdef[0]
                _224 = _223 > 0
                _225 = _read_char(jchar[11:], 1 - 1)
                _226 = _read_char(bl, 1 - 1)
                _227 = _225 == _226
                _228 = _224 & _227
                _pc = 104 if _228 != 0 else 105
                continue
            case 104:  # <D.19817>
                card1b_junit[11] = 6
                _pc = 105
                continue
            case 105:  # L.958
                _229 = card1a_mdef[0]
                _230 = _229 > 0
                _231 = _read_char(jchar[12:], 1 - 1)
                _232 = _read_char(bl, 1 - 1)
                _233 = _231 == _232
                _234 = _230 & _233
                _pc = 106 if _234 != 0 else 107
                continue
            case 106:  # <D.19820>
                card1b_junit[12] = 6
                _pc = 107
                continue
            case 107:  # L.959
                _235 = card1a_mdef[0]
                _236 = _235 > 0
                _237 = _read_char(jchar[13:], 1 - 1)
                _238 = _read_char(bl, 1 - 1)
                _239 = _237 == _238
                _240 = _236 & _239
                _pc = 108 if _240 != 0 else 109
                continue
            case 108:  # <D.19823>
                card1b_junit[13] = 6
                _pc = 109
                continue
            case 109:  # L.946
                _pc = 110 if iconv == 1 else 111
                continue
            case 110:  # <D.19826>
                k_598_241 = k[0]
                _242 = _int(k_598_241)
                _243 = _242 + -1
                _244 = mdata_p[_243:]
                _ft_check(_state, _244, card1b_junit[0:], C_14775)
                k_599_245 = k[0]
                _246 = _int(k_599_245)
                _247 = _246 + -1
                _248 = mdata_t[_247:]
                _ft_check(_state, _248, card1b_junit[1:], C_14781)
                k_600_249 = k[0]
                _250 = _int(k_600_249)
                _251 = _250 + -1
                _252 = mdata_t[_251:]
                k_601_253 = k[0]
                _254 = _int(k_601_253)
                _255 = _254 + -1
                _256 = mdata_p[_255:]
                k_602_257 = k[0]
                _258 = _int(k_602_257)
                _259 = _258 + -1
                _260 = model_zmdl[_259:]
                _ft_defalt(_state, _260, _256, _252)
                k_603_261 = k[0]
                _262 = _int(k_603_261)
                _263 = _262 + -1
                _264 = mdata_t[_263:]
                k_604_265 = k[0]
                _266 = _int(k_604_265)
                _267 = _266 + -1
                _268 = mdata_p[_267:]
                _ft_convrt(_state, _268, _264)
                k_605_269 = k[0]
                _270 = _int(k_605_269)
                _271 = _270 + -1
                _272 = card1b_wmol[0]
                mdata_wh[_271] = _272
                k_606_273 = k[0]
                _274 = _int(k_606_273)
                _275 = _274 + -1
                _276 = card1b_wmol[1]
                mdata_wco2[_275] = _276
                k_607_277 = k[0]
                _278 = _int(k_607_277)
                _279 = _278 + -1
                _280 = card1b_wmol[2]
                mdata_wo[_279] = _280
                k_608_281 = k[0]
                _282 = _int(k_608_281)
                _283 = _282 + -1
                _284 = card1b_wmol[3]
                mdata_wn2o[_283] = _284
                k_609_285 = k[0]
                _286 = _int(k_609_285)
                _287 = _286 + -1
                _288 = card1b_wmol[4]
                mdata_wco[_287] = _288
                k_610_289 = k[0]
                _290 = _int(k_610_289)
                _291 = _290 + -1
                _292 = card1b_wmol[5]
                mdata_wch4[_291] = _292
                k_611_293 = k[0]
                _294 = _int(k_611_293)
                _295 = _294 + -1
                _296 = card1b_wmol[6]
                mdata_wo2[_295] = _296
                k_612_297 = k[0]
                _298 = _int(k_612_297)
                _299 = _298 + -1
                _300 = card1b_wmol[7]
                mdata1_wno[_299] = _300
                k_613_301 = k[0]
                _302 = _int(k_613_301)
                _303 = _302 + -1
                _304 = card1b_wmol[8]
                mdata1_wso2[_303] = _304
                k_614_305 = k[0]
                _306 = _int(k_614_305)
                _307 = _306 + -1
                _308 = card1b_wmol[9]
                mdata1_wno2[_307] = _308
                k_615_309 = k[0]
                _310 = _int(k_615_309)
                _311 = _310 + -1
                _312 = card1b_wmol[10]
                mdata1_wnh3[_311] = _312
                k_616_313 = k[0]
                _314 = _int(k_616_313)
                _315 = _314 + -1
                _316 = card1b_wmol[11]
                __BLNK___whno3[_315] = _316
                k_617_317 = k[0]
                _318 = _int(k_617_317)
                _319 = _318 + -1
                _320 = card1b_wair1[0]
                mdata1_wair[_319] = _320
                _pc = 112
                continue
            case 111:  # <D.19827>
                _ft_vsansm(_state, k, ahaze, iha1)
                k_618_321 = k[0]
                _322 = _int(k_618_321)
                _323 = _322 + -1
                k_619_324 = k[0]
                _325 = _int(k_619_324)
                _326 = _325 + -1
                _327 = mdata_z[_323]
                model_zmdl[_326] = _327
                _pc = 112
            case 112:  # L.961
                k_620_328 = k[0]
                _329 = _int(k_620_328)
                _330 = _329 + -1
                zsc = _f32(model_zmdl[_330])
                _331 = gndalt[0]
                _332 = _331 > 0.0
                k_621_333 = k[0]
                _334 = _int(k_621_333)
                _335 = _334 + -1
                _336 = model_zmdl[_335]
                _337 = _336 < 6.0e+0
                _338 = _332 & _337
                _pc = 113 if _338 != 0 else 116
                continue
            case 113:  # <D.19829>
                _339 = gndalt[0]
                _340 = 6.0e+0 - _339
                _341 = _340
                asc = _f32(_div(6.0e+0, _341))
                _342 = gndalt[0]
                _343 = asc * _342
                con = _f32(-_343)
                k_622_344 = k[0]
                _345 = _int(k_622_344)
                _346 = _345 + -1
                _347 = model_zmdl[_346]
                _348 = asc * _347
                _349 = con + _348
                zsc = _f32(_349 - 9.99999974737875163555145263671875e-5)
                _pc = 114 if zsc < 0.0 else 115
                continue
            case 114:  # <D.19831>
                zsc = _f32(0.0)
                _pc = 115
                continue
            case 115:  # L.963
                _pc = 116
                continue
            case 116:  # L.962
                k_623_350 = k[0]
                _351 = _int(k_623_350)
                _352 = _351 + -1
                zgn[_352] = zsc
                icld1_624_353 = icld1[0]
                _pc = 117 if icld1_624_353 == 0 else 118
                continue
            case 117:  # <D.19835>
                _354 = card2_icld[0]
                icld1[0] = _354
                _pc = 118
                continue
            case 118:  # L.964
                icldl = _int(icld1[0])
                icld1_625_355 = icld1[0]
                _pc = 119 if icld1_625_355 > 11 else 120
                continue
            case 119:  # <D.19838>
                icld1[0] = 0
                _pc = 120
                continue
            case 120:  # L.965
                iha1_626_356 = iha1[0]
                _pc = 121 if iha1_626_356 != 0 else 122
                continue
            case 121:  # <D.19841>
                ivul1[0] = 0
                _pc = 122
                continue
            case 122:  # L.966
                iha1_627_357 = iha1[0]
                _pc = 123 if iha1_627_357 != 0 else 124
                continue
            case 123:  # <D.19844>
                icld1[0] = 0
                _pc = 124
                continue
            case 124:  # L.967
                icld1_628_358 = icld1[0]
                _pc = 125 if icld1_628_358 != 0 else 126
                continue
            case 125:  # <D.19847>
                ivul1[0] = 0
                _pc = 126
                continue
            case 126:  # L.968
                ahaze_629_359 = ahaze[0]
                _360 = ahaze_629_359 != 0.0
                eqlwcz_630_361 = eqlwcz[0]
                _362 = eqlwcz_630_361 != 0.0
                _363 = _360 | _362
                _pc = 127 if _363 != 0 else 128
                continue
            case 127:  # <D.19850>
                _pc = 140
                continue
            case 128:  # L.969
                _364 = card2_ivsa[0]
                _365 = _364 == 1
                icld1_631_366 = icld1[0]
                _367 = icld1_631_366 == 0
                _368 = _365 & _367
                _pc = 129 if _368 != 0 else 132
                continue
            case 129:  # <D.19852>
                _369 = card1_model[0]
                _pc = 130 if _369 != 7 else 131
                continue
            case 130:  # <D.19854>
                _ft_layvsa(_state, k, rh, ahaze, iha1)
                _pc = 131
                continue
            case 131:  # L.971
                _pc = 140
                continue
            case 132:  # <D.19853>
                _ft_laycld(_state, k, eqlwcz, rratz, icld1, gndalt, card2_rainrt)
                _370 = card2_rainrt[0]
                _371 = _370 > 0.0
                k_632_372 = k[0]
                _373 = _int(k_632_372)
                _374 = _373 + -1
                _375 = model_zmdl[_374]
                _376 = _375 < 6.0e+0
                _377 = _371 & _376
                _pc = 133 if _377 != 0 else 134
                continue
            case 133:  # <D.19858>
                _378 = card2_rainrt[0]
                rratz[0] = _378
                _pc = 134
                continue
            case 134:  # L.972
                icld1_633_379 = icld1[0]
                _pc = 135 if icld1_633_379 <= 0 else 136
                continue
            case 135:  # <D.19861>
                _pc = 140
                continue
            case 136:  # L.973
                icld1_634_380 = icld1[0]
                _pc = 137 if icld1_634_380 > 10 else 138
                continue
            case 137:  # <D.19863>
                _pc = 140
                continue
            case 138:  # L.974
                k_635_381 = k[0]
                _382 = _int(k_635_381)
                _383 = _382 + -1
                _384 = model_zmdl[_383]
                icld1_636_385 = icld1[0]
                _386 = _int(icld1_636_385)
                _387 = _386 + -1
                _388 = cldtop[_387]
                _389 = gndalt[0]
                _390 = _388 + _389
                _pc = 139 if _384 > _390 else 140
                continue
            case 139:  # <D.19865>
                rratz[0] = 0.0
                _pc = 140
                continue
            case 140:  # __label_000008
                icldc = _int(card2_icld[0])
                _pc = 141 if iclds != 0 else 142
                continue
            case 141:  # <D.19868>
                icldc = _int(iclds)
                _pc = 142
                continue
            case 142:  # L.976
                _391 = iclds == 18
                _392 = iclds == 19
                _393 = _391 | _392
                _pc = 143 if _393 != 0 else 152
                continue
            case 143:  # <D.19871>
                ahaze_637_394 = ahaze[0]
                _pc = 144 if ahaze_637_394 > 0.0 else 145
                continue
            case 144:  # <D.19873>
                k_638_395 = k[0]
                _396 = _int(k_638_395)
                _397 = _396 * 63
                _398 = _397 + -48
                ahaze_639_399 = ahaze[0]
                model_densty[_398] = ahaze_639_399
                ahaze[0] = 0.0
                _pc = 156
                continue
            case 145:  # L.978
                eqlwcz_640_400 = eqlwcz[0]
                _pc = 146 if eqlwcz_640_400 > 0.0 else 151
                continue
            case 146:  # <D.19875>
                _pc = 147 if iclds == 18 else 148
                continue
            case 147:  # <D.19877>
                con = _f32(3.44599992968142032623291015625e-3)
                _pc = 148
                continue
            case 148:  # L.980
                _pc = 149 if iclds == 19 else 150
                continue
            case 149:  # <D.19880>
                con = _f32(5.81099987030029296875e-2)
                _pc = 150
                continue
            case 150:  # L.981
                eqlwcz_641_401 = eqlwcz[0]
                k_642_402 = k[0]
                _403 = _int(k_642_402)
                _404 = _403 * 63
                _405 = _404 + -48
                _406 = _div(eqlwcz_641_401, con)
                model_densty[_405] = _406
                eqlwcz[0] = 0.0
                _pc = 156
                continue
            case 151:  # L.979
                _pc = 152
                continue
            case 152:  # L.977
                _407 = icldc == 18
                _408 = icldc == 19
                _409 = _407 | _408
                _pc = 153 if _409 != 0 else 156
                continue
            case 153:  # <D.19884>
                k_643_410 = k[0]
                _411 = _int(k_643_410)
                _412 = _411 * 63
                _413 = _412 + -48
                model_densty[_413] = 0.0
                k_644_414 = k[0]
                _415 = _int(k_644_414)
                _416 = _415 + -1
                _417 = model_zmdl[_416]
                _418 = cld1 <= _417
                k_645_419 = k[0]
                _420 = _int(k_645_419)
                _421 = _420 + -1
                _422 = model_zmdl[_421]
                _423 = cld2 >= _422
                _424 = _418 & _423
                _pc = 154 if _424 != 0 else 155
                continue
            case 154:  # <D.19886>
                k_646_425 = k[0]
                _426 = _int(k_646_425)
                _427 = _426 * 63
                _428 = _427 + -48
                _429 = card2a_cext[0]
                model_densty[_428] = _429
                _pc = 155
                continue
            case 155:  # L.983
                _pc = 156
                continue
            case 156:  # __label_000046
                k_647_430 = k[0]
                _431 = _int(k_647_430)
                _432 = _431 + -1
                eqlwcz_648_433 = eqlwcz[0]
                model_cldamt[_432] = eqlwcz_648_433
                _434 = iclds == 0
                k_649_435 = k[0]
                _436 = _int(k_649_435)
                _437 = _436 + -1
                _438 = model_cldamt[_437]
                _439 = _438 == 0.0
                _440 = _434 & _439
                _pc = 157 if _440 != 0 else 158
                continue
            case 157:  # <D.19890>
                icld1[0] = 0
                _pc = 158
                continue
            case 158:  # L.984
                k_650_441 = k[0]
                _442 = _int(k_650_441)
                _443 = _442 + -1
                rratz_651_444 = rratz[0]
                model_rramt[_443] = rratz_651_444
                _445 = card1_model[0]
                _446 = _445 != 0
                _447 = card1_model[0]
                _448 = _447 != 7
                _449 = _446 & _448
                _pc = 159 if _449 != 0 else 164
                continue
            case 159:  # <D.19893>
                eqlwcz_652_450 = eqlwcz[0]
                _pc = 160 if eqlwcz_652_450 > 0.0 else 161
                continue
            case 160:  # <D.19895>
                rh[0] = 1.0e+2
                _pc = 161
                continue
            case 161:  # L.986
                rratz_653_451 = rratz[0]
                _pc = 162 if rratz_653_451 > 0.0 else 163
                continue
            case 162:  # <D.19898>
                rh[0] = 1.0e+2
                _pc = 163
                continue
            case 163:  # L.987
                _pc = 164
                continue
            case 164:  # L.985
                k_654_452 = k[0]
                _453 = _int(k_654_452)
                _454 = _453 + -1
                ahaze_655_455 = ahaze[0]
                ahast[_454] = ahaze_655_455
                isea1_656_456 = isea1[0]
                _pc = 165 if isea1_656_456 == 0 else 166
                continue
            case 165:  # <D.19902>
                _457 = card2_iseasn[0]
                isea1[0] = _457
                _pc = 166
                continue
            case 166:  # L.988
                ityaer = _int(card2_ihaze[0])
                iha1_657_458 = iha1[0]
                _pc = 167 if iha1_657_458 > 0 else 168
                continue
            case 167:  # <D.19905>
                ityaer = _int(iha1[0])
                _pc = 168
                continue
            case 168:  # L.989
                ivul1_658_459 = ivul1[0]
                _pc = 169 if ivul1_658_459 > 0 else 170
                continue
            case 169:  # <D.19908>
                ivul1_659_460 = ivul1[0]
                card2_ivulcn[0] = ivul1_659_460
                _pc = 170
                continue
            case 170:  # L.990
                ivul1_660_461 = ivul1[0]
                _pc = 171 if ivul1_660_461 <= 0 else 172
                continue
            case 171:  # <D.19911>
                _462 = card2_ivulcn[0]
                ivul1[0] = _462
                _pc = 172
                continue
            case 172:  # L.991
                k_661_463 = k[0]
                _pc = 173 if k_661_463 == 1 else 174
                continue
            case 173:  # <D.19914>
                _pc = 232
                continue
            case 174:  # L.992
                _pc = 175 if ichr == 1 else 176
                continue
            case 175:  # <D.19916>
                _pc = 227
                continue
            case 176:  # L.993
                ic1_662_464 = ic1[0]
                _465 = _int(ic1_662_464)
                _466 = _465 + -1
                _467 = card2d_iregc[_466]
                icld1_663_468 = icld1[0]
                _pc = 177 if _467 != icld1_663_468 else 178
                continue
            case 177:  # <D.19918>
                _pc = 197
                continue
            case 178:  # L.994
                iha1_664_469 = iha1[0]
                _470 = iha1_664_469 == 0
                icld1_665_471 = icld1[0]
                _472 = icld1_665_471 == 0
                _473 = _470 & _472
                _pc = 179 if _473 != 0 else 188
                continue
            case 179:  # <D.19920>
                _pc = 180 if zsc > 2.0e+0 else 181
                continue
            case 180:  # <D.19922>
                ityaer = _int(6)
                _pc = 181
                continue
            case 181:  # L.996
                _pc = 182 if zsc > 1.0e+1 else 183
                continue
            case 182:  # <D.19925>
                _474 = card2_ivulcn[0]
                ityaer = _int(_474 + 10)
                _pc = 183
                continue
            case 183:  # L.997
                _pc = 184 if zsc > 3.0e+1 else 185
                continue
            case 184:  # <D.19928>
                ityaer = _int(19)
                _pc = 185
                continue
            case 185:  # L.998
                ic1_666_475 = ic1[0]
                _476 = _int(ic1_666_475)
                _477 = _476 + -1
                _478 = __BLNK___ich[_477]
                _pc = 186 if ityaer == _478 else 187
                continue
            case 186:  # <D.19931>
                _pc = 232
                continue
            case 187:  # L.999
                _pc = 188
                continue
            case 188:  # L.995
                icld1_667_479 = icld1[0]
                _480 = icld1_667_479 == 0
                iha1_668_481 = iha1[0]
                _482 = iha1_668_481 == 0
                _483 = _480 & _482
                _pc = 189 if _483 != 0 else 190
                continue
            case 189:  # <D.19934>
                _pc = 227
                continue
            case 190:  # L.1000
                n = _int(7)
                ic1_669_484 = ic1[0]
                _pc = 191 if ic1_669_484 > 1 else 192
                continue
            case 191:  # <D.19936>
                ic1_670_485 = ic1[0]
                n = _int(ic1_670_485 + 10)
                _pc = 192
                continue
            case 192:  # L.1001
                iha1_671_486 = iha1[0]
                _pc = 193 if iha1_671_486 == 0 else 194
                continue
            case 193:  # <D.19939>
                _pc = 232
                continue
            case 194:  # L.1002
                ic1_672_487 = ic1[0]
                _488 = _int(ic1_672_487)
                _489 = _488 + -1
                _490 = __BLNK___ich[_489]
                iha1_673_491 = iha1[0]
                _pc = 195 if _490 != iha1_673_491 else 196
                continue
            case 195:  # <D.19941>
                _pc = 227
                continue
            case 196:  # L.1003
                _pc = 232
                continue
            case 197:  # __label_000019
                icld1_674_492 = icld1[0]
                _pc = 198 if icld1_674_492 != 0 else 209
                continue
            case 198:  # <D.19943>
                _493 = card2d_iregc[0]
                icld1_675_494 = icld1[0]
                _pc = 199 if _493 == icld1_675_494 else 200
                continue
            case 199:  # <D.19945>
                n = _int(7)
                k_676_495 = k[0]
                _496 = _int(k_676_495)
                _497 = _496 + -1
                _498 = model_zmdl[_497]
                card2d_altb[0] = _498
                _pc = 233
                continue
            case 200:  # L.1005
                ic1_677_499 = ic1[0]
                _pc = 201 if ic1_677_499 == 1 else 202
                continue
            case 201:  # <D.19947>
                _pc = 227
                continue
            case 202:  # L.1006
                _500 = card2d_iregc[1]
                icld1_678_501 = icld1[0]
                _pc = 203 if _500 == icld1_678_501 else 204
                continue
            case 203:  # <D.19949>
                n = _int(12)
                k_679_502 = k[0]
                _503 = _int(k_679_502)
                _504 = _503 + -1
                _505 = model_zmdl[_504]
                card2d_altb[1] = _505
                _pc = 233
                continue
            case 204:  # L.1007
                ic1_680_506 = ic1[0]
                _pc = 205 if ic1_680_506 == 2 else 206
                continue
            case 205:  # <D.19951>
                _pc = 227
                continue
            case 206:  # L.1008
                _507 = card2d_iregc[2]
                icld1_681_508 = icld1[0]
                _pc = 207 if _507 == icld1_681_508 else 208
                continue
            case 207:  # <D.19953>
                n = _int(13)
                k_682_509 = k[0]
                _510 = _int(k_682_509)
                _511 = _510 + -1
                _512 = model_zmdl[_511]
                card2d_altb[2] = _512
                _pc = 233
                continue
            case 208:  # L.1009
                _pc = 227
                continue
            case 209:  # <D.19944>
                iha1_683_513 = iha1[0]
                _514 = iha1_683_513 == 0
                icld1_684_515 = icld1[0]
                _516 = icld1_684_515 == 0
                _517 = _514 & _516
                _pc = 210 if _517 != 0 else 217
                continue
            case 210:  # <D.19956>
                _pc = 211 if zsc > 2.0e+0 else 212
                continue
            case 211:  # <D.19958>
                ityaer = _int(6)
                _pc = 212
                continue
            case 212:  # L.1011
                _pc = 213 if zsc > 1.0e+1 else 214
                continue
            case 213:  # <D.19961>
                _518 = card2_ivulcn[0]
                ityaer = _int(_518 + 10)
                _pc = 214
                continue
            case 214:  # L.1012
                _pc = 215 if zsc > 3.0e+1 else 216
                continue
            case 215:  # <D.19964>
                ityaer = _int(19)
                _pc = 216
                continue
            case 216:  # L.1013
                _pc = 217
                continue
            case 217:  # L.1010
                _519 = __BLNK___ich[0]
                _pc = 218 if ityaer == _519 else 219
                continue
            case 218:  # <D.19968>
                n = _int(7)
                k_685_520 = k[0]
                _521 = _int(k_685_520)
                _522 = _521 + -1
                _523 = model_zmdl[_522]
                card2d_altb[0] = _523
                _pc = 233
                continue
            case 219:  # L.1014
                ic1_686_524 = ic1[0]
                _pc = 220 if ic1_686_524 == 1 else 221
                continue
            case 220:  # <D.19970>
                _pc = 227
                continue
            case 221:  # L.1015
                _525 = __BLNK___ich[1]
                _pc = 222 if ityaer == _525 else 223
                continue
            case 222:  # <D.19972>
                n = _int(12)
                k_687_526 = k[0]
                _527 = _int(k_687_526)
                _528 = _527 + -1
                _529 = model_zmdl[_528]
                card2d_altb[1] = _529
                _pc = 233
                continue
            case 223:  # L.1016
                ic1_688_530 = ic1[0]
                _pc = 224 if ic1_688_530 == 2 else 225
                continue
            case 224:  # <D.19974>
                _pc = 227
                continue
            case 225:  # L.1017
                _531 = __BLNK___ich[2]
                _pc = 226 if ityaer == _531 else 227
                continue
            case 226:  # <D.19976>
                n = _int(13)
                k_689_532 = k[0]
                _533 = _int(k_689_532)
                _534 = _533 + -1
                _535 = model_zmdl[_534]
                card2d_altb[2] = _535
                _pc = 233
                continue
            case 227:  # __label_000020
                ic1_690_536 = ic1[0]
                _537 = ic1_690_536 + 1
                ic1[0] = _537
                ic1_691_538 = ic1[0]
                n = _int(ic1_691_538 + 10)
                rh_692_539 = rh[0]
                _pc = 228 if rh_692_539 > 0.0 else 229
                continue
            case 228:  # <D.19978>
                rh_693_540 = rh[0]
                mart_rhh[0] = rh_693_540
                _pc = 229
                continue
            case 229:  # L.1019
                ic1_694_541 = ic1[0]
                _pc = 230 if ic1_694_541 <= 4 else 231
                continue
            case 230:  # <D.19981>
                _pc = 232
                continue
            case 231:  # L.1020
                ic1[0] = 4
                n = _int(14)
                ic1_695_542 = ic1[0]
                _543 = _int(ic1_695_542)
                _544 = _543 + -1
                ityaer = _int(__BLNK___ich[_544])
                _pc = 232
            case 232:  # __label_000023
                ic1_696_545 = ic1[0]
                _546 = _int(ic1_696_545)
                _547 = _546 + -1
                __BLNK___ich[_547] = ityaer
                ic1_697_548 = ic1[0]
                _549 = _int(ic1_697_548)
                _550 = _549 + -1
                icld1_698_551 = icld1[0]
                card2d_iregc[_550] = icld1_698_551
                k_699_552 = k[0]
                _553 = _int(k_699_552)
                _554 = _553 + -1
                ic1_700_555 = ic1[0]
                _556 = _int(ic1_700_555)
                _557 = _556 + -1
                _558 = model_zmdl[_554]
                card2d_altb[_557] = _558
                _pc = 233
            case 233:  # __label_000024
                rh_701_559 = rh[0]
                _pc = 234 if rh_701_559 > 0.0 else 235
                continue
            case 234:  # <D.19983>
                k_702_560 = k[0]
                _561 = _int(k_702_560)
                _562 = _561 + -1
                _563 = mdata_t[_562]
                ta = _f32(_div(t0, _563))
                a_39 = _f32(ta)
                _564 = a_39 * 1.495950031280517578125e+1
                _565 = 1.897660064697265625e+1 - _564
                _566 = a_39 * 2.43881988525390625e+0
                _567 = a_39 * _566
                _568 = _565 - _567
                _569 = __builtin_expf(_568)
                _570 = a_39 * _569
                _571 = _570 * 9.99999977648258209228515625e-3
                rh_703_572 = rh[0]
                k_704_573 = k[0]
                _574 = _int(k_704_573)
                _575 = _574 + -1
                _576 = _571 * rh_703_572
                mdata_wh[_575] = _576
                _pc = 235
                continue
            case 235:  # __label_000040
                k_705_577 = k[0]
                _578 = _int(k_705_577)
                _579 = _578 * 63
                _580 = _579 + -57
                model_densty[_580] = 0.0
                k_706_581 = k[0]
                _582 = _int(k_706_581)
                _583 = _582 * 63
                _584 = _583 + -52
                model_densty[_584] = 0.0
                k_707_585 = k[0]
                _586 = _int(k_707_585)
                _587 = _586 * 63
                _588 = _587 + -51
                model_densty[_588] = 0.0
                k_708_589 = k[0]
                _590 = _int(k_708_589)
                _591 = _590 * 63
                _592 = _591 + -50
                model_densty[_592] = 0.0
                k_709_593 = k[0]
                _594 = _int(k_709_593)
                _595 = _594 * 63
                _596 = _595 + -49
                model_densty[_596] = 0.0
                k_710_597 = k[0]
                _598 = _int(k_710_597)
                _599 = _598 + -1
                _600 = mdata_t[_599]
                ts = _f32(_div(2.73149993896484375e+2, _600))
                k_711_601 = k[0]
                _602 = _int(k_711_601)
                _603 = _602 + -1
                wtemp = _f32(mdata_wh[_603])
                k_712_604 = k[0]
                _605 = _int(k_712_604)
                _606 = _605 + -1
                __BLNK___relhum[_606] = 0.0
                _pc = 236 if wtemp <= 0.0 else 237
                continue
            case 236:  # <D.19986>
                _pc = 241
                continue
            case 237:  # L.1022
                a_40 = _f32(ts)
                _607 = wtemp * 1.0e+2
                _608 = a_40 * 1.495950031280517578125e+1
                _609 = 1.897660064697265625e+1 - _608
                _610 = a_40 * 2.43881988525390625e+0
                _611 = a_40 * _610
                _612 = _609 - _611
                _613 = __builtin_expf(_612)
                _614 = a_40 * _613
                k_713_615 = k[0]
                _616 = _int(k_713_615)
                _617 = _616 + -1
                _618 = _div(_607, _614)
                __BLNK___relhum[_617] = _618
                k_714_619 = k[0]
                _620 = _int(k_714_619)
                _621 = _620 + -1
                _622 = __BLNK___relhum[_621]
                _pc = 238 if _622 > 1.0e+2 else 239
                continue
            case 238:  # <D.19988>
                k_715_623 = k[0]
                _624 = _int(k_715_623)
                _625 = _624 + -1
                __BLNK___relhum[_625] = 1.0e+2
                _pc = 239
                continue
            case 239:  # __label_000930
                k_716_626 = k[0]
                _627 = _int(k_716_626)
                _628 = _627 + -1
                _629 = __BLNK___relhum[_628]
                _pc = 240 if _629 < 0.0 else 241
                continue
            case 240:  # <D.19991>
                k_717_630 = k[0]
                _631 = _int(k_717_630)
                _632 = _631 + -1
                __BLNK___relhum[_632] = 0.0
                _pc = 241
                continue
            case 241:  # __label_000045
                k_718_633 = k[0]
                _634 = _int(k_718_633)
                _635 = _634 + -1
                _636 = __BLNK___relhum[_635]
                mart_rhh[0] = _636
                _637 = mart_rhh[0]
                rh[0] = _637
                vis1_719_638 = vis1[0]
                _pc = 242 if vis1_719_638 <= 0.0 else 243
                continue
            case 242:  # <D.19994>
                _639 = card2_vis[0]
                vis1[0] = _639
                _pc = 243
                continue
            case 243:  # L.1025
                ahaze_720_640 = ahaze[0]
                _pc = 244 if ahaze_720_640 == 0.0 else 245
                continue
            case 244:  # <D.19997>
                _pc = 250
                continue
            case 245:  # L.1026
                k_721_641 = k[0]
                _642 = _int(k_721_641)
                _643 = _642 * 63
                _644 = _int(n)
                _645 = _643 + _644
                _646 = _645 + -64
                ahaze_722_647 = ahaze[0]
                model_densty[_646] = ahaze_722_647
                _pc = 246 if ityaer == 3 else 247
                continue
            case 246:  # <D.19999>
                _pc = 250
                continue
            case 247:  # L.1027
                _pc = 248 if ityaer == 10 else 249
                continue
            case 248:  # <D.20001>
                _pc = 250
                continue
            case 249:  # L.1028
                _pc = 282
                continue
            case 250:  # __label_000047
                _648 = gndalt[0]
                _649 = _648 > 0.0
                k_723_650 = k[0]
                _651 = _int(k_723_650)
                _652 = _651 + -1
                _653 = model_zmdl[_652]
                _654 = _653 < 6.0e+0
                _655 = _649 & _654
                _pc = 251 if _655 != 0 else 252
                continue
            case 251:  # <D.20003>
                _656 = zsc + 9.999999974752427078783512115478515625e-7
                _657 = _int(_656)
                _658 = _657 + 1
                j[0] = _658
                j_724_659 = j[0]
                _660 = j_724_659 + -1
                _661 = _f32(_660)
                fac = _f32(zsc - _661)
                _pc = 266
                continue
            case 252:  # <D.20004>
                k_725_662 = k[0]
                _663 = _int(k_725_662)
                _664 = _663 + -1
                _665 = model_zmdl[_664]
                _666 = _665 + 9.999999974752427078783512115478515625e-7
                _667 = _int(_666)
                _668 = _667 + 1
                j[0] = _668
                k_726_669 = k[0]
                _670 = _int(k_726_669)
                _671 = _670 + -1
                _672 = model_zmdl[_671]
                _pc = 253 if _672 >= 2.5e+1 else 254
                continue
            case 253:  # <D.20006>
                k_727_673 = k[0]
                _674 = _int(k_727_673)
                _675 = _674 + -1
                _676 = model_zmdl[_675]
                _677 = _676 - 2.5e+1
                _678 = _677
                _679 = _div(_678, 5.0e+0)
                _680 = _679 + 2.6e+1
                _681 = _int(_680)
                j[0] = _681
                _pc = 254
                continue
            case 254:  # L.1030
                k_728_682 = k[0]
                _683 = _int(k_728_682)
                _684 = _683 + -1
                _685 = model_zmdl[_684]
                _pc = 255 if _685 >= 5.0e+1 else 256
                continue
            case 255:  # <D.20009>
                k_729_686 = k[0]
                _687 = _int(k_729_686)
                _688 = _687 + -1
                _689 = model_zmdl[_688]
                _690 = _689 - 5.0e+1
                _691 = _690
                _692 = _div(_691, 2.0e+1)
                _693 = _692 + 3.1e+1
                _694 = _int(_693)
                j[0] = _694
                _pc = 256
                continue
            case 256:  # L.1031
                k_730_695 = k[0]
                _696 = _int(k_730_695)
                _697 = _696 + -1
                _698 = model_zmdl[_697]
                _pc = 257 if _698 >= 7.0e+1 else 258
                continue
            case 257:  # <D.20012>
                k_731_699 = k[0]
                _700 = _int(k_731_699)
                _701 = _700 + -1
                _702 = model_zmdl[_701]
                _703 = _702 - 7.0e+1
                _704 = _703
                _705 = _div(_704, 3.0e+1)
                _706 = _705 + 3.2e+1
                _707 = _int(_706)
                j[0] = _707
                _pc = 258
                continue
            case 258:  # L.1032
                j_732_708 = j[0]
                _pc = 259 if j_732_708 > 32 else 260
                continue
            case 259:  # <D.20015>
                j[0] = 32
                _pc = 260
                continue
            case 260:  # L.1033
                k_733_709 = k[0]
                _710 = _int(k_733_709)
                _711 = _710 + -1
                _712 = model_zmdl[_711]
                j_734_713 = j[0]
                _714 = j_734_713 + -1
                _715 = _f32(_714)
                fac = _f32(_712 - _715)
                j_735_716 = j[0]
                _pc = 261 if j_735_716 <= 25 else 262
                continue
            case 261:  # <D.20018>
                _pc = 266
                continue
            case 262:  # L.1034
                k_736_717 = k[0]
                _718 = _int(k_736_717)
                _719 = _718 + -1
                _720 = model_zmdl[_719]
                j_737_721 = j[0]
                _722 = j_737_721 + -26
                _723 = _f32(_722)
                _724 = _723 * 5.0e+0
                _725 = _720 - _724
                _726 = _725 - 2.5e+1
                _727 = _726
                fac = _f32(_div(_727, 5.0e+0))
                j_738_728 = j[0]
                _pc = 263 if j_738_728 > 30 else 264
                continue
            case 263:  # <D.20020>
                k_739_729 = k[0]
                _730 = _int(k_739_729)
                _731 = _730 + -1
                _732 = model_zmdl[_731]
                _733 = _732 - 5.0e+1
                _734 = _733
                fac = _f32(_div(_734, 2.0e+1))
                _pc = 264
                continue
            case 264:  # L.1035
                j_740_735 = j[0]
                _pc = 265 if j_740_735 > 31 else 266
                continue
            case 265:  # <D.20023>
                k_741_736 = k[0]
                _737 = _int(k_741_736)
                _738 = _737 + -1
                _739 = model_zmdl[_738]
                _740 = _739 - 7.0e+1
                _741 = _740
                fac = _f32(_div(_741, 3.0e+1))
                _pc = 266
                continue
            case 266:  # __label_000125
                j_742_742 = j[0]
                _743 = j_742_742 + 1
                l[0] = _743
                _pc = 267 if fac > 1.0e+0 else 268
                continue
            case 267:  # <D.20026>
                fac = _f32(1.0e+0)
                _pc = 268
                continue
            case 268:  # L.1037
                _744 = ityaer == 3
                _745 = icl == 0
                _746 = _744 & _745
                _pc = 269 if _746 != 0 else 270
                continue
            case 269:  # <D.20029>
                _ft_marine(_state, vis1, card1_model, card2_wss, card2_whh, card2_icstl, __BLNK___extc, __BLNK___absc, ic1)
                ic1_743_747 = ic1[0]
                _748 = _int(ic1_743_747)
                _749 = _748 + -1
                card2d_ireg[_749] = 1
                vis1_744_750 = vis1[0]
                card2_vis[0] = vis1_744_750
                icl = _int(icl + 1)
                _pc = 270
                continue
            case 270:  # L.1038
                _751 = ityaer == 10
                _752 = idsr == 0
                _753 = _751 & _752
                _pc = 271 if _753 != 0 else 272
                continue
            case 271:  # <D.20032>
                _ft_desatt(_state, card2_wss, vis1)
                ic1_745_754 = ic1[0]
                _755 = _int(ic1_745_754)
                _756 = _755 + -1
                card2d_ireg[_756] = 1
                vis1_746_757 = vis1[0]
                card2_vis[0] = vis1_746_757
                idsr = _int(idsr + 1)
                _pc = 272
                continue
            case 272:  # L.1039
                ahaze_747_758 = ahaze[0]
                _pc = 273 if ahaze_747_758 > 0.0 else 274
                continue
            case 273:  # <D.20035>
                _pc = 282
                continue
            case 274:  # L.1040
                iha1_748_759 = iha1[0]
                _pc = 275 if iha1_748_759 <= 0 else 276
                continue
            case 275:  # <D.20037>
                _760 = card2_ihaze[0]
                iha1[0] = _760
                _pc = 276
                continue
            case 276:  # L.1041
                _ft_cldprf(_state, k, icld1, iha1, ic1)
                _ft_aerprf(_state, j, vis1, haz1, iha1, isea1, ivul1, nn)
                _ft_aerprf(_state, l, vis1, haz2, iha1, isea1, ivul1, nn)
                haze = _f32(0.0)
                haz1_749_761 = haz1[0]
                _762 = haz1_749_761 <= 0.0
                haz2_750_763 = haz2[0]
                _764 = haz2_750_763 <= 0.0
                _765 = _762 | _764
                _pc = 277 if _765 != 0 else 278
                continue
            case 277:  # <D.20040>
                _pc = 279
                continue
            case 278:  # L.1042
                haz2_751_766 = haz2[0]
                haz1_752_767 = haz1[0]
                _768 = _div(haz2_751_766, haz1_752_767)
                D_14937 = _f32(_768)
                _769 = __builtin_powf(D_14937, fac)
                haz1_753_770 = haz1[0]
                haze = _f32(_769 * haz1_753_770)
                _pc = 279
            case 279:  # __label_000048
                k_754_771 = k[0]
                _772 = _int(k_754_771)
                _773 = _772 + -1
                _774 = model_cldamt[_773]
                _pc = 280 if _774 > 0.0 else 281
                continue
            case 280:  # <D.20042>
                k_755_775 = k[0]
                _776 = _int(k_755_775)
                _777 = _776 + -1
                haze = _f32(model_hazec[_777])
                _pc = 281
                continue
            case 281:  # L.1043
                k_756_778 = k[0]
                _779 = _int(k_756_778)
                _780 = _779 * 63
                _781 = _int(n)
                _782 = _780 + _781
                _783 = _782 + -64
                model_densty[_783] = haze
                _pc = 282
            case 282:  # __label_000050
                k_757_784 = k[0]
                _785 = _int(k_757_784)
                _786 = _785 + -1
                ity1[_786] = ityaer
                k_758_787 = k[0]
                _788 = _int(k_758_787)
                _789 = _788 + -1
                iha1_759_790 = iha1[0]
                ih1[_789] = iha1_759_790
                ahaze_760_791 = ahaze[0]
                _pc = 283 if ahaze_760_791 != 0.0 else 284
                continue
            case 283:  # <D.20045>
                k_761_792 = k[0]
                _793 = _int(k_761_792)
                _794 = _793 + -1
                ih1[_794] = -99
                _pc = 284
                continue
            case 284:  # L.1044
                k_762_795 = k[0]
                _796 = _int(k_762_795)
                _797 = _796 + -1
                isea1_763_798 = isea1[0]
                is1[_797] = isea1_763_798
                k_764_799 = k[0]
                _800 = _int(k_764_799)
                _801 = _800 + -1
                ivul1_765_802 = ivul1[0]
                ivl1[_801] = ivul1_765_802
                _pc = 285
            case 285:  # L.925
                k_766_803 = k[0]
                _804 = k_766_803 + 1
                k[0] = _804
                _pc = 42
                continue
            case 286:  # L.926
                ihh = _int(card2_icld[0])
                _pc = 287 if ihh <= 0 else 288
                continue
            case 287:  # <D.20048>
                ihh = _int(12)
                _pc = 288
                continue
            case 288:  # L.1045
                _pc = 289 if ihh > 12 else 290
                continue
            case 289:  # <D.20051>
                ihh = _int(12)
                _pc = 290
                continue
            case 290:  # L.1046
                _805 = card2_icld[0]
                _pc = 291 if _805 > 17 else 292
                continue
            case 291:  # <D.20054>
                ihh = _int(13)
                _pc = 292
                continue
            case 292:  # L.1047
                ii = _int(1)
                _pc = 293
            case 293:  # <D.20057>
                D_14946 = _int(ii > 5)
                _pc = 297 if D_14946 != 0 else 294
                continue
            case 294:  # <D.20058>
                _806 = _int(ihh)
                _807 = _806 * 5
                _808 = _int(ii)
                _809 = _807 + _808
                _810 = _809 + -6
                _811 = ahahol[_810:]
                _812 = _int(ii)
                _813 = _812 + -1
                _814 = hhol[_813:]
                __builtin_memmove(_814, _811, 4)
                _815 = card2_ivsa[0]
                _pc = 295 if _815 != 0 else 296
                continue
            case 295:  # <D.20059>
                _816 = _int(ii)
                _817 = _816 + -1
                _818 = ahlvsa[_817:]
                _819 = _int(ii)
                _820 = _819 + -1
                _821 = hhol[_820:]
                __builtin_memmove(_821, _818, 4)
                _pc = 296
                continue
            case 296:  # L.1048
                ii = _int(ii + 1)
                _pc = 293
                continue
            case 297:  # L.1049
                _822 = card2_icld[0]
                _pc = 298 if _822 != 0 else 299
                continue
            case 298:  # __label_000904
                _pc = 299
                continue
            case 299:  # __label_000905
                _823 = jprt[0]
                _pc = 300 if _823 == 1 else 301
                continue
            case 300:  # <D.20065>
                return
            case 301:  # L.1052
                D_14953 = _int(cntrl_ml[0])
                kk = _int(1)
                _pc = 302
            case 302:  # <D.20067>
                D_14956 = _int(kk > D_14953)
                _pc = 334 if D_14956 != 0 else 303
                continue
            case 303:  # <D.20068>
                ij = _int(1)
                _pc = 304
            case 304:  # <D.20069>
                D_14959 = _int(ij > 5)
                _pc = 308 if D_14959 != 0 else 305
                continue
            case 305:  # <D.20070>
                _824 = _int(ij)
                _825 = _824 + -1
                _826 = ahol1[_825:]
                __builtin_memmove(_826, titl_blank, 4)
                _827 = _int(ij)
                _828 = _827 + -1
                _829 = ahol2[_828:]
                __builtin_memmove(_829, titl_blank, 4)
                _pc = 306
            case 306:  # __label_000052
                _830 = _int(ij)
                _831 = _830 + -1
                _832 = ahol3[_831:]
                __builtin_memmove(_832, titl_blank, 4)
                _pc = 307
            case 307:  # L.1055
                ij = _int(ij + 1)
                _pc = 304
                continue
            case 308:  # L.1056
                _833 = _int(kk)
                _834 = _833 + -1
                ityaer = _int(ity1[_834])
                _pc = 309 if ityaer <= 0 else 310
                continue
            case 309:  # <D.20071>
                ityaer = _int(1)
                _pc = 310
                continue
            case 310:  # L.1057
                _pc = 311 if ityaer == 16 else 312
                continue
            case 311:  # <D.20074>
                ityaer = _int(11)
                _pc = 312
                continue
            case 312:  # L.1058
                _pc = 313 if ityaer == 17 else 314
                continue
            case 313:  # <D.20077>
                ityaer = _int(11)
                _pc = 314
                continue
            case 314:  # L.1059
                _pc = 315 if ityaer == 18 else 316
                continue
            case 315:  # <D.20080>
                ityaer = _int(13)
                _pc = 316
                continue
            case 316:  # L.1060
                _pc = 317 if ityaer == 19 else 318
                continue
            case 317:  # <D.20083>
                ityaer = _int(11)
                _pc = 318
                continue
            case 318:  # L.1061
                _835 = _int(kk)
                _836 = _835 + -1
                _837 = ih1[_836]
                iha1[0] = _837
                _838 = _int(kk)
                _839 = _838 + -1
                _840 = is1[_839]
                isea1[0] = _840
                _841 = _int(kk)
                _842 = _841 + -1
                _843 = ivl1[_842]
                ivul1[0] = _843
                ij = _int(1)
                _pc = 319
            case 319:  # <D.20086>
                D_14968 = _int(ij > 5)
                _pc = 333 if D_14968 != 0 else 320
                continue
            case 320:  # <D.20087>
                _844 = _int(ityaer)
                _845 = _844 * 5
                _846 = _int(ij)
                _847 = _845 + _846
                _848 = _847 + -6
                _849 = titl_hz[_848:]
                _850 = _int(ij)
                _851 = _850 + -1
                _852 = ahol1[_851:]
                __builtin_memmove(_852, _849, 4)
                _853 = card2_ivsa[0]
                _pc = 321 if _853 == 1 else 322
                continue
            case 321:  # <D.20088>
                _854 = _int(ij)
                _855 = _854 + -1
                _856 = hhol[_855:]
                _857 = _int(ij)
                _858 = _857 + -1
                _859 = ahol1[_858:]
                __builtin_memmove(_859, _856, 4)
                _pc = 322
                continue
            case 322:  # L.1064
                _860 = _int(kk)
                _861 = _860 + -1
                _862 = model_cldamt[_861]
                _863 = _862 > 0.0
                _864 = _int(kk)
                _865 = _864 + -1
                _866 = model_rramt[_865]
                _867 = _866 > 0.0
                _868 = _863 | _867
                _pc = 323 if _868 != 0 else 324
                continue
            case 323:  # <D.20091>
                _869 = _int(ij)
                _870 = _869 + -1
                _871 = hhol[_870:]
                _872 = _int(ij)
                _873 = _872 + -1
                _874 = ahol1[_873:]
                __builtin_memmove(_874, _871, 4)
                _pc = 324
                continue
            case 324:  # L.1065
                _875 = card2_ihaze[0]
                _pc = 325 if _875 == 0 else 326
                continue
            case 325:  # <D.20094>
                _876 = _int(ij)
                _877 = _876 + -1
                _878 = hhol[_877:]
                _879 = _int(ij)
                _880 = _879 + -1
                _881 = ahol1[_880:]
                __builtin_memmove(_881, _878, 4)
                _pc = 326
                continue
            case 326:  # L.1066
                _882 = _int(ij)
                _883 = _882 + -1
                _884 = ahus[_883:]
                _885 = _int(ij)
                _886 = _885 + -1
                _887 = ahol2[_886:]
                __builtin_memmove(_887, _884, 4)
                _888 = _int(kk)
                _889 = _888 + -1
                _890 = ahast[_889]
                _pc = 327 if _890 == 0.0 else 328
                continue
            case 327:  # <D.20097>
                _891 = _int(ij)
                _892 = _891 + -1
                _893 = ahol1[_892:]
                _894 = _int(ij)
                _895 = _894 + -1
                _896 = ahol2[_895:]
                __builtin_memmove(_896, _893, 4)
                _pc = 328
                continue
            case 328:  # L.1067
                _897 = _int(kk)
                _898 = _897 + -1
                _899 = model_cldamt[_898]
                _900 = _899 > 0.0
                _901 = _int(kk)
                _902 = _901 + -1
                _903 = model_rramt[_902]
                _904 = _903 > 0.0
                _905 = _900 | _904
                _pc = 329 if _905 != 0 else 330
                continue
            case 329:  # <D.20100>
                _906 = _int(ij)
                _907 = _906 + -1
                _908 = hhol[_907:]
                _909 = _int(ij)
                _910 = _909 + -1
                _911 = ahol2[_910:]
                __builtin_memmove(_911, _908, 4)
                _pc = 330
                continue
            case 330:  # __label_000054
                _912 = _int(kk)
                _913 = _912 + -1
                _914 = zgn[_913]
                _pc = 331 if _914 > 2.0e+0 else 332
                continue
            case 331:  # <D.20103>
                isea1_767_915 = isea1[0]
                _916 = _int(isea1_767_915)
                _917 = _916 * 5
                _918 = _int(ij)
                _919 = _917 + _918
                _920 = _919 + -6
                _921 = titl_seasn[_920:]
                _922 = _int(ij)
                _923 = _922 + -1
                _924 = ahol3[_923:]
                __builtin_memmove(_924, _921, 4)
                _pc = 332
                continue
            case 332:  # L.1062
                ij = _int(ij + 1)
                _pc = 319
                continue
            case 333:  # L.1053
                kk = _int(kk + 1)
                _pc = 302
                continue
            case 334:  # __label_000915
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_aerprf(_state, i, vis, haze, ihaze, iseasn, ivulcn, n):
    prfd_zht = _state.view(60288, '<f4')
    prfd_hz2k = _state.view(60424, '<f4')
    prfd_fawi50 = _state.view(61104, '<f4')
    prfd_fawi23 = _state.view(61240, '<f4')
    prfd_spsu50 = _state.view(61376, '<f4')
    prfd_spsu23 = _state.view(61512, '<f4')
    prfd_bastfw = _state.view(61648, '<f4')
    prfd_vumofw = _state.view(61784, '<f4')
    prfd_hivufw = _state.view(61920, '<f4')
    prfd_exvufw = _state.view(62056, '<f4')
    prfd_bastss = _state.view(62192, '<f4')
    prfd_vumoss = _state.view(62328, '<f4')
    prfd_hivuss = _state.view(62464, '<f4')
    prfd_exvuss = _state.view(62600, '<f4')
    prfd_upnatm = _state.view(62736, '<f4')
    prfd_vutono = _state.view(62872, '<f4')
    vs = _state.view(181568, '<f4')
    const = _ZERO32
    hazi = _ZERO32
    j = 0
    D_15043 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                haze[0] = 0.0
                n[0] = 7
                _1 = ihaze[0]
                _pc = 1 if _1 == 0 else 2
                continue
            case 1:  # <D.20122>
                return
            case 2:  # L.1070
                _2 = i[0]
                _3 = _int(_2)
                _4 = _3 + -1
                _5 = prfd_zht[_4]
                _pc = 3 if _5 > 2.0e+0 else 4
                continue
            case 3:  # <D.20124>
                _pc = 13
                continue
            case 4:  # L.1071
                j = _int(2)
                _pc = 5
            case 5:  # <D.20126>
                D_15043 = _int(j > 5)
                _pc = 9 if D_15043 != 0 else 6
                continue
            case 6:  # <D.20127>
                _6 = vis[0]
                _7 = _int(j)
                _8 = _7 + -1
                _9 = vs[_8]
                _pc = 7 if _6 >= _9 else 8
                continue
            case 7:  # <D.20128>
                _pc = 10
                continue
            case 8:  # L.1072
                j = _int(j + 1)
                _pc = 5
                continue
            case 9:  # L.1073
                j = _int(5)
                _pc = 10
            case 10:  # __label_000010
                _10 = _int(j)
                _11 = _10 + -1
                _12 = vs[_11]
                _13 = _div(1.0e+0, _12)
                _14 = j + -1
                _15 = _int(_14)
                _16 = _15 + -1
                _17 = vs[_16]
                _18 = _div(1.0e+0, _17)
                _19 = _13 - _18
                _20 = _19
                const = _f32(_div(1.0e+0, _20))
                _21 = _int(j)
                _22 = _21 * 34
                _23 = i[0]
                _24 = _int(_23)
                _25 = _22 + _24
                _26 = _25 + -35
                _27 = prfd_hz2k[_26]
                _28 = j + -1
                _29 = _int(_28)
                _30 = _29 * 34
                _31 = i[0]
                _32 = _int(_31)
                _33 = _30 + _32
                _34 = _33 + -35
                _35 = prfd_hz2k[_34]
                _36 = _27 - _35
                _37 = _36
                _38 = vis[0]
                _39 = _div(_37, _38)
                _40 = j + -1
                _41 = _int(_40)
                _42 = _41 * 34
                _43 = i[0]
                _44 = _int(_43)
                _45 = _42 + _44
                _46 = _45 + -35
                _47 = prfd_hz2k[_46]
                _48 = _int(j)
                _49 = _48 + -1
                _50 = vs[_49]
                _51 = _div(_47, _50)
                _52 = _39 + _51
                _53 = _int(j)
                _54 = _53 * 34
                _55 = i[0]
                _56 = _int(_55)
                _57 = _54 + _56
                _58 = _57 + -35
                _59 = prfd_hz2k[_58]
                _60 = j + -1
                _61 = _int(_60)
                _62 = _61 + -1
                _63 = vs[_62]
                _64 = _div(_59, _63)
                _65 = _52 - _64
                _66 = _65
                _67 = const * _66
                haze[0] = _67
                _68 = i[0]
                _69 = _int(_68)
                _70 = _69 + -1
                _71 = prfd_zht[_70]
                _pc = 11 if _71 > 2.0e+0 else 12
                continue
            case 11:  # <D.20130>
                _pc = 13
                continue
            case 12:  # L.1075
                return
            case 13:  # __label_000015
                _72 = i[0]
                _73 = _int(_72)
                _74 = _73 + -1
                _75 = prfd_zht[_74]
                _pc = 14 if _75 > 1.0e+1 else 15
                continue
            case 14:  # <D.20132>
                _pc = 33
                continue
            case 15:  # L.1076
                const = _f32(4.259259033203125e+1)
                _76 = iseasn[0]
                _pc = 16 if _76 > 1 else 17
                continue
            case 16:  # <D.20134>
                _pc = 25
                continue
            case 17:  # L.1077
                _77 = vis[0]
                _pc = 18 if _77 <= 2.3e+1 else 19
                continue
            case 18:  # <D.20136>
                _78 = i[0]
                _79 = _int(_78)
                _80 = _79 + -1
                hazi = _f32(prfd_spsu23[_80])
                _pc = 19
                continue
            case 19:  # L.1078
                _81 = vis[0]
                _pc = 20 if _81 <= 2.3e+1 else 21
                continue
            case 20:  # <D.20139>
                _pc = 91
                continue
            case 21:  # L.1079
                _82 = i[0]
                _83 = _int(_82)
                _84 = _83 + -1
                _85 = prfd_zht[_84]
                _pc = 22 if _85 > 4.0e+0 else 23
                continue
            case 22:  # <D.20141>
                _pc = 24
                continue
            case 23:  # L.1080
                _86 = i[0]
                _87 = _int(_86)
                _88 = _87 + -1
                _89 = prfd_spsu23[_88]
                _90 = i[0]
                _91 = _int(_90)
                _92 = _91 + -1
                _93 = prfd_spsu50[_92]
                _94 = _89 - _93
                _95 = _94
                _96 = vis[0]
                _97 = _div(_95, _96)
                _98 = i[0]
                _99 = _int(_98)
                _100 = _99 + -1
                _101 = prfd_spsu50[_100]
                _102 = _div(_101, 2.3e+1)
                _103 = _97 + _102
                _104 = i[0]
                _105 = _int(_104)
                _106 = _105 + -1
                _107 = prfd_spsu23[_106]
                _108 = _div(_107, 5.0e+1)
                _109 = _103 - _108
                _110 = _109
                hazi = _f32(const * _110)
                _pc = 91
                continue
            case 24:  # __label_000020
                _111 = i[0]
                _112 = _int(_111)
                _113 = _112 + -1
                hazi = _f32(prfd_spsu50[_113])
                _pc = 91
                continue
            case 25:  # __label_000025
                _114 = vis[0]
                _pc = 26 if _114 <= 2.3e+1 else 27
                continue
            case 26:  # <D.20143>
                _115 = i[0]
                _116 = _int(_115)
                _117 = _116 + -1
                hazi = _f32(prfd_fawi23[_117])
                _pc = 27
                continue
            case 27:  # L.1081
                _118 = vis[0]
                _pc = 28 if _118 <= 2.3e+1 else 29
                continue
            case 28:  # <D.20146>
                _pc = 91
                continue
            case 29:  # L.1082
                _119 = i[0]
                _120 = _int(_119)
                _121 = _120 + -1
                _122 = prfd_zht[_121]
                _pc = 30 if _122 > 4.0e+0 else 31
                continue
            case 30:  # <D.20148>
                _pc = 32
                continue
            case 31:  # L.1083
                _123 = i[0]
                _124 = _int(_123)
                _125 = _124 + -1
                _126 = prfd_fawi23[_125]
                _127 = i[0]
                _128 = _int(_127)
                _129 = _128 + -1
                _130 = prfd_fawi50[_129]
                _131 = _126 - _130
                _132 = _131
                _133 = vis[0]
                _134 = _div(_132, _133)
                _135 = i[0]
                _136 = _int(_135)
                _137 = _136 + -1
                _138 = prfd_fawi50[_137]
                _139 = _div(_138, 2.3e+1)
                _140 = _134 + _139
                _141 = i[0]
                _142 = _int(_141)
                _143 = _142 + -1
                _144 = prfd_fawi23[_143]
                _145 = _div(_144, 5.0e+1)
                _146 = _140 - _145
                _147 = _146
                hazi = _f32(const * _147)
                _pc = 91
                continue
            case 32:  # __label_000030
                _148 = i[0]
                _149 = _int(_148)
                _150 = _149 + -1
                hazi = _f32(prfd_fawi50[_150])
                _pc = 91
                continue
            case 33:  # __label_000035
                _151 = i[0]
                _152 = _int(_151)
                _153 = _152 + -1
                _154 = prfd_zht[_153]
                _pc = 34 if _154 > 3.0e+1 else 35
                continue
            case 34:  # <D.20150>
                _pc = 87
                continue
            case 35:  # L.1084
                _155 = i[0]
                _156 = _int(_155)
                _157 = _156 + -1
                hazi = _f32(prfd_bastss[_157])
                _158 = iseasn[0]
                _pc = 36 if _158 > 1 else 37
                continue
            case 36:  # <D.20152>
                _pc = 62
                continue
            case 37:  # L.1085
                _159 = ivulcn[0]
                _pc = 38 if _159 == 0 else 39
                continue
            case 38:  # <D.20154>
                _160 = i[0]
                _161 = _int(_160)
                _162 = _161 + -1
                hazi = _f32(prfd_bastss[_162])
                _pc = 39
                continue
            case 39:  # L.1086
                _163 = ivulcn[0]
                _pc = 40 if _163 == 0 else 41
                continue
            case 40:  # <D.20157>
                _pc = 91
                continue
            case 41:  # L.1087
                _164 = ivulcn[0]
                _pc = {1: 42, 2: 44, 3: 46, 4: 48, 5: 50, 6: 52, 7: 54, 8: 56}.get(_164, 58)
                continue
            case 42:  # L.1090
                _pc = 58
                continue
            case 43:  # continuation_104
                _pc = 58
                continue
            case 44:  # L.1091
                _pc = 59
                continue
            case 45:  # continuation_107
                _pc = 58
                continue
            case 46:  # L.1092
                _pc = 60
                continue
            case 47:  # continuation_110
                _pc = 58
                continue
            case 48:  # L.1093
                _pc = 60
                continue
            case 49:  # continuation_113
                _pc = 58
                continue
            case 50:  # L.1094
                _pc = 59
                continue
            case 51:  # continuation_116
                _pc = 58
                continue
            case 52:  # L.1095
                _pc = 59
                continue
            case 53:  # continuation_119
                _pc = 58
                continue
            case 54:  # L.1096
                _pc = 60
                continue
            case 55:  # continuation_122
                _pc = 58
                continue
            case 56:  # L.1097
                _pc = 61
                continue
            case 57:  # continuation_125
                _pc = 58
                continue
            case 58:  # __label_000040
                _165 = i[0]
                _166 = _int(_165)
                _167 = _166 + -1
                hazi = _f32(prfd_bastss[_167])
                _pc = 91
                continue
            case 59:  # __label_000045
                _168 = i[0]
                _169 = _int(_168)
                _170 = _169 + -1
                hazi = _f32(prfd_vumoss[_170])
                _pc = 91
                continue
            case 60:  # __label_000050
                _171 = i[0]
                _172 = _int(_171)
                _173 = _172 + -1
                hazi = _f32(prfd_hivuss[_173])
                _pc = 91
                continue
            case 61:  # __label_000052
                _174 = i[0]
                _175 = _int(_174)
                _176 = _175 + -1
                hazi = _f32(prfd_exvuss[_176])
                _pc = 91
                continue
            case 62:  # __label_000055
                _177 = ivulcn[0]
                _pc = 63 if _177 == 0 else 64
                continue
            case 63:  # <D.20160>
                _178 = i[0]
                _179 = _int(_178)
                _180 = _179 + -1
                hazi = _f32(prfd_bastfw[_180])
                _pc = 64
                continue
            case 64:  # L.1098
                _181 = ivulcn[0]
                _pc = 65 if _181 == 0 else 66
                continue
            case 65:  # <D.20163>
                _pc = 91
                continue
            case 66:  # L.1099
                _182 = ivulcn[0]
                _pc = {1: 67, 2: 69, 3: 71, 4: 73, 5: 75, 6: 77, 7: 79, 8: 81}.get(_182, 83)
                continue
            case 67:  # L.1102
                _pc = 83
                continue
            case 68:  # continuation_152
                _pc = 83
                continue
            case 69:  # L.1103
                _pc = 84
                continue
            case 70:  # continuation_155
                _pc = 83
                continue
            case 71:  # L.1104
                _pc = 85
                continue
            case 72:  # continuation_158
                _pc = 83
                continue
            case 73:  # L.1105
                _pc = 85
                continue
            case 74:  # continuation_161
                _pc = 83
                continue
            case 75:  # L.1106
                _pc = 84
                continue
            case 76:  # continuation_164
                _pc = 83
                continue
            case 77:  # L.1107
                _pc = 84
                continue
            case 78:  # continuation_167
                _pc = 83
                continue
            case 79:  # L.1108
                _pc = 85
                continue
            case 80:  # continuation_170
                _pc = 83
                continue
            case 81:  # L.1109
                _pc = 86
                continue
            case 82:  # continuation_173
                _pc = 83
                continue
            case 83:  # __label_000060
                _183 = i[0]
                _184 = _int(_183)
                _185 = _184 + -1
                hazi = _f32(prfd_bastfw[_185])
                _pc = 91
                continue
            case 84:  # __label_000065
                _186 = i[0]
                _187 = _int(_186)
                _188 = _187 + -1
                hazi = _f32(prfd_vumofw[_188])
                _pc = 91
                continue
            case 85:  # __label_000070
                _189 = i[0]
                _190 = _int(_189)
                _191 = _190 + -1
                hazi = _f32(prfd_hivufw[_191])
                _pc = 91
                continue
            case 86:  # __label_000072
                _192 = i[0]
                _193 = _int(_192)
                _194 = _193 + -1
                hazi = _f32(prfd_exvufw[_194])
                _pc = 91
                continue
            case 87:  # __label_000075
                n[0] = 14
                _195 = ivulcn[0]
                _pc = 88 if _195 > 1 else 89
                continue
            case 88:  # <D.20166>
                _pc = 90
                continue
            case 89:  # L.1110
                _196 = i[0]
                _197 = _int(_196)
                _198 = _197 + -1
                hazi = _f32(prfd_upnatm[_198])
                _pc = 91
                continue
            case 90:  # __label_000080
                _199 = i[0]
                _200 = _int(_199)
                _201 = _200 + -1
                hazi = _f32(prfd_vutono[_201])
                _pc = 91
            case 91:  # __label_000200
                _pc = 92 if hazi > 0.0 else -1
                continue
            case 92:  # <D.20168>
                haze[0] = hazi
                _pc = -1
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_cldprf(_state, k, icld, iha1, ic1):
    __BLNK___relhum = _state.view(265568, '<f4')
    __BLNK___ich = _state.view(265840, '<i4')
    model_cldamt = _state.view(241016, '<f4')
    model_hazec = _state.view(241424, '<f4')
    aflwc = _state.view(181696, '<f4')
    aslwc = _state.view(181600, '<f4')
    avlwc = _state.view(181708, '<f4')
    bslwc = _state.view(181704, '<f4')
    culwc = _state.view(181596, '<f4')
    elwcm = _state.view(181648, '<f4')
    elwcr = _state.view(181632, '<f4')
    elwct = _state.view(181680, '<f4')
    elwcu = _state.view(181664, '<f4')
    fvlwc = _state.view(181712, '<f4')
    mdlwc = _state.view(181716, '<f4')
    rflwc = _state.view(181700, '<f4')
    rhzone = _state.view(181616, '<f4')
    sclwc = _state.view(181608, '<f4')
    snlwc = _state.view(181612, '<f4')
    stlwc = _state.view(181604, '<f4')
    tklwc = _state.view(181592, '<f4')
    tnlwc = _state.view(181588, '<f4')
    con = _ZERO32
    e1 = _ZERO32
    e2 = _ZERO32
    ec = _ZERO32
    i = 0
    ih = 0
    ii = 0
    ita = 0
    itc = 0
    m = 0
    n = 0
    wrh = _ZERO32
    x = _ZERO32
    x1 = _ZERO32
    x2 = _ZERO32
    D_15234 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = k[0]
                _2 = _int(_1)
                _3 = _2 + -1
                _4 = model_cldamt[_3]
                _pc = 1 if _4 <= 0.0 else 2
                continue
            case 1:  # <D.20172>
                _pc = 38
                continue
            case 2:  # L.1112
                ih = _int(icld[0])
                _pc = 3 if ih == 0 else 4
                continue
            case 3:  # <D.20174>
                _pc = 39
                continue
            case 4:  # L.1113
                _5 = icld[0]
                _pc = 5 if _5 == 18 else 6
                continue
            case 5:  # <D.20176>
                _6 = k[0]
                _7 = _int(_6)
                _8 = _7 + -1
                _9 = model_cldamt[_8]
                tnlwc_768_10 = tnlwc[0]
                _11 = k[0]
                _12 = _int(_11)
                _13 = _12 + -1
                _14 = _div(_9, tnlwc_768_10)
                model_hazec[_13] = _14
                return
            case 6:  # L.1114
                _15 = icld[0]
                _pc = 7 if _15 == 19 else 8
                continue
            case 7:  # <D.20178>
                _16 = k[0]
                _17 = _int(_16)
                _18 = _17 + -1
                _19 = model_cldamt[_18]
                tklwc_769_20 = tklwc[0]
                _21 = k[0]
                _22 = _int(_21)
                _23 = _22 + -1
                _24 = _div(_19, tklwc_769_20)
                model_hazec[_23] = _24
                return
            case 8:  # L.1115
                _25 = icld[0]
                _pc = 9 if _25 == 20 else 10
                continue
            case 9:  # <D.20180>
                return
            case 10:  # L.1116
                _pc = {1: 11, 2: 13, 3: 15, 4: 17, 5: 19, 6: 21, 7: 23, 8: 25, 9: 27, 10: 29, 11: 31}.get(ih, 33)
                continue
            case 11:  # L.1119
                _pc = 33
                continue
            case 12:  # continuation_28
                _pc = 33
                continue
            case 13:  # L.1120
                _pc = 34
                continue
            case 14:  # continuation_31
                _pc = 33
                continue
            case 15:  # L.1121
                _pc = 35
                continue
            case 16:  # continuation_34
                _pc = 33
                continue
            case 17:  # L.1122
                _pc = 36
                continue
            case 18:  # continuation_37
                _pc = 33
                continue
            case 19:  # L.1123
                _pc = 37
                continue
            case 20:  # continuation_40
                _pc = 33
                continue
            case 21:  # L.1124
                _pc = 35
                continue
            case 22:  # continuation_43
                _pc = 33
                continue
            case 23:  # L.1125
                _pc = 37
                continue
            case 24:  # continuation_46
                _pc = 33
                continue
            case 25:  # L.1126
                _pc = 37
                continue
            case 26:  # continuation_49
                _pc = 33
                continue
            case 27:  # L.1127
                _pc = 33
                continue
            case 28:  # continuation_52
                _pc = 33
                continue
            case 29:  # L.1128
                _pc = 33
                continue
            case 30:  # continuation_55
                _pc = 33
                continue
            case 31:  # L.1129
                _pc = 33
                continue
            case 32:  # continuation_58
                _pc = 33
                continue
            case 33:  # __label_000114
                _26 = k[0]
                _27 = _int(_26)
                _28 = _27 + -1
                _29 = model_cldamt[_28]
                culwc_770_30 = culwc[0]
                _31 = k[0]
                _32 = _int(_31)
                _33 = _32 + -1
                _34 = _div(_29, culwc_770_30)
                model_hazec[_33] = _34
                return
            case 34:  # __label_000115
                _35 = k[0]
                _36 = _int(_35)
                _37 = _36 + -1
                _38 = model_cldamt[_37]
                aslwc_771_39 = aslwc[0]
                _40 = k[0]
                _41 = _int(_40)
                _42 = _41 + -1
                _43 = _div(_38, aslwc_771_39)
                model_hazec[_42] = _43
                return
            case 35:  # __label_000116
                _44 = k[0]
                _45 = _int(_44)
                _46 = _45 + -1
                _47 = model_cldamt[_46]
                stlwc_772_48 = stlwc[0]
                _49 = k[0]
                _50 = _int(_49)
                _51 = _50 + -1
                _52 = _div(_47, stlwc_772_48)
                model_hazec[_51] = _52
                return
            case 36:  # __label_000117
                _53 = k[0]
                _54 = _int(_53)
                _55 = _54 + -1
                _56 = model_cldamt[_55]
                sclwc_773_57 = sclwc[0]
                _58 = k[0]
                _59 = _int(_58)
                _60 = _59 + -1
                _61 = _div(_56, sclwc_773_57)
                model_hazec[_60] = _61
                return
            case 37:  # __label_000118
                _62 = k[0]
                _63 = _int(_62)
                _64 = _63 + -1
                _65 = model_cldamt[_64]
                snlwc_774_66 = snlwc[0]
                _67 = k[0]
                _68 = _int(_67)
                _69 = _68 + -1
                _70 = _div(_65, snlwc_774_66)
                model_hazec[_69] = _70
                _pc = 38
            case 38:  # __label_000015
                return
            case 39:  # __label_000200
                _71 = iha1[0]
                _pc = 40 if _71 > 0 else 41
                continue
            case 40:  # <D.20183>
                _pc = 42
                continue
            case 41:  # L.1130
                return
            case 42:  # __label_000205
                _72 = k[0]
                _73 = _int(_72)
                _74 = _73 + -1
                wrh = _f32(__BLNK___relhum[_74])
                m = _int(ic1[0])
                _75 = _int(m)
                _76 = _75 + -1
                _77 = __BLNK___ich[_76]
                _78 = _77 == 6
                _79 = m != 1
                _80 = _78 & _79
                _pc = 43 if _80 != 0 else 44
                continue
            case 43:  # <D.20185>
                wrh = _f32(7.0e+1)
                _pc = 44
                continue
            case 44:  # L.1131
                i = _int(2)
                _pc = 45
            case 45:  # <D.20188>
                D_15234 = _int(i > 4)
                _pc = 49 if D_15234 != 0 else 46
                continue
            case 46:  # <D.20189>
                _81 = _int(i)
                _82 = _81 + -1
                _83 = rhzone[_82]
                _pc = 47 if wrh < _83 else 48
                continue
            case 47:  # <D.20190>
                _pc = 50
                continue
            case 48:  # L.1132
                i = _int(i + 1)
                _pc = 45
                continue
            case 49:  # L.1133
                i = _int(4)
                _pc = 50
            case 50:  # __label_000215
                ii = _int(i + -1)
                _84 = wrh > 0.0
                _85 = wrh < 9.9e+1
                _86 = _84 & _85
                _pc = 51 if _86 != 0 else 52
                continue
            case 51:  # <D.20192>
                _87 = 1.0e+2 - wrh
                x = _f32(__builtin_logf(_87))
                _pc = 52
                continue
            case 52:  # L.1135
                _88 = _int(ii)
                _89 = _88 + -1
                _90 = rhzone[_89]
                _91 = 1.0e+2 - _90
                x1 = _f32(__builtin_logf(_91))
                _92 = _int(i)
                _93 = _92 + -1
                _94 = rhzone[_93]
                _95 = 1.0e+2 - _94
                x2 = _f32(__builtin_logf(_95))
                _pc = 53 if wrh >= 9.9e+1 else 54
                continue
            case 53:  # <D.20195>
                x = _f32(x2)
                _pc = 54
                continue
            case 54:  # L.1136
                _pc = 55 if wrh <= 0.0 else 56
                continue
            case 55:  # <D.20198>
                x = _f32(x1)
                _pc = 56
                continue
            case 56:  # L.1137
                _96 = _int(m)
                _97 = _96 + -1
                ita = _int(__BLNK___ich[_97])
                _98 = ita == 3
                _99 = m == 1
                _100 = _98 & _99
                _pc = 57 if _100 != 0 else 58
                continue
            case 57:  # <D.20201>
                _pc = 61
                continue
            case 58:  # L.1138
                _pc = 59 if ita > 6 else 60
                continue
            case 59:  # <D.20203>
                _pc = 84
                continue
            case 60:  # L.1139
                n = _int(41)
                _pc = 61
            case 61:  # __label_000218
                _101 = n > 40
                _102 = ita == 3
                _103 = _101 & _102
                _pc = 62 if _103 != 0 else 63
                continue
            case 62:  # <D.20205>
                ita = _int(4)
                _pc = 63
                continue
            case 63:  # L.1140
                _pc = {1: 64, 2: 66, 3: 68, 4: 70, 5: 72, 6: 74}.get(ita, 76)
                continue
            case 64:  # L.1143
                _pc = 76
                continue
            case 65:  # continuation_138
                _pc = 76
                continue
            case 66:  # L.1144
                _pc = 76
                continue
            case 67:  # continuation_141
                _pc = 76
                continue
            case 68:  # L.1145
                _pc = 77
                continue
            case 69:  # continuation_144
                _pc = 76
                continue
            case 70:  # L.1146
                _pc = 80
                continue
            case 71:  # continuation_147
                _pc = 76
                continue
            case 72:  # L.1147
                _pc = 81
                continue
            case 73:  # continuation_150
                _pc = 76
                continue
            case 74:  # L.1148
                _pc = 82
                continue
            case 75:  # continuation_153
                _pc = 76
                continue
            case 76:  # __label_000220
                _104 = _int(i)
                _105 = _104 + -1
                _106 = elwcr[_105]
                e2 = _f32(__builtin_logf(_106))
                _107 = _int(ii)
                _108 = _107 + -1
                _109 = elwcr[_108]
                e1 = _f32(__builtin_logf(_109))
                _pc = 83
                continue
            case 77:  # __label_000222
                _pc = 78 if m > 1 else 79
                continue
            case 78:  # <D.20209>
                _pc = 80
                continue
            case 79:  # L.1149
                _110 = _int(i)
                _111 = _110 + -1
                _112 = elwcm[_111]
                e2 = _f32(__builtin_logf(_112))
                _113 = _int(ii)
                _114 = _113 + -1
                _115 = elwcm[_114]
                e1 = _f32(__builtin_logf(_115))
                _pc = 83
                continue
            case 80:  # __label_000225
                _116 = _int(i)
                _117 = _116 + -1
                _118 = elwcm[_117]
                e2 = _f32(__builtin_logf(_118))
                _119 = _int(ii)
                _120 = _119 + -1
                _121 = elwcm[_120]
                e1 = _f32(__builtin_logf(_121))
                _pc = 83
                continue
            case 81:  # __label_000230
                _122 = _int(i)
                _123 = _122 + -1
                _124 = elwcu[_123]
                e2 = _f32(__builtin_logf(_124))
                _125 = _int(ii)
                _126 = _125 + -1
                _127 = elwcu[_126]
                e1 = _f32(__builtin_logf(_127))
                _pc = 83
                continue
            case 82:  # __label_000235
                _128 = _int(i)
                _129 = _128 + -1
                _130 = elwct[_129]
                e2 = _f32(__builtin_logf(_130))
                _131 = _int(ii)
                _132 = _131 + -1
                _133 = elwct[_132]
                e1 = _f32(__builtin_logf(_133))
                _pc = 83
            case 83:  # __label_000240
                _134 = e2 - e1
                _135 = _134
                _136 = x - x1
                _137 = _136
                _138 = _135 * _137
                _139 = x2 - x1
                _140 = _139
                _141 = _div(_138, _140)
                ec = _f32(e1 + _141)
                con = _f32(__builtin_expf(ec))
                _142 = k[0]
                _143 = _int(_142)
                _144 = _143 + -1
                _145 = model_cldamt[_144]
                _146 = k[0]
                _147 = _int(_146)
                _148 = _147 + -1
                _149 = _div(_145, con)
                model_hazec[_148] = _149
                return
            case 84:  # __label_000245
                _pc = 85 if ita > 19 else 86
                continue
            case 85:  # <D.20211>
                _pc = 118
                continue
            case 86:  # L.1150
                _150 = _int(m)
                _151 = _150 + -1
                _152 = __BLNK___ich[_151]
                itc = _int(_152 + -7)
                _pc = 87 if itc <= 0 else 88
                continue
            case 87:  # <D.20213>
                return
            case 88:  # L.1151
                _pc = {1: 89, 2: 91, 3: 93, 4: 95, 5: 97, 6: 99, 7: 101, 8: 103, 9: 105, 10: 107, 11: 109, 12: 111}.get(itc, 113)
                continue
            case 89:  # L.1154
                _pc = 113
                continue
            case 90:  # continuation_187
                _pc = 113
                continue
            case 91:  # L.1155
                _pc = 114
                continue
            case 92:  # continuation_190
                _pc = 113
                continue
            case 93:  # L.1156
                _pc = 119
                continue
            case 94:  # continuation_193
                _pc = 113
                continue
            case 95:  # L.1157
                _pc = 115
                continue
            case 96:  # continuation_196
                _pc = 113
                continue
            case 97:  # L.1158
                _pc = 116
                continue
            case 98:  # continuation_199
                _pc = 113
                continue
            case 99:  # L.1159
                _pc = 117
                continue
            case 100:  # continuation_202
                _pc = 113
                continue
            case 101:  # L.1160
                _pc = 116
                continue
            case 102:  # continuation_205
                _pc = 113
                continue
            case 103:  # L.1161
                _pc = 117
                continue
            case 104:  # continuation_208
                _pc = 113
                continue
            case 105:  # L.1162
                _pc = 115
                continue
            case 106:  # continuation_211
                _pc = 113
                continue
            case 107:  # L.1163
                _pc = 115
                continue
            case 108:  # continuation_214
                _pc = 113
                continue
            case 109:  # L.1164
                _pc = 117
                continue
            case 110:  # continuation_217
                _pc = 113
                continue
            case 111:  # L.1165
                _pc = 118
                continue
            case 112:  # continuation_220
                _pc = 113
                continue
            case 113:  # __label_000250
                con = _f32(aflwc[0])
                _pc = 119
                continue
            case 114:  # __label_000255
                con = _f32(rflwc[0])
                _pc = 119
                continue
            case 115:  # __label_000260
                con = _f32(bslwc[0])
                _pc = 119
                continue
            case 116:  # __label_000265
                con = _f32(avlwc[0])
                _pc = 119
                continue
            case 117:  # __label_000270
                con = _f32(fvlwc[0])
                _pc = 119
                continue
            case 118:  # __label_000275
                con = _f32(mdlwc[0])
                _pc = 119
            case 119:  # __label_000280
                _153 = k[0]
                _154 = _int(_153)
                _155 = _154 + -1
                _156 = model_cldamt[_155]
                _157 = k[0]
                _158 = _int(_157)
                _159 = _158 + -1
                _160 = _div(_156, con)
                model_hazec[_159] = _160
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_desatt(_state, wspd, vis):
    __BLNK___absc = _state.view(283836, '<f4')
    __BLNK___extc = _state.view(284776, '<f4')
    __BLNK___asym = _state.view(285716, '<f4')
    desaer_ext = _state.view(32, '<f4')
    desaer_abs = _state.view(784, '<f4')
    desaer_g = _state.view(1536, '<f4')
    raysct = _state.view(181744, '<f4')
    wind = _state.view(181728, '<f4')
    b = _ZERO32
    desabs = _zeros(47, '<f4')
    desext = _zeros(47, '<f4')
    desg = _zeros(47, '<f4')
    dessca = _zeros(47, '<f4')
    ext55 = _ZERO32
    nwspd = 0
    slope = _ZERO32
    wavel = 0
    D_15352 = 0
    D_15357 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = wspd[0]
                _pc = 1 if _1 < 0.0 else 2
                continue
            case 1:  # <D.20217>
                wspd[0] = 1.0e+1
                _pc = 2
                continue
            case 2:  # L.1166
                _2 = wspd[0]
                _3 = _div(_2, 1.0e+1)
                _4 = _int(_3)
                nwspd = _int(_4 + 1)
                _pc = 3 if nwspd > 3 else 4
                continue
            case 3:  # <D.20220>
                nwspd = _int(3)
                _pc = 4
                continue
            case 4:  # L.1167
                wavel = _int(1)
                _pc = 5
            case 5:  # <D.20223>
                D_15352 = _int(wavel > 47)
                _pc = 8 if D_15352 != 0 else 6
                continue
            case 6:  # <D.20224>
                _5 = nwspd + 1
                _6 = _int(_5)
                _7 = _6 * 47
                _8 = _int(wavel)
                _9 = _7 + _8
                _10 = _9 + -48
                _11 = desaer_ext[_10]
                _12 = _int(nwspd)
                _13 = _12 * 47
                _14 = _int(wavel)
                _15 = _13 + _14
                _16 = _15 + -48
                _17 = desaer_ext[_16]
                _18 = _div(_11, _17)
                _19 = __builtin_logf(_18)
                _20 = nwspd + 1
                _21 = _int(_20)
                _22 = _21 + -1
                _23 = wind[_22]
                _24 = _int(nwspd)
                _25 = _24 + -1
                _26 = wind[_25]
                _27 = _23 - _26
                _28 = _27
                slope = _f32(_div(_19, _28))
                _29 = nwspd + 1
                _30 = _int(_29)
                _31 = _30 * 47
                _32 = _int(wavel)
                _33 = _31 + _32
                _34 = _33 + -48
                _35 = desaer_ext[_34]
                _36 = __builtin_logf(_35)
                _37 = nwspd + 1
                _38 = _int(_37)
                _39 = _38 + -1
                _40 = wind[_39]
                _41 = slope * _40
                b = _f32(_36 - _41)
                _42 = wspd[0]
                _43 = slope * _42
                _44 = b + _43
                _45 = _int(wavel)
                _46 = _45 + -1
                _47 = __builtin_expf(_44)
                desext[_46] = _47
                _48 = nwspd + 1
                _49 = _int(_48)
                _50 = _49 * 47
                _51 = _int(wavel)
                _52 = _50 + _51
                _53 = _52 + -48
                _54 = desaer_abs[_53]
                _55 = _int(nwspd)
                _56 = _55 * 47
                _57 = _int(wavel)
                _58 = _56 + _57
                _59 = _58 + -48
                _60 = desaer_abs[_59]
                _61 = _div(_54, _60)
                _62 = __builtin_logf(_61)
                _63 = nwspd + 1
                _64 = _int(_63)
                _65 = _64 + -1
                _66 = wind[_65]
                _67 = _int(nwspd)
                _68 = _67 + -1
                _69 = wind[_68]
                _70 = _66 - _69
                _71 = _70
                slope = _f32(_div(_62, _71))
                _72 = nwspd + 1
                _73 = _int(_72)
                _74 = _73 * 47
                _75 = _int(wavel)
                _76 = _74 + _75
                _77 = _76 + -48
                _78 = desaer_abs[_77]
                _79 = __builtin_logf(_78)
                _80 = nwspd + 1
                _81 = _int(_80)
                _82 = _81 + -1
                _83 = wind[_82]
                _84 = slope * _83
                b = _f32(_79 - _84)
                _85 = wspd[0]
                _86 = slope * _85
                _87 = b + _86
                _88 = _int(wavel)
                _89 = _88 + -1
                _90 = __builtin_expf(_87)
                desabs[_89] = _90
                _91 = _int(wavel)
                _92 = _91 + -1
                _93 = desext[_92]
                _94 = _int(wavel)
                _95 = _94 + -1
                _96 = desabs[_95]
                _97 = _int(wavel)
                _98 = _97 + -1
                _99 = _93 - _96
                dessca[_98] = _99
                _100 = nwspd + 1
                _101 = _int(_100)
                _102 = _101 * 47
                _103 = _int(wavel)
                _104 = _102 + _103
                _105 = _104 + -48
                _106 = desaer_g[_105]
                _107 = _int(nwspd)
                _108 = _107 * 47
                _109 = _int(wavel)
                _110 = _108 + _109
                _111 = _110 + -48
                _112 = desaer_g[_111]
                _113 = _106 - _112
                _114 = _113
                _115 = nwspd + 1
                _116 = _int(_115)
                _117 = _116 + -1
                _118 = wind[_117]
                _119 = _int(nwspd)
                _120 = _119 + -1
                _121 = wind[_120]
                _122 = _118 - _121
                _123 = _122
                slope = _f32(_div(_114, _123))
                _124 = nwspd + 1
                _125 = _int(_124)
                _126 = _125 * 47
                _127 = _int(wavel)
                _128 = _126 + _127
                _129 = _128 + -48
                _130 = desaer_g[_129]
                _131 = nwspd + 1
                _132 = _int(_131)
                _133 = _132 + -1
                _134 = wind[_133]
                _135 = _134
                _136 = slope * _135
                b = _f32(_130 - _136)
                _137 = wspd[0]
                _138 = slope * _137
                _139 = _int(wavel)
                _140 = _139 + -1
                _141 = b + _138
                desg[_140] = _141
                _pc = 7
            case 7:  # L.1168
                wavel = _int(wavel + 1)
                _pc = 5
                continue
            case 8:  # L.1169
                ext55 = _f32(desext[3])
                _142 = vis[0]
                _pc = 9 if _142 <= 0.0 else 10
                continue
            case 9:  # <D.20225>
                _143 = desext[3]
                raysct_775_144 = raysct[0]
                _145 = _143 + raysct_775_144
                _146 = _145
                _147 = _div(3.9119999408721923828125e+0, _146)
                vis[0] = _147
                _pc = 10
                continue
            case 10:  # L.1170
                wavel = _int(1)
                _pc = 11
            case 11:  # <D.20228>
                D_15357 = _int(wavel > 47)
                _pc = 14 if D_15357 != 0 else 12
                continue
            case 12:  # <D.20229>
                _148 = _int(wavel)
                _149 = _148 + -1
                _150 = desext[_149]
                _151 = _int(wavel)
                _152 = _151 + -1
                _153 = _152 * 5
                _154 = _div(_150, ext55)
                __BLNK___extc[_153] = _154
                _155 = _int(wavel)
                _156 = _155 + -1
                _157 = desabs[_156]
                _158 = _int(wavel)
                _159 = _158 + -1
                _160 = _159 * 5
                _161 = _div(_157, ext55)
                __BLNK___absc[_160] = _161
                _162 = _int(wavel)
                _163 = _162 + -1
                _164 = _int(wavel)
                _165 = _164 + -1
                _166 = _165 * 5
                _167 = desg[_163]
                __BLNK___asym[_166] = _167
                _pc = 13
            case 13:  # L.1171
                wavel = _int(wavel + 1)
                _pc = 11
                continue
            case 14:  # __label_000900
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_marine(_state, vis, model, ws, wh, icstl, bext, babs, nl):
    a_t1qext = _state.view(37952, '<f4')
    a_t2qext = _state.view(38592, '<f4')
    a_t3qext = _state.view(39232, '<f4')
    a_t1qabs = _state.view(39872, '<f4')
    a_t2qabs = _state.view(40512, '<f4')
    a_t3qabs = _state.view(41152, '<f4')
    a_arel = _state.view(41952, '<f4')
    cnstns_pi = _state.view(246160, '<f4')
    mart_rhh = _state.view(241568, '<f4')
    rhd = _state.view(181760, '<f4')
    wspd = _state.view(181792, '<f4')
    a1 = _ZERO32
    a2 = _ZERO32
    a3 = _ZERO32
    c = _ZERO32
    delrh = _ZERO32
    delrhv = _ZERO32
    ext55 = _ZERO32
    f = _ZERO32
    i = 0
    j = 0
    pisc = _ZERO32
    qe1 = _ZERO32
    qe2 = _ZERO32
    qe3 = _ZERO32
    ratio = _ZERO32
    rh = _ZERO32
    t1av = _ZERO32
    t1xv = _ZERO32
    t2av = _ZERO32
    t2xv = _ZERO32
    t3av = _ZERO32
    t3xv = _ZERO32
    total = _ZERO32
    D_15445 = _ZERO32
    D_15446 = _ZERO32
    M_41 = _ZERO32
    D_15450 = 0
    D_15457 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = cnstns_pi[0]
                pisc = _f32(_div(_1, 1.0e+3))
                rh = _f32(mart_rhh[0])
                _2 = mart_rhh[0]
                _pc = 1 if _2 > 0.0 else 2
                continue
            case 1:  # <D.20233>
                _pc = 3
                continue
            case 2:  # L.1173
                _3 = model[0]
                _4 = _3 + 1
                _5 = _int(_4)
                _6 = _5 + -1
                rh = _f32(rhd[_6])
                _pc = 3
            case 3:  # __label_000010
                _7 = ws[0]
                _pc = 4 if _7 > 2.0e+1 else 5
                continue
            case 4:  # <D.20235>
                ws[0] = 2.0e+1
                _pc = 5
                continue
            case 5:  # L.1174
                _8 = wh[0]
                _pc = 6 if _8 > 2.0e+1 else 7
                continue
            case 6:  # <D.20238>
                wh[0] = 2.0e+1
                _pc = 7
                continue
            case 7:  # L.1175
                _pc = 8 if rh > 9.8e+1 else 9
                continue
            case 8:  # <D.20241>
                rh = _f32(9.8e+1)
                _pc = 9
                continue
            case 9:  # L.1176
                _9 = rh < 5.0e+1
                _10 = rh >= 0.0
                _11 = _9 & _10
                _pc = 10 if _11 != 0 else 11
                continue
            case 10:  # <D.20244>
                rh = _f32(5.0e+1)
                _pc = 11
                continue
            case 11:  # L.1177
                _12 = icstl[0]
                _13 = _12 <= 0
                _14 = icstl[0]
                _15 = _14 > 10
                _16 = _13 | _15
                _pc = 12 if _16 != 0 else 13
                continue
            case 12:  # <D.20247>
                icstl[0] = 3
                _pc = 13
                continue
            case 13:  # L.1178
                _17 = wh[0]
                _pc = 14 if _17 <= 0.0 else 15
                continue
            case 14:  # <D.20250>
                _18 = model[0]
                _19 = _18 + 1
                _20 = _int(_19)
                _21 = _20 + -1
                _22 = wspd[_21]
                wh[0] = _22
                _pc = 15
                continue
            case 15:  # L.1179
                _23 = ws[0]
                _pc = 16 if _23 <= 0.0 else 17
                continue
            case 16:  # <D.20253>
                _24 = wh[0]
                ws[0] = _24
                _pc = 17
                continue
            case 17:  # L.1180
                _25 = _div(rh, 1.0e+2)
                _26 = 2.0e+0 - _25
                _27 = _26
                _28 = _div(rh, 1.0e+2)
                _29 = 1.0e+0 - _28
                _30 = _29
                _31 = _30 * 6.0e+0
                _32 = _31
                _33 = _div(_27, _32)
                D_15445 = _f32(_33)
                f = _f32(__builtin_powf(D_15445, 3.333300054073333740234375e-1))
                _34 = icstl[0]
                _35 = _f32(_34)
                _36 = _35 * 2.0e+3
                _37 = icstl[0]
                _38 = _f32(_37)
                a1 = _f32(_36 * _38)
                _39 = wh[0]
                _40 = _39 - 2.2000000476837158203125e+0
                _41 = _40
                D_15446 = _f32(_41 * 5.86600017547607421875e+0)
                M_41 = _f32(D_15446)
                M_41 = _f32(max(M_41, 5.0e-1))
                a2 = _f32(M_41)
                _42 = ws[0]
                _43 = _42 * 5.99999986588954925537109375e-2
                _44 = _43 - 2.7999999523162841796875e+0
                _45 = _44
                a3 = _f32(__builtin_powf(1.0e+1, _45))
                j = _int(2)
                _pc = 18
            case 18:  # <D.20256>
                D_15450 = _int(j > 4)
                _pc = 22 if D_15450 != 0 else 19
                continue
            case 19:  # <D.20257>
                _46 = _int(j)
                _47 = _46 + -1
                _48 = a_arel[_47]
                _pc = 20 if rh <= _48 else 21
                continue
            case 20:  # <D.20258>
                _pc = 22
                continue
            case 21:  # L.1181
                j = _int(j + 1)
                _pc = 18
                continue
            case 22:  # __label_000042
                _49 = _int(j)
                _50 = _49 + -1
                _51 = a_arel[_50]
                _52 = j + -1
                _53 = _int(_52)
                _54 = _53 + -1
                _55 = a_arel[_54]
                delrh = _f32(_51 - _55)
                _56 = j + -1
                _57 = _int(_56)
                _58 = _57 + -1
                _59 = a_arel[_58]
                delrhv = _f32(rh - _59)
                ratio = _f32(_div(delrhv, delrh))
                _60 = j + -1
                _61 = _int(_60)
                _62 = _61 * 40
                _63 = _62 + -37
                _64 = a_t1qext[_63]
                _65 = _int(j)
                _66 = _65 * 40
                _67 = _66 + -37
                _68 = a_t1qext[_67]
                _69 = j + -1
                _70 = _int(_69)
                _71 = _70 * 40
                _72 = _71 + -37
                _73 = a_t1qext[_72]
                _74 = _68 - _73
                _75 = _74
                _76 = ratio * _75
                qe1 = _f32(_64 + _76)
                _77 = j + -1
                _78 = _int(_77)
                _79 = _78 * 40
                _80 = _79 + -37
                _81 = a_t2qext[_80]
                _82 = _int(j)
                _83 = _82 * 40
                _84 = _83 + -37
                _85 = a_t2qext[_84]
                _86 = j + -1
                _87 = _int(_86)
                _88 = _87 * 40
                _89 = _88 + -37
                _90 = a_t2qext[_89]
                _91 = _85 - _90
                _92 = _91
                _93 = ratio * _92
                qe2 = _f32(_81 + _93)
                _94 = j + -1
                _95 = _int(_94)
                _96 = _95 * 40
                _97 = _96 + -37
                _98 = a_t3qext[_97]
                _99 = _int(j)
                _100 = _99 * 40
                _101 = _100 + -37
                _102 = a_t3qext[_101]
                _103 = j + -1
                _104 = _int(_103)
                _105 = _104 * 40
                _106 = _105 + -37
                _107 = a_t3qext[_106]
                _108 = _102 - _107
                _109 = _108
                _110 = ratio * _109
                qe3 = _f32(_98 + _110)
                _111 = __builtin_powf(1.0e+1, qe1)
                _112 = a1 * _111
                _113 = __builtin_powf(1.0e+1, qe2)
                _114 = a2 * _113
                _115 = _112 + _114
                _116 = __builtin_powf(1.0e+1, qe3)
                _117 = a3 * _116
                total = _f32(_115 + _117)
                _118 = pisc * total
                ext55 = _f32(_div(_118, f))
                _119 = vis[0]
                _pc = 23 if _119 <= 0.0 else 24
                continue
            case 23:  # <D.20260>
                _120 = ext55 + 1.15900002419948577880859375e-2
                _121 = _120
                _122 = _div(3.9119999408721923828125e+0, _121)
                vis[0] = _122
                _pc = 24
                continue
            case 24:  # L.1184
                _123 = _div(1.0e+0, ext55)
                _124 = _123
                _125 = _div(pisc, f)
                _126 = _125
                c = _f32(_124 * _126)
                a1 = _f32(c * a1)
                a2 = _f32(c * a2)
                a3 = _f32(c * a3)
                i = _int(1)
                _pc = 25
            case 25:  # <D.20263>
                D_15457 = _int(i > 40)
                _pc = 28 if D_15457 != 0 else 26
                continue
            case 26:  # <D.20264>
                _127 = j + -1
                _128 = _int(_127)
                _129 = _128 * 40
                _130 = _int(i)
                _131 = _129 + _130
                _132 = _131 + -41
                _133 = a_t1qext[_132]
                _134 = _int(j)
                _135 = _134 * 40
                _136 = _int(i)
                _137 = _135 + _136
                _138 = _137 + -41
                _139 = a_t1qext[_138]
                _140 = j + -1
                _141 = _int(_140)
                _142 = _141 * 40
                _143 = _int(i)
                _144 = _142 + _143
                _145 = _144 + -41
                _146 = a_t1qext[_145]
                _147 = _139 - _146
                _148 = _147
                _149 = ratio * _148
                t1xv = _f32(_133 + _149)
                _150 = j + -1
                _151 = _int(_150)
                _152 = _151 * 40
                _153 = _int(i)
                _154 = _152 + _153
                _155 = _154 + -41
                _156 = a_t2qext[_155]
                _157 = _int(j)
                _158 = _157 * 40
                _159 = _int(i)
                _160 = _158 + _159
                _161 = _160 + -41
                _162 = a_t2qext[_161]
                _163 = j + -1
                _164 = _int(_163)
                _165 = _164 * 40
                _166 = _int(i)
                _167 = _165 + _166
                _168 = _167 + -41
                _169 = a_t2qext[_168]
                _170 = _162 - _169
                _171 = _170
                _172 = ratio * _171
                t2xv = _f32(_156 + _172)
                _173 = j + -1
                _174 = _int(_173)
                _175 = _174 * 40
                _176 = _int(i)
                _177 = _175 + _176
                _178 = _177 + -41
                _179 = a_t3qext[_178]
                _180 = _int(j)
                _181 = _180 * 40
                _182 = _int(i)
                _183 = _181 + _182
                _184 = _183 + -41
                _185 = a_t3qext[_184]
                _186 = j + -1
                _187 = _int(_186)
                _188 = _187 * 40
                _189 = _int(i)
                _190 = _188 + _189
                _191 = _190 + -41
                _192 = a_t3qext[_191]
                _193 = _185 - _192
                _194 = _193
                _195 = ratio * _194
                t3xv = _f32(_179 + _195)
                _196 = j + -1
                _197 = _int(_196)
                _198 = _197 * 40
                _199 = _int(i)
                _200 = _198 + _199
                _201 = _200 + -41
                _202 = a_t1qabs[_201]
                _203 = _int(j)
                _204 = _203 * 40
                _205 = _int(i)
                _206 = _204 + _205
                _207 = _206 + -41
                _208 = a_t1qabs[_207]
                _209 = j + -1
                _210 = _int(_209)
                _211 = _210 * 40
                _212 = _int(i)
                _213 = _211 + _212
                _214 = _213 + -41
                _215 = a_t1qabs[_214]
                _216 = _208 - _215
                _217 = _216
                _218 = ratio * _217
                t1av = _f32(_202 + _218)
                _219 = j + -1
                _220 = _int(_219)
                _221 = _220 * 40
                _222 = _int(i)
                _223 = _221 + _222
                _224 = _223 + -41
                _225 = a_t2qabs[_224]
                _226 = _int(j)
                _227 = _226 * 40
                _228 = _int(i)
                _229 = _227 + _228
                _230 = _229 + -41
                _231 = a_t2qabs[_230]
                _232 = j + -1
                _233 = _int(_232)
                _234 = _233 * 40
                _235 = _int(i)
                _236 = _234 + _235
                _237 = _236 + -41
                _238 = a_t2qabs[_237]
                _239 = _231 - _238
                _240 = _239
                _241 = ratio * _240
                t2av = _f32(_225 + _241)
                _242 = j + -1
                _243 = _int(_242)
                _244 = _243 * 40
                _245 = _int(i)
                _246 = _244 + _245
                _247 = _246 + -41
                _248 = a_t3qabs[_247]
                _249 = _int(j)
                _250 = _249 * 40
                _251 = _int(i)
                _252 = _250 + _251
                _253 = _252 + -41
                _254 = a_t3qabs[_253]
                _255 = j + -1
                _256 = _int(_255)
                _257 = _256 * 40
                _258 = _int(i)
                _259 = _257 + _258
                _260 = _259 + -41
                _261 = a_t3qabs[_260]
                _262 = _254 - _261
                _263 = _262
                _264 = ratio * _263
                t3av = _f32(_248 + _264)
                _265 = t1xv
                _266 = __builtin_powf(1.0e+1, _265)
                _267 = a1 * _266
                _268 = t2xv
                _269 = __builtin_powf(1.0e+1, _268)
                _270 = a2 * _269
                _271 = _267 + _270
                _272 = t3xv
                _273 = __builtin_powf(1.0e+1, _272)
                _274 = a3 * _273
                _275 = _int(i)
                _276 = _275 * 5
                _277 = nl[0]
                _278 = _int(_277)
                _279 = _276 + _278
                _280 = _279 + -6
                _281 = _271 + _274
                bext[_280] = _281
                _282 = t1av
                _283 = __builtin_powf(1.0e+1, _282)
                _284 = a1 * _283
                _285 = t2av
                _286 = __builtin_powf(1.0e+1, _285)
                _287 = a2 * _286
                _288 = _284 + _287
                _289 = t3av
                _290 = __builtin_powf(1.0e+1, _289)
                _291 = a3 * _290
                _292 = _int(i)
                _293 = _292 * 5
                _294 = nl[0]
                _295 = _int(_294)
                _296 = _293 + _295
                _297 = _296 + -6
                _298 = _288 + _291
                babs[_297] = _298
                _pc = 27
            case 27:  # L.1185
                i = _int(i + 1)
                _pc = 25
                continue
            case 28:  # L.1186
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_laycld(_state, k, cldatz, rratz, icld1, gndalt, rainrt):
    mdata_cld = _state.view(151120, '<f4')
    mdata_rr = _state.view(152520, '<f4')
    model_zmdl = _state.view(231904, '<f4')
    model_cldamt = _state.view(241016, '<f4')
    model_rramt = _state.view(241152, '<f4')
    cldtp = _state.view(181824, '<f4')
    delz = _state.view(181920, '<f4')
    zcld = _state.view(181856, '<f4')
    fac = _ZERO32
    icld = 0
    mc = 0
    mk = 0
    mr = 0
    zdif = _ZERO32
    zk = _ZERO32
    D_15570 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                icld = _int(icld1[0])
                _pc = 1 if icld == 0 else 2
                continue
            case 1:  # <D.20266>
                return
            case 2:  # L.1187
                _pc = 3 if icld > 11 else 4
                continue
            case 3:  # <D.20268>
                return
            case 4:  # L.1188
                _1 = k[0]
                _2 = _int(_1)
                _3 = _2 + -1
                _4 = model_zmdl[_3]
                _5 = gndalt[0]
                zk = _f32(_4 - _5)
                _pc = 5 if zk < 0.0 else 6
                continue
            case 5:  # <D.20270>
                zk = _f32(0.0)
                _pc = 6
                continue
            case 6:  # L.1189
                _6 = k[0]
                _7 = _int(_6)
                _8 = _7 + -1
                _9 = model_zmdl[_8]
                _pc = 7 if _9 > 6.0e+0 else 8
                continue
            case 7:  # <D.20273>
                _10 = k[0]
                _11 = _int(_10)
                _12 = _11 + -1
                zk = _f32(model_zmdl[_12])
                _pc = 8
                continue
            case 8:  # L.1190
                _pc = 9 if icld > 5 else 10
                continue
            case 9:  # <D.20276>
                _pc = 11
                continue
            case 10:  # L.1191
                mc = _int(icld)
                mr = _int(6)
                _pc = 18
                continue
            case 11:  # __label_000015
                _pc = 12 if icld == 6 else 13
                continue
            case 12:  # <D.20278>
                mc = _int(3)
                _pc = 13
                continue
            case 13:  # L.1192
                _13 = icld == 7
                _14 = icld == 8
                _15 = _13 | _14
                _pc = 14 if _15 != 0 else 15
                continue
            case 14:  # <D.20281>
                mc = _int(5)
                _pc = 15
                continue
            case 15:  # L.1193
                _pc = 16 if icld > 8 else 17
                continue
            case 16:  # <D.20284>
                mc = _int(1)
                _pc = 17
                continue
            case 17:  # L.1194
                mr = _int(icld + -5)
                _pc = 18
            case 18:  # __label_000025
                cldtp_776_16 = cldtp[0]
                _pc = 19 if zk > cldtp_776_16 else 20
                continue
            case 19:  # <D.20287>
                _pc = 39
                continue
            case 20:  # L.1195
                cldatz[0] = 0.0
                rratz[0] = 0.0
                _pc = 21 if zk <= 1.0e+1 else 22
                continue
            case 21:  # <D.20289>
                _17 = rainrt[0]
                rratz[0] = _17
                _pc = 22
                continue
            case 22:  # L.1196
                _pc = 23 if mc <= 0 else 24
                continue
            case 23:  # <D.20292>
                _pc = 38
                continue
            case 24:  # L.1197
                mk = _int(1)
                _pc = 25
            case 25:  # <D.20294>
                D_15570 = _int(mk > 15)
                _pc = 38 if D_15570 != 0 else 26
                continue
            case 26:  # <D.20295>
                _18 = mk + 1
                _19 = _int(_18)
                _20 = _19 + -1
                _21 = zcld[_20]
                _pc = 27 if zk >= _21 else 28
                continue
            case 27:  # <D.20296>
                _pc = 37
                continue
            case 28:  # L.1200
                _22 = _int(mk)
                _23 = _22 + -1
                _24 = zcld[_23]
                _pc = 29 if zk < _24 else 30
                continue
            case 29:  # <D.20298>
                _pc = 37
                continue
            case 30:  # L.1201
                _25 = _int(mk)
                _26 = _25 + -1
                _27 = zcld[_26]
                _28 = zk - _27
                _29 = abs(_28)
                delz_777_30 = delz[0]
                _pc = 31 if _29 < delz_777_30 else 32
                continue
            case 31:  # <D.20300>
                _pc = 33
                continue
            case 32:  # L.1202
                _pc = 34
                continue
            case 33:  # __label_000027
                _31 = _int(mc)
                _32 = _31 * 50
                _33 = _int(mk)
                _34 = _32 + _33
                _35 = _34 + -51
                _36 = mdata_cld[_35]
                cldatz[0] = _36
                _37 = _int(mr)
                _38 = _37 * 50
                _39 = _int(mk)
                _40 = _38 + _39
                _41 = _40 + -51
                _42 = mdata_rr[_41]
                rratz[0] = _42
                _pc = 38
                continue
            case 34:  # __label_000028
                _43 = mk + 1
                _44 = _int(_43)
                _45 = _44 + -1
                _46 = zcld[_45]
                _47 = _int(mk)
                _48 = _47 + -1
                _49 = zcld[_48]
                zdif = _f32(_46 - _49)
                delz_778_50 = delz[0]
                _pc = 35 if zdif < delz_778_50 else 36
                continue
            case 35:  # <D.20302>
                _pc = 33
                continue
            case 36:  # L.1203
                _51 = mk + 1
                _52 = _int(_51)
                _53 = _52 + -1
                _54 = zcld[_53]
                _55 = _54 - zk
                _56 = _55
                fac = _f32(_div(_56, zdif))
                _57 = _int(mc)
                _58 = _57 * 50
                _59 = mk + 1
                _60 = _int(_59)
                _61 = _58 + _60
                _62 = _61 + -51
                _63 = mdata_cld[_62]
                _64 = _int(mc)
                _65 = _64 * 50
                _66 = _int(mk)
                _67 = _65 + _66
                _68 = _67 + -51
                _69 = mdata_cld[_68]
                _70 = _int(mc)
                _71 = _70 * 50
                _72 = mk + 1
                _73 = _int(_72)
                _74 = _71 + _73
                _75 = _74 + -51
                _76 = mdata_cld[_75]
                _77 = _69 - _76
                _78 = _77
                _79 = fac * _78
                _80 = _63 + _79
                cldatz[0] = _80
                _81 = _int(mr)
                _82 = _81 * 50
                _83 = mk + 1
                _84 = _int(_83)
                _85 = _82 + _84
                _86 = _85 + -51
                _87 = mdata_rr[_86]
                _88 = _int(mr)
                _89 = _88 * 50
                _90 = _int(mk)
                _91 = _89 + _90
                _92 = _91 + -51
                _93 = mdata_rr[_92]
                _94 = _int(mr)
                _95 = _94 * 50
                _96 = mk + 1
                _97 = _int(_96)
                _98 = _95 + _97
                _99 = _98 + -51
                _100 = mdata_rr[_99]
                _101 = _93 - _100
                _102 = _101
                _103 = fac * _102
                _104 = _87 + _103
                rratz[0] = _104
                _pc = 38
                continue
            case 37:  # L.1198
                mk = _int(mk + 1)
                _pc = 25
                continue
            case 38:  # __label_000029
                _105 = k[0]
                _106 = _int(_105)
                _107 = _106 + -1
                _108 = cldatz[0]
                model_cldamt[_107] = _108
                _109 = k[0]
                _110 = _int(_109)
                _111 = _110 + 299
                _112 = cldatz[0]
                mdata_cld[_111] = _112
                _113 = k[0]
                _114 = _int(_113)
                _115 = _114 + 299
                _116 = rratz[0]
                mdata_rr[_115] = _116
                _117 = k[0]
                _118 = _int(_117)
                _119 = _118 + -1
                _120 = rratz[0]
                model_rramt[_119] = _120
                return
            case 39:  # __label_000030
                _121 = k[0]
                _122 = _int(_121)
                _123 = _122 + -1
                model_cldamt[_123] = 0.0
                _124 = k[0]
                _125 = _int(_124)
                _126 = _125 + -1
                model_rramt[_126] = 0.0
                cldatz[0] = 0.0
                rratz[0] = 0.0
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_layvsa(_state, k, rh, ahaze, iha1):
    card1_model = _state.view(209568, '<i4')
    model_z = _state.view(231904, '<f4')
    zvsaly_zvsa = _state.view(245664, '<f4')
    zvsaly_rhvsa = _state.view(245704, '<f4')
    zvsaly_ahvsa = _state.view(245744, '<f4')
    zvsaly_ihvsa = _state.view(245784, '<i4')
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                rh[0] = 0.0
                ahaze[0] = 0.0
                iha1[0] = 0
                _1 = card1_model[0]
                _2 = _1 == 0
                _3 = card1_model[0]
                _4 = _3 == 7
                _5 = _2 | _4
                _pc = 1 if _5 != 0 else 2
                continue
            case 1:  # <D.20305>
                return
            case 2:  # L.1204
                _6 = k[0]
                _pc = 3 if _6 > 9 else 4
                continue
            case 3:  # <D.20307>
                return
            case 4:  # L.1205
                _7 = k[0]
                _8 = _int(_7)
                _9 = _8 + -1
                _10 = k[0]
                _11 = _int(_10)
                _12 = _11 + -1
                _13 = zvsaly_zvsa[_9]
                model_z[_12] = _13
                _14 = k[0]
                _15 = _int(_14)
                _16 = _15 + -1
                _17 = zvsaly_rhvsa[_16]
                rh[0] = _17
                _18 = k[0]
                _19 = _int(_18)
                _20 = _19 + -1
                _21 = zvsaly_ahvsa[_20]
                ahaze[0] = _21
                _22 = k[0]
                _23 = _int(_22)
                _24 = _23 + -1
                _25 = zvsaly_ihvsa[_24]
                iha1[0] = _25
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_vsansm(_state, k, ahaze, iha1):
    __BLNK___whno3 = _state.view(265704, '<f4')
    card1b_jlow = _state.view(209744, '<i4')
    cntrl_ml = _state.view(245616, '<i4')
    mdata_z = _state.view(149120, '<f4')
    mdata_p = _state.view(149320, '<f4')
    mdata_t = _state.view(149520, '<f4')
    mdata_wh = _state.view(149720, '<f4')
    mdata_wco2 = _state.view(149920, '<f4')
    mdata_wo = _state.view(150120, '<f4')
    mdata_wn2o = _state.view(150320, '<f4')
    mdata_wco = _state.view(150520, '<f4')
    mdata_wch4 = _state.view(150720, '<f4')
    mdata_wo2 = _state.view(150920, '<f4')
    mdata1_wno = _state.view(286880, '<f4')
    mdata1_wso2 = _state.view(287080, '<f4')
    mdata1_wno2 = _state.view(287280, '<f4')
    mdata1_wnh3 = _state.view(287480, '<f4')
    mdata1_wair = _state.view(287680, '<f4')
    nsinp_zmdl = _state.view(243040, '<f4')
    nsinp_pm = _state.view(243200, '<f4')
    nsinp_tm = _state.view(243360, '<f4')
    nsinp_wmdl = _state.view(243520, '<f4')
    zvsaly_zvsa = _state.view(245664, '<f4')
    zvsaly_ahvsa = _state.view(245744, '<f4')
    zvsaly_ihvsa = _state.view(245784, '<i4')
    dif = _ZERO32
    dlin = _ZERO32
    dz = _ZERO32
    fac = _ZERO32
    j = 0
    jl = 0
    jls = 0
    jml = 0
    jp = 0
    km = 0
    kn = 0
    wmol = _zeros(13, '<f4')
    D_15951 = 0
    D_15954 = _ZERO32
    D_15956 = _ZERO32
    D_15959 = 0
    D_15961 = _ZERO32
    D_15966 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                jml = _int(cntrl_ml[0])
                j = _int(1)
                kn = _int(k[0])
                _pc = 1
            case 1:  # __label_000110
                _pc = 2 if kn > 10 else 3
                continue
            case 2:  # <D.20310>
                _pc = 28
                continue
            case 3:  # L.1206
                jl = _int(j + -1)
                _pc = 4 if jl <= 0 else 5
                continue
            case 4:  # <D.20312>
                jl = _int(1)
                _pc = 5
                continue
            case 5:  # L.1207
                jp = _int(jl + 1)
                jls = _int(jl)
                _1 = _int(kn)
                _2 = _1 + -1
                _3 = zvsaly_zvsa[_2]
                _4 = _int(jl)
                _5 = _4 + -1
                _6 = nsinp_zmdl[_5]
                _pc = 6 if _3 == _6 else 7
                continue
            case 6:  # <D.20315>
                _pc = 28
                continue
            case 7:  # L.1208
                jls = _int(jp)
                _7 = _int(kn)
                _8 = _7 + -1
                _9 = zvsaly_zvsa[_8]
                _10 = _int(jp)
                _11 = _10 + -1
                _12 = nsinp_zmdl[_11]
                _pc = 8 if _9 == _12 else 9
                continue
            case 8:  # <D.20317>
                _pc = 28
                continue
            case 9:  # L.1209
                _13 = _int(kn)
                _14 = _13 + -1
                _15 = zvsaly_zvsa[_14]
                _16 = _int(jl)
                _17 = _16 + -1
                _18 = nsinp_zmdl[_17]
                _19 = _15 > _18
                _20 = _int(kn)
                _21 = _20 + -1
                _22 = zvsaly_zvsa[_21]
                _23 = _int(jp)
                _24 = _23 + -1
                _25 = nsinp_zmdl[_24]
                _26 = _22 < _25
                _27 = _19 & _26
                _pc = 10 if _27 != 0 else 11
                continue
            case 10:  # <D.20319>
                _pc = 14
                continue
            case 11:  # L.1210
                _pc = 12 if j >= jml else 13
                continue
            case 12:  # <D.20321>
                _pc = 14
                continue
            case 13:  # L.1211
                j = _int(j + 1)
                _pc = 1
                continue
            case 14:  # __label_000115
                _28 = _int(kn)
                _29 = _28 + -1
                _30 = k[0]
                _31 = _int(_30)
                _32 = _31 + -1
                _33 = zvsaly_zvsa[_29]
                mdata_z[_32] = _33
                _34 = _int(jp)
                _35 = _34 + -1
                _36 = nsinp_zmdl[_35]
                _37 = _int(jl)
                _38 = _37 + -1
                _39 = nsinp_zmdl[_38]
                dif = _f32(_36 - _39)
                _40 = _int(kn)
                _41 = _40 + -1
                _42 = zvsaly_zvsa[_41]
                _43 = _int(jl)
                _44 = _43 + -1
                _45 = nsinp_zmdl[_44]
                dz = _f32(_42 - _45)
                dlin = _f32(_div(dz, dif))
                _46 = _int(jp)
                _47 = _46 + -1
                _48 = nsinp_pm[_47]
                _49 = _int(jl)
                _50 = _49 + -1
                _51 = nsinp_pm[_50]
                _52 = _48 - _51
                _53 = _52
                _54 = dlin * _53
                _55 = _int(jl)
                _56 = _55 + -1
                _57 = nsinp_pm[_56]
                _58 = k[0]
                _59 = _int(_58)
                _60 = _59 + -1
                _61 = _54 + _57
                mdata_p[_60] = _61
                _62 = _int(jp)
                _63 = _62 + -1
                _64 = nsinp_tm[_63]
                _65 = _int(jl)
                _66 = _65 + -1
                _67 = nsinp_tm[_66]
                _68 = _64 - _67
                _69 = _68
                _70 = dlin * _69
                _71 = _int(jl)
                _72 = _71 + -1
                _73 = nsinp_tm[_72]
                _74 = k[0]
                _75 = _int(_74)
                _76 = _75 + -1
                _77 = _70 + _73
                mdata_t[_76] = _77
                km = _int(1)
                _pc = 15
            case 15:  # <D.20323>
                D_15951 = _int(km > 13)
                _pc = 18 if D_15951 != 0 else 16
                continue
            case 16:  # <D.20324>
                _78 = _int(km)
                _79 = _78 * 40
                _80 = _int(jp)
                _81 = _79 + _80
                _82 = _81 + -41
                _83 = nsinp_wmdl[_82]
                _84 = _int(km)
                _85 = _84 * 40
                _86 = _int(jl)
                _87 = _85 + _86
                _88 = _87 + -41
                _89 = nsinp_wmdl[_88]
                _90 = _83 - _89
                _91 = _90
                _92 = dlin * _91
                _93 = _int(km)
                _94 = _93 * 40
                _95 = _int(jl)
                _96 = _94 + _95
                _97 = _96 + -41
                _98 = nsinp_wmdl[_97]
                _99 = _int(km)
                _100 = _99 + -1
                _101 = _92 + _98
                wmol[_100] = _101
                _pc = 17
            case 17:  # L.1212
                km = _int(km + 1)
                _pc = 15
                continue
            case 18:  # L.1213
                _102 = _int(kn)
                _103 = _102 + -1
                _104 = zvsaly_ihvsa[_103]
                iha1[0] = _104
                _105 = _int(kn)
                _106 = _105 + -1
                _107 = zvsaly_ahvsa[_106]
                ahaze[0] = _107
                _108 = _int(kn)
                _109 = _108 + -1
                _110 = zvsaly_zvsa[_109]
                _111 = _int(jl)
                _112 = _111 + -1
                _113 = nsinp_zmdl[_112]
                _114 = _110 - _113
                _115 = _114
                fac = _f32(_div(_115, dif))
                _116 = _int(jp)
                _117 = _116 + -1
                _118 = nsinp_pm[_117]
                _119 = _118 > 0.0
                _120 = _int(jl)
                _121 = _120 + -1
                _122 = nsinp_pm[_121]
                _123 = _122 > 0.0
                _124 = _119 & _123
                _pc = 19 if _124 != 0 else 20
                continue
            case 19:  # <D.20325>
                _125 = _int(jp)
                _126 = _125 + -1
                _127 = nsinp_pm[_126]
                _128 = _int(jl)
                _129 = _128 + -1
                _130 = nsinp_pm[_129]
                _131 = _div(_127, _130)
                D_15954 = _f32(_131)
                _132 = _int(jl)
                _133 = _132 + -1
                _134 = nsinp_pm[_133]
                _135 = __builtin_powf(D_15954, fac)
                _136 = k[0]
                _137 = _int(_136)
                _138 = _137 + -1
                _139 = _134 * _135
                mdata_p[_138] = _139
                _pc = 20
                continue
            case 20:  # L.1214
                _140 = _int(jp)
                _141 = _140 + -1
                _142 = nsinp_tm[_141]
                _143 = _142 > 0.0
                _144 = _int(jl)
                _145 = _144 + -1
                _146 = nsinp_tm[_145]
                _147 = _146 > 0.0
                _148 = _143 & _147
                _pc = 21 if _148 != 0 else 22
                continue
            case 21:  # <D.20328>
                _149 = _int(jp)
                _150 = _149 + -1
                _151 = nsinp_tm[_150]
                _152 = _int(jl)
                _153 = _152 + -1
                _154 = nsinp_tm[_153]
                _155 = _div(_151, _154)
                D_15956 = _f32(_155)
                _156 = _int(jl)
                _157 = _156 + -1
                _158 = nsinp_tm[_157]
                _159 = __builtin_powf(D_15956, fac)
                _160 = k[0]
                _161 = _int(_160)
                _162 = _161 + -1
                _163 = _158 * _159
                mdata_t[_162] = _163
                _pc = 22
                continue
            case 22:  # L.1215
                km = _int(1)
                _pc = 23
            case 23:  # <D.20331>
                D_15959 = _int(km > 13)
                _pc = 27 if D_15959 != 0 else 24
                continue
            case 24:  # <D.20332>
                _164 = _int(km)
                _165 = _164 * 40
                _166 = _int(jp)
                _167 = _165 + _166
                _168 = _167 + -41
                _169 = nsinp_wmdl[_168]
                _170 = _169 > 0.0
                _171 = _int(km)
                _172 = _171 * 40
                _173 = _int(jl)
                _174 = _172 + _173
                _175 = _174 + -41
                _176 = nsinp_wmdl[_175]
                _177 = _176 > 0.0
                _178 = _170 & _177
                _pc = 25 if _178 != 0 else 26
                continue
            case 25:  # <D.20333>
                _179 = _int(km)
                _180 = _179 * 40
                _181 = _int(jl)
                _182 = _180 + _181
                _183 = _182 + -41
                _184 = nsinp_wmdl[_183]
                _185 = _int(km)
                _186 = _185 * 40
                _187 = _int(jp)
                _188 = _186 + _187
                _189 = _188 + -41
                _190 = nsinp_wmdl[_189]
                _191 = _190
                _192 = _184 * _191
                _193 = _int(km)
                _194 = _193 * 40
                _195 = _int(jl)
                _196 = _194 + _195
                _197 = _196 + -41
                _198 = nsinp_wmdl[_197]
                _199 = _div(_192, _198)
                D_15961 = _f32(_199)
                _200 = _int(km)
                _201 = _200 + -1
                _202 = __builtin_powf(D_15961, fac)
                wmol[_201] = _202
                _pc = 26
                continue
            case 26:  # L.1216
                km = _int(km + 1)
                _pc = 23
                continue
            case 27:  # L.1217
                _203 = k[0]
                _204 = _int(_203)
                _205 = _204 + -1
                _206 = wmol[0]
                mdata_wh[_205] = _206
                _207 = k[0]
                _208 = _int(_207)
                _209 = _208 + -1
                _210 = wmol[1]
                mdata_wco2[_209] = _210
                _211 = k[0]
                _212 = _int(_211)
                _213 = _212 + -1
                _214 = wmol[2]
                mdata_wo[_213] = _214
                _215 = k[0]
                _216 = _int(_215)
                _217 = _216 + -1
                _218 = wmol[3]
                mdata_wn2o[_217] = _218
                _219 = k[0]
                _220 = _int(_219)
                _221 = _220 + -1
                _222 = wmol[4]
                mdata_wco[_221] = _222
                _223 = k[0]
                _224 = _int(_223)
                _225 = _224 + -1
                _226 = wmol[5]
                mdata_wch4[_225] = _226
                _227 = k[0]
                _228 = _int(_227)
                _229 = _228 + -1
                _230 = wmol[6]
                mdata_wo2[_229] = _230
                _231 = k[0]
                _232 = _int(_231)
                _233 = _232 + -1
                _234 = wmol[7]
                mdata1_wno[_233] = _234
                _235 = k[0]
                _236 = _int(_235)
                _237 = _236 + -1
                _238 = wmol[8]
                mdata1_wso2[_237] = _238
                _239 = k[0]
                _240 = _int(_239)
                _241 = _240 + -1
                _242 = wmol[9]
                mdata1_wno2[_241] = _242
                _243 = k[0]
                _244 = _int(_243)
                _245 = _244 + -1
                _246 = wmol[10]
                mdata1_wnh3[_245] = _246
                _247 = k[0]
                _248 = _int(_247)
                _249 = _248 + -1
                _250 = wmol[11]
                __BLNK___whno3[_249] = _250
                _251 = k[0]
                _252 = _int(_251)
                _253 = _252 + -1
                _254 = wmol[12]
                mdata1_wair[_253] = _254
                return
            case 28:  # __label_000140
                j = _int(jls)
                _255 = k[0]
                _pc = 29 if _255 > 10 else 30
                continue
            case 29:  # <D.20336>
                _256 = k[0]
                _257 = _256 + -10
                _258 = card1b_jlow[0]
                j = _int(_257 + _258)
                iha1[0] = 0
                ahaze[0] = 0.0
                _pc = 30
                continue
            case 30:  # L.1219
                _259 = _int(j)
                _260 = _259 + -1
                _261 = k[0]
                _262 = _int(_261)
                _263 = _262 + -1
                _264 = nsinp_zmdl[_260]
                mdata_z[_263] = _264
                _265 = _int(j)
                _266 = _265 + -1
                _267 = k[0]
                _268 = _int(_267)
                _269 = _268 + -1
                _270 = nsinp_pm[_266]
                mdata_p[_269] = _270
                _271 = _int(j)
                _272 = _271 + -1
                _273 = k[0]
                _274 = _int(_273)
                _275 = _274 + -1
                _276 = nsinp_tm[_272]
                mdata_t[_275] = _276
                km = _int(1)
                _pc = 31
            case 31:  # <D.20339>
                D_15966 = _int(km > 13)
                _pc = 34 if D_15966 != 0 else 32
                continue
            case 32:  # <D.20340>
                _277 = _int(km)
                _278 = _277 * 40
                _279 = _int(j)
                _280 = _278 + _279
                _281 = _280 + -41
                _282 = _int(km)
                _283 = _282 + -1
                _284 = nsinp_wmdl[_281]
                wmol[_283] = _284
                _pc = 33
            case 33:  # L.1220
                km = _int(km + 1)
                _pc = 31
                continue
            case 34:  # L.1221
                _285 = k[0]
                _286 = _int(_285)
                _287 = _286 + -1
                _288 = wmol[0]
                mdata_wh[_287] = _288
                _289 = k[0]
                _290 = _int(_289)
                _291 = _290 + -1
                _292 = wmol[1]
                mdata_wco2[_291] = _292
                _293 = k[0]
                _294 = _int(_293)
                _295 = _294 + -1
                _296 = wmol[2]
                mdata_wo[_295] = _296
                _297 = k[0]
                _298 = _int(_297)
                _299 = _298 + -1
                _300 = wmol[3]
                mdata_wn2o[_299] = _300
                _301 = k[0]
                _302 = _int(_301)
                _303 = _302 + -1
                _304 = wmol[4]
                mdata_wco[_303] = _304
                _305 = k[0]
                _306 = _int(_305)
                _307 = _306 + -1
                _308 = wmol[5]
                mdata_wch4[_307] = _308
                _309 = k[0]
                _310 = _int(_309)
                _311 = _310 + -1
                _312 = wmol[6]
                mdata_wo2[_311] = _312
                _313 = k[0]
                _314 = _int(_313)
                _315 = _314 + -1
                _316 = wmol[7]
                mdata1_wno[_315] = _316
                _317 = k[0]
                _318 = _int(_317)
                _319 = _318 + -1
                _320 = wmol[8]
                mdata1_wso2[_319] = _320
                _321 = k[0]
                _322 = _int(_321)
                _323 = _322 + -1
                _324 = wmol[9]
                mdata1_wno2[_323] = _324
                _325 = k[0]
                _326 = _int(_325)
                _327 = _326 + -1
                _328 = wmol[10]
                mdata1_wnh3[_327] = _328
                _329 = k[0]
                _330 = _int(_329)
                _331 = _330 + -1
                _332 = wmol[11]
                __BLNK___whno3[_331] = _332
                _333 = k[0]
                _334 = _int(_333)
                _335 = _334 + -1
                _336 = wmol[12]
                mdata1_wair[_335] = _336
                _pc = 35 if kn <= 9 else 36
                continue
            case 35:  # <D.20341>
                _337 = _int(kn)
                _338 = _337 + -1
                _339 = zvsaly_ihvsa[_338]
                iha1[0] = _339
                _pc = 36
                continue
            case 36:  # L.1222
                _pc = 37 if kn <= 9 else -1
                continue
            case 37:  # <D.20344>
                _340 = _int(kn)
                _341 = _340 + -1
                _342 = zvsaly_ahvsa[_341]
                ahaze[0] = _342
                _pc = -1
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_convrt(_state, p, t):
    card1b_junit1 = _state.view(209640, '<i4')
    card1b_wmol1 = _state.view(209692, '<f4')
    constn_pzero = _state.view(2304, '<f4')
    constn_tzero = _state.view(2308, '<f4')
    constn_avogad = _state.view(2312, '<f4')
    constn_alosmt = _state.view(2316, '<f4')
    constn_airmwt = _state.view(2348, '<f4')
    constn_amwt = _state.view(2352, '<f4')
    b = _ZERO32
    junit = 0
    k = 0
    r = _ZERO32
    rhoair = _ZERO32
    wmol = _ZERO32
    wtem = _ZERO32
    D_16034 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = p[0]
                _2 = constn_pzero[0]
                _3 = _div(_1, _2)
                _4 = _3
                _5 = constn_alosmt[0]
                _6 = _4 * _5
                _7 = constn_tzero[0]
                _8 = t[0]
                _9 = _div(_7, _8)
                _10 = _9
                rhoair = _f32(_6 * _10)
                k = _int(1)
                _pc = 1
            case 1:  # <D.20350>
                D_16034 = _int(k > 12)
                _pc = 23 if D_16034 != 0 else 2
                continue
            case 2:  # <D.20351>
                _11 = constn_avogad[0]
                _12 = _int(k)
                _13 = _12 + -1
                _14 = constn_amwt[_13]
                b = _f32(_div(_11, _14))
                _15 = constn_airmwt[0]
                _16 = _int(k)
                _17 = _16 + -1
                _18 = constn_amwt[_17]
                r = _f32(_div(_15, _18))
                _19 = _int(k)
                _20 = _19 + -1
                junit = _int(card1b_junit1[_20])
                _21 = _int(k)
                _22 = _21 + -1
                wmol = _f32(card1b_wmol1[_22])
                _pc = 3 if k != 1 else 4
                continue
            case 3:  # <D.20352>
                _pc = 5
                continue
            case 4:  # L.1226
                _ft_watvap(_state, p, t)
                _pc = 22
                continue
            case 5:  # __label_000100
                _pc = 6 if junit > 10 else 7
                continue
            case 6:  # <D.20354>
                _pc = 8
                continue
            case 7:  # L.1227
                _pc = 22
                continue
            case 8:  # __label_000110
                _pc = 9 if junit != 11 else 10
                continue
            case 9:  # <D.20356>
                _pc = 11
                continue
            case 10:  # L.1228
                _23 = rhoair * 9.999999974752427078783512115478515625e-7
                _24 = _23
                _25 = _int(k)
                _26 = _25 + -1
                _27 = _div(wmol, _24)
                card1b_wmol1[_26] = _27
                _pc = 22
                continue
            case 11:  # __label_000120
                _pc = 12 if junit != 12 else 13
                continue
            case 12:  # <D.20358>
                _pc = 14
                continue
            case 13:  # L.1229
                _28 = r * wmol
                _29 = _int(k)
                _30 = _29 + -1
                _31 = _28 * 1.0e+3
                card1b_wmol1[_30] = _31
                _pc = 22
                continue
            case 14:  # __label_000130
                _pc = 15 if junit != 13 else 16
                continue
            case 15:  # <D.20360>
                _pc = 17
                continue
            case 16:  # L.1230
                _32 = b * wmol
                _33 = _int(k)
                _34 = _33 + -1
                _35 = _div(_32, rhoair)
                card1b_wmol1[_34] = _35
                _pc = 22
                continue
            case 17:  # __label_000140
                _pc = 18 if junit != 14 else 19
                continue
            case 18:  # <D.20362>
                _pc = 20
                continue
            case 19:  # L.1231
                _36 = constn_pzero[0]
                _37 = _div(wmol, _36)
                _38 = _37
                _39 = constn_alosmt[0]
                _40 = _38 * _39
                _41 = constn_tzero[0]
                _42 = t[0]
                _43 = _div(_41, _42)
                _44 = _43
                wtem = _f32(_40 * _44)
                _45 = rhoair * 9.999999974752427078783512115478515625e-7
                _46 = _45
                _47 = _int(k)
                _48 = _47 + -1
                _49 = _div(wtem, _46)
                card1b_wmol1[_48] = _49
                _pc = 22
                continue
            case 20:  # __label_000150
                _pc = 21 if junit > 14 else 22
                continue
            case 21:  # <D.20364>
                _pc = 24
                continue
            case 22:  # L.1224
                k = _int(k + 1)
                _pc = 1
                continue
            case 23:  # L.1225
                return
            case 24:  # __label_000951
                _gfortran_stop_numeric(-1, 0)
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_defalt(_state, z, p, t):
    card1b_junitp = _state.view(209632, '<i4')
    card1b_junitt = _state.view(209636, '<i4')
    card1b_junit = _state.view(209640, '<i4')
    card1b_wmol = _state.view(209692, '<f4')
    mlatm_alt = _state.view(153920, '<f4')
    mlatm_pmatm = _state.view(154120, '<f4')
    mlatm_tmatm = _state.view(155320, '<f4')
    mlatm_amol = _state.view(156520, '<f4')
    trac_trac = _state.view(166144, '<f4')
    a1 = _ZERO32
    a2 = _ZERO32
    a3 = _ZERO32
    a4 = _ZERO32
    den1 = _ZERO32
    den2 = _ZERO32
    den3 = _ZERO32
    den4 = _ZERO32
    i0 = 0
    i1 = 0
    i2 = 0
    i3 = 0
    ilower = 0
    im = 0
    im50 = 0
    itr = 0
    iupper = 0
    k = 0
    matm = 0
    nmol = 0
    x1 = _ZERO32
    x2 = _ZERO32
    x3 = _ZERO32
    x4 = _ZERO32
    z0 = _ZERO32
    z1 = _ZERO32
    z2 = _ZERO32
    z3 = _ZERO32
    D_16125 = 0
    D_16128 = 0
    a1_42 = _ZERO32
    a2_43 = _ZERO32
    a3_44 = _ZERO32
    a4_45 = _ZERO32
    x1_46 = _ZERO32
    x2_47 = _ZERO32
    x3_48 = _ZERO32
    x4_49 = _ZERO32
    a1_50 = _ZERO32
    a2_51 = _ZERO32
    a3_52 = _ZERO32
    a4_53 = _ZERO32
    x1_54 = _ZERO32
    x2_55 = _ZERO32
    x3_56 = _ZERO32
    x4_57 = _ZERO32
    D_16162 = 0
    D_16165 = 0
    a1_58 = _ZERO32
    a2_59 = _ZERO32
    a3_60 = _ZERO32
    a4_61 = _ZERO32
    x1_62 = _ZERO32
    x2_63 = _ZERO32
    x3_64 = _ZERO32
    x4_65 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                nmol = _int(12)
                ilower = _int(0)
                iupper = _int(0)
                im50 = _int(50)
                D_16125 = _int(im50)
                im = _int(2)
                _pc = 1
            case 1:  # <D.20367>
                D_16128 = _int(im > D_16125)
                _pc = 5 if D_16128 != 0 else 2
                continue
            case 2:  # <D.20368>
                i2 = _int(im)
                _1 = _int(im)
                _2 = _1 + -1
                _3 = mlatm_alt[_2]
                _4 = z[0]
                _pc = 3 if _3 >= _4 else 4
                continue
            case 3:  # <D.20369>
                _pc = 6
                continue
            case 4:  # L.1233
                im = _int(im + 1)
                _pc = 1
                continue
            case 5:  # L.1234
                i2 = _int(im50)
                _pc = 6
            case 6:  # __label_000020
                i1 = _int(i2 + -1)
                i0 = _int(i2 + -2)
                i3 = _int(i2 + 1)
                _pc = 7 if i0 <= 0 else 8
                continue
            case 7:  # <D.20371>
                _pc = 11
                continue
            case 8:  # L.1236
                _pc = 9 if i3 > im50 else 10
                continue
            case 9:  # <D.20373>
                _pc = 12
                continue
            case 10:  # L.1237
                _pc = 17
                continue
            case 11:  # __label_000025
                ilower = _int(1)
                i0 = _int(i1)
                i1 = _int(i2)
                i2 = _int(i3)
                i3 = _int(i3 + 1)
                _pc = 17
                continue
            case 12:  # __label_000026
                iupper = _int(1)
                _5 = z[0]
                _6 = _int(im50)
                _7 = _6 + -1
                _8 = mlatm_alt[_7]
                _pc = 13 if _5 > _8 else 14
                continue
            case 13:  # <D.20375>
                _pc = 15
                continue
            case 14:  # L.1238
                i3 = _int(i2)
                i2 = _int(i1)
                i1 = _int(i0)
                i0 = _int(i1 + -1)
                _pc = 17
                continue
            case 15:  # __label_000029
                _9 = _int(i0)
                _10 = _9 + -1
                z0 = _f32(mlatm_alt[_10])
                _11 = _int(i1)
                _12 = _11 + -1
                z1 = _f32(mlatm_alt[_12])
                _13 = _int(i2)
                _14 = _13 + -1
                z2 = _f32(mlatm_alt[_14])
                _15 = z[0]
                _16 = _15 - z2
                _17 = _16
                _18 = _17 * 2.0e+0
                z3 = _f32(z2 + _18)
                iupper = _int(2)
                _pc = 16
            case 16:  # __label_000080
                _gfortran_stop_string(b"DEFAULTZ", 8, 0)
                _pc = 17
            case 17:  # __label_000028
                _19 = _int(i1)
                _20 = _19 + -1
                z1 = _f32(mlatm_alt[_20])
                _21 = _int(i2)
                _22 = _21 + -1
                z2 = _f32(mlatm_alt[_22])
                _23 = _int(i0)
                _24 = _23 + -1
                z0 = _f32(mlatm_alt[_24])
                _25 = _int(i3)
                _26 = _25 + -1
                z3 = _f32(mlatm_alt[_26])
                _pc = 18
            case 18:  # __label_000031
                _27 = z0 - z1
                _28 = _27
                _29 = z0 - z2
                _30 = _29
                _31 = _28 * _30
                _32 = z0 - z3
                _33 = _32
                den1 = _f32(_31 * _33)
                _34 = z1 - z2
                _35 = _34
                _36 = z1 - z3
                _37 = _36
                _38 = _35 * _37
                _39 = z1 - z0
                _40 = _39
                den2 = _f32(_38 * _40)
                _41 = z2 - z3
                _42 = _41
                _43 = z2 - z0
                _44 = _43
                _45 = _42 * _44
                _46 = z2 - z1
                _47 = _46
                den3 = _f32(_45 * _47)
                _48 = z3 - z0
                _49 = _48
                _50 = z3 - z1
                _51 = _50
                _52 = _49 * _51
                _53 = z3 - z2
                _54 = _53
                den4 = _f32(_52 * _54)
                _55 = z[0]
                _56 = _55 - z1
                _57 = _56
                _58 = z[0]
                _59 = _58 - z2
                _60 = _59
                _61 = _57 * _60
                _62 = z[0]
                _63 = _62 - z3
                _64 = _63
                _65 = _61 * _64
                _66 = _65
                a1 = _f32(_div(_66, den1))
                _67 = z[0]
                _68 = _67 - z2
                _69 = _68
                _70 = z[0]
                _71 = _70 - z3
                _72 = _71
                _73 = _69 * _72
                _74 = z[0]
                _75 = _74 - z0
                _76 = _75
                _77 = _73 * _76
                _78 = _77
                a2 = _f32(_div(_78, den2))
                _79 = z[0]
                _80 = _79 - z3
                _81 = _80
                _82 = z[0]
                _83 = _82 - z0
                _84 = _83
                _85 = _81 * _84
                _86 = z[0]
                _87 = _86 - z1
                _88 = _87
                _89 = _85 * _88
                _90 = _89
                a3 = _f32(_div(_90, den3))
                _91 = z[0]
                _92 = _91 - z0
                _93 = _92
                _94 = z[0]
                _95 = _94 - z1
                _96 = _95
                _97 = _93 * _96
                _98 = z[0]
                _99 = _98 - z2
                _100 = _99
                _101 = _97 * _100
                _102 = _101
                a4 = _f32(_div(_102, den4))
                _103 = card1b_junitp[0]
                _pc = 19 if _103 > 6 else 20
                continue
            case 19:  # <D.20377>
                _pc = 23
                continue
            case 20:  # L.1239
                matm = _int(card1b_junitp[0])
                _104 = _int(matm)
                _105 = _104 * 50
                _106 = _int(i0)
                _107 = _105 + _106
                _108 = _107 + -51
                _109 = mlatm_pmatm[_108]
                x1 = _f32(__builtin_logf(_109))
                _110 = _int(matm)
                _111 = _110 * 50
                _112 = _int(i1)
                _113 = _111 + _112
                _114 = _113 + -51
                _115 = mlatm_pmatm[_114]
                x2 = _f32(__builtin_logf(_115))
                _116 = _int(matm)
                _117 = _116 * 50
                _118 = _int(i2)
                _119 = _117 + _118
                _120 = _119 + -51
                _121 = mlatm_pmatm[_120]
                x3 = _f32(__builtin_logf(_121))
                _122 = _int(matm)
                _123 = _122 * 50
                _124 = _int(i3)
                _125 = _123 + _124
                _126 = _125 + -51
                _127 = mlatm_pmatm[_126]
                x4 = _f32(__builtin_logf(_127))
                _pc = 21 if iupper == 2 else 22
                continue
            case 21:  # <D.20379>
                _128 = x3 - x2
                _129 = _128
                _130 = _129 * 2.0e+0
                x4 = _f32(x3 + _130)
                _pc = 22
                continue
            case 22:  # L.1240
                a1_42 = _f32(a1)
                a2_43 = _f32(a2)
                a3_44 = _f32(a3)
                a4_45 = _f32(a4)
                x1_46 = _f32(x1)
                x2_47 = _f32(x2)
                x3_48 = _f32(x3)
                x4_49 = _f32(x4)
                _131 = a1_42 * x1_46
                _132 = a2_43 * x2_47
                _133 = _131 + _132
                _134 = a3_44 * x3_48
                _135 = _133 + _134
                _136 = a4_45 * x4_49
                _137 = _135 + _136
                p[0] = _137
                _138 = p[0]
                _139 = __builtin_expf(_138)
                p[0] = _139
                _pc = 23
            case 23:  # __label_000035
                _140 = card1b_junitt[0]
                _pc = 24 if _140 > 6 else 25
                continue
            case 24:  # <D.20382>
                _pc = 26
                continue
            case 25:  # L.1241
                matm = _int(card1b_junitt[0])
                _141 = _int(matm)
                _142 = _141 * 50
                _143 = _int(i0)
                _144 = _142 + _143
                _145 = _144 + -51
                x1 = _f32(mlatm_tmatm[_145])
                _146 = _int(matm)
                _147 = _146 * 50
                _148 = _int(i1)
                _149 = _147 + _148
                _150 = _149 + -51
                x2 = _f32(mlatm_tmatm[_150])
                _151 = _int(matm)
                _152 = _151 * 50
                _153 = _int(i2)
                _154 = _152 + _153
                _155 = _154 + -51
                x3 = _f32(mlatm_tmatm[_155])
                _156 = _int(matm)
                _157 = _156 * 50
                _158 = _int(i3)
                _159 = _157 + _158
                _160 = _159 + -51
                x4 = _f32(mlatm_tmatm[_160])
                a1_50 = _f32(a1)
                a2_51 = _f32(a2)
                a3_52 = _f32(a3)
                a4_53 = _f32(a4)
                x1_54 = _f32(x1)
                x2_55 = _f32(x2)
                x3_56 = _f32(x3)
                x4_57 = _f32(x4)
                _161 = a1_50 * x1_54
                _162 = a2_51 * x2_55
                _163 = _161 + _162
                _164 = a3_52 * x3_56
                _165 = _163 + _164
                _166 = a4_53 * x4_57
                _167 = _165 + _166
                t[0] = _167
                _pc = 26
            case 26:  # __label_000040
                D_16162 = _int(nmol)
                k = _int(1)
                _pc = 27
            case 27:  # <D.20384>
                D_16165 = _int(k > D_16162)
                _pc = 36 if D_16165 != 0 else 28
                continue
            case 28:  # <D.20385>
                _168 = _int(k)
                _169 = _168 + -1
                _170 = card1b_junit[_169]
                _pc = 29 if _170 > 6 else 30
                continue
            case 29:  # <D.20386>
                _pc = 35
                continue
            case 30:  # L.1244
                _pc = 31 if k > 7 else 32
                continue
            case 31:  # <D.20388>
                _pc = 33
                continue
            case 32:  # L.1245
                _171 = _int(k)
                _172 = _171 + -1
                matm = _int(card1b_junit[_172])
                _173 = _int(matm)
                _174 = _173 * 400
                _175 = _int(k)
                _176 = _175 * 50
                _177 = _174 + _176
                _178 = _int(i0)
                _179 = _177 + _178
                _180 = _179 + -451
                x1 = _f32(mlatm_amol[_180])
                _181 = _int(matm)
                _182 = _181 * 400
                _183 = _int(k)
                _184 = _183 * 50
                _185 = _182 + _184
                _186 = _int(i1)
                _187 = _185 + _186
                _188 = _187 + -451
                x2 = _f32(mlatm_amol[_188])
                _189 = _int(matm)
                _190 = _189 * 400
                _191 = _int(k)
                _192 = _191 * 50
                _193 = _190 + _192
                _194 = _int(i2)
                _195 = _193 + _194
                _196 = _195 + -451
                x3 = _f32(mlatm_amol[_196])
                _197 = _int(matm)
                _198 = _197 * 400
                _199 = _int(k)
                _200 = _199 * 50
                _201 = _198 + _200
                _202 = _int(i3)
                _203 = _201 + _202
                _204 = _203 + -451
                x4 = _f32(mlatm_amol[_204])
                _pc = 34
                continue
            case 33:  # __label_000045
                itr = _int(k + -7)
                matm = _int(6)
                _205 = _int(itr)
                _206 = _205 * 50
                _207 = _int(i0)
                _208 = _206 + _207
                _209 = _208 + -51
                x1 = _f32(trac_trac[_209])
                _210 = _int(itr)
                _211 = _210 * 50
                _212 = _int(i1)
                _213 = _211 + _212
                _214 = _213 + -51
                x2 = _f32(trac_trac[_214])
                _215 = _int(itr)
                _216 = _215 * 50
                _217 = _int(i2)
                _218 = _216 + _217
                _219 = _218 + -51
                x3 = _f32(trac_trac[_219])
                _220 = _int(itr)
                _221 = _220 * 50
                _222 = _int(i3)
                _223 = _221 + _222
                _224 = _223 + -51
                x4 = _f32(trac_trac[_224])
                _pc = 34
            case 34:  # __label_000050
                a1_58 = _f32(a1)
                a2_59 = _f32(a2)
                a3_60 = _f32(a3)
                a4_61 = _f32(a4)
                x1_62 = _f32(x1)
                x2_63 = _f32(x2)
                x3_64 = _f32(x3)
                x4_65 = _f32(x4)
                _225 = a1_58 * x1_62
                _226 = a2_59 * x2_63
                _227 = _225 + _226
                _228 = a3_60 * x3_64
                _229 = _227 + _228
                _230 = a4_61 * x4_65
                _231 = _int(k)
                _232 = _231 + -1
                _233 = _229 + _230
                card1b_wmol[_232] = _233
                _234 = _int(k)
                _235 = _234 + -1
                card1b_junit[_235] = 10
                _pc = 35
                continue
            case 35:  # L.1242
                k = _int(k + 1)
                _pc = 27
                continue
            case 36:  # L.1243
                _236 = card1b_wmol[11]
                _237 = _236 * 1.0e+3
                card1b_wmol[11] = _237
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_check(_state, v, iv, key):
    degk = _state.view(181956, '<f4')
    pmb = _state.view(181948, '<f4')
    ptorr = _state.view(181952, '<f4')
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = iv[0]
                _pc = 1 if _1 <= 10 else 2
                continue
            case 1:  # <D.20391>
                return
            case 2:  # L.1246
                _2 = key[0]
                _pc = {1: 3, 2: 5, 3: 7}.get(_2, 9)
                continue
            case 3:  # L.1249
                _pc = 9
                continue
            case 4:  # continuation_8
                _pc = 9
                continue
            case 5:  # L.1250
                _pc = 16
                continue
            case 6:  # continuation_11
                _pc = 9
                continue
            case 7:  # L.1251
                _pc = 19
                continue
            case 8:  # continuation_14
                _pc = 9
                continue
            case 9:  # __label_000100
                _3 = iv[0]
                _pc = 10 if _3 == 11 else 11
                continue
            case 10:  # <D.20394>
                _pc = 14
                continue
            case 11:  # L.1252
                _4 = iv[0]
                _pc = 12 if _4 == 12 else 13
                continue
            case 12:  # <D.20396>
                _pc = 15
                continue
            case 13:  # L.1253
                _gfortran_stop_string(b"CHECK(P)", 8, 0)
                _pc = 14
            case 14:  # __label_000110
                _5 = v[0]
                pmb_779_6 = pmb[0]
                _7 = _5 * pmb_779_6
                v[0] = _7
                return
            case 15:  # __label_000120
                _8 = v[0]
                pmb_780_9 = pmb[0]
                _10 = _8 * pmb_780_9
                ptorr_781_11 = ptorr[0]
                _12 = _div(_10, ptorr_781_11)
                v[0] = _12
                return
            case 16:  # __label_000200
                _13 = iv[0]
                _pc = 17 if _13 > 11 else 18
                continue
            case 17:  # <D.20398>
                _gfortran_stop_string(b"CHECK(T)", 8, 0)
                _pc = 18
            case 18:  # L.1254
                _14 = v[0]
                degk_782_15 = degk[0]
                _16 = _14 + degk_782_15
                v[0] = _16
                return
            case 19:  # __label_000300
                _17 = iv[0]
                _pc = 20 if _17 == 11 else 21
                continue
            case 20:  # <D.20400>
                _pc = 24
                continue
            case 21:  # L.1255
                _18 = iv[0]
                _pc = 22 if _18 == 12 else 23
                continue
            case 22:  # <D.20402>
                _pc = 25
                continue
            case 23:  # L.1256
                _gfortran_stop_string(b"CHECK(R)", 8, 0)
                _pc = 24
            case 24:  # __label_000310
                _19 = v[0]
                _20 = _div(_19, 1.0e+3)
                v[0] = _20
                return
            case 25:  # __label_000320
                _21 = v[0]
                _22 = _div(_21, 1.0e+5)
                v[0] = _22
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_jou(_state, char, _char):
    holvec = _state.view(181968, 'S1')
    indx1 = _state.view(182016, '<i4')
    D_20411 = 0
    i = 0
    indx = 0
    __result_jou = 0
    D_16222 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                indx = _int(0)
                i = _int(1)
                _pc = 1
            case 1:  # <D.20405>
                D_16222 = _int(i > 22)
                _pc = 6 if D_16222 != 0 else 2
                continue
            case 2:  # <D.20406>
                _1 = _int(i)
                _2 = _1 + -1
                _3 = _read_char(holvec[_2:], 1 - 1)
                _4 = _read_char(char, 1 - 1)
                _pc = 3 if _3 != _4 else 4
                continue
            case 3:  # <D.20407>
                _pc = 5
                continue
            case 4:  # L.1259
                _5 = _int(i)
                _6 = _5 + -1
                indx = _int(indx1[_6])
                _pc = 6
                continue
            case 5:  # L.1257
                i = _int(i + 1)
                _pc = 1
                continue
            case 6:  # __label_000110
                _pc = 7 if indx == 0 else 8
                continue
            case 7:  # __label_000910
                _gfortran_stop_numeric(-1, 0)
                _pc = 8
            case 8:  # __label_000920
                __result_jou = _int(indx)
                D_20411 = _int(__result_jou)
                return D_20411
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_flayz(_state, ml, model, icld, zmdl, gndalt, ivsa):
    card2a_cthik = _state.view(209616, '<f4')
    card2a_calt = _state.view(209620, '<f4')
    zvsaly_zvsa = _state.view(245664, '<f4')
    zaer = _state.view(182208, '<f4')
    zcld = _state.view(182368, '<f4')
    znew = _state.view(182432, '<f4')
    znewv = _state.view(182112, '<f4')
    cld0 = _ZERO32
    cld1 = _ZERO32
    cld2 = _ZERO32
    cld3 = _ZERO32
    cldd = _ZERO32
    dalt = _ZERO32
    hmxvsa = _ZERO32
    i = 0
    ii = 0
    ij = 0
    ijii = 0
    ik = 0
    il = 0
    j = 0
    k = 0
    mdel = 0
    ml1 = 0
    zk1 = _ZERO32
    zst = _zeros(34, '<f4')
    D_16283 = 0
    D_16288 = 0
    D_16291 = 0
    D_16297 = 0
    D_16300 = 0
    D_16309 = 0
    D_16313 = 0
    D_16316 = 0
    D_16320 = 0
    D_16323 = 0
    D_16325 = 0
    D_16328 = 0
    D_16335 = 0
    D_16337 = 0
    D_16340 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = model[0]
                _pc = 1 if _1 == 7 else 2
                continue
            case 1:  # <D.20414>
                _pc = 76
                continue
            case 2:  # L.1261
                _2 = model[0]
                _pc = 3 if _2 == 0 else 4
                continue
            case 3:  # <D.20416>
                _pc = 76
                continue
            case 4:  # L.1262
                _3 = ivsa[0]
                _pc = 5 if _3 == 1 else 23
                continue
            case 5:  # <D.20418>
                i = _int(1)
                _pc = 6
            case 6:  # <D.20420>
                D_16283 = _int(i > 9)
                _pc = 9 if D_16283 != 0 else 7
                continue
            case 7:  # __label_000002
                _4 = _int(i)
                _5 = _4 + -1
                _6 = _int(i)
                _7 = _6 + -1
                _8 = zvsaly_zvsa[_5]
                zmdl[_7] = _8
                _pc = 8
            case 8:  # L.1264
                i = _int(i + 1)
                _pc = 6
                continue
            case 9:  # L.1265
                hmxvsa = _f32(zvsaly_zvsa[8])
                zk1 = _f32(hmxvsa + 9.99999977648258209228515625e-3)
                _pc = 10 if hmxvsa < 2.0e+0 else 11
                continue
            case 10:  # <D.20422>
                ml[0] = 33
                _pc = 11
                continue
            case 11:  # L.1266
                _pc = 12 if hmxvsa < 1.0e+0 else 13
                continue
            case 12:  # <D.20425>
                ml[0] = 34
                _pc = 13
                continue
            case 13:  # L.1267
                _pc = 14 if hmxvsa == 2.0e+0 else 15
                continue
            case 14:  # <D.20428>
                ml[0] = 32
                _pc = 15
                continue
            case 15:  # L.1268
                _9 = ml[0]
                mdel = _int(34 - _9)
                D_16288 = _int(ml[0])
                k = _int(1)
                _pc = 16
            case 16:  # <D.20431>
                D_16291 = _int(k > D_16288)
                _pc = 22 if D_16291 != 0 else 17
                continue
            case 17:  # <D.20432>
                _10 = k + -10
                ik = _int(mdel + _10)
                _pc = 18 if ik > 0 else 19
                continue
            case 18:  # <D.20433>
                _11 = _int(ik)
                _12 = _11 + -1
                _13 = _int(k)
                _14 = _13 + -1
                _15 = znewv[_12]
                zmdl[_14] = _15
                _pc = 19
                continue
            case 19:  # L.1271
                _pc = 20 if k == 10 else 21
                continue
            case 20:  # <D.20436>
                _16 = _int(k)
                _17 = _16 + -1
                zmdl[_17] = zk1
                _pc = 21
                continue
            case 21:  # L.1269
                k = _int(k + 1)
                _pc = 16
                continue
            case 22:  # L.1270
                return
            case 23:  # L.1263
                _18 = icld[0]
                _19 = _18 > 0
                _20 = icld[0]
                _21 = _20 <= 11
                _22 = _19 & _21
                _pc = 24 if _22 != 0 else 25
                continue
            case 24:  # <D.20439>
                _pc = 65
                continue
            case 25:  # L.1273
                D_16297 = _int(ml[0])
                i = _int(1)
                _pc = 26
            case 26:  # <D.20441>
                D_16300 = _int(i > D_16297)
                _pc = 32 if D_16300 != 0 else 27
                continue
            case 27:  # <D.20442>
                _23 = _int(i)
                _24 = _23 + -1
                _25 = zaer[_24]
                _pc = 28 if _25 > 1.0e+2 else 29
                continue
            case 28:  # <D.20443>
                _pc = 32
                continue
            case 29:  # L.1276
                il = _int(i)
                _pc = 30
            case 30:  # __label_000010
                _26 = _int(i)
                _27 = _26 + -1
                _28 = _int(i)
                _29 = _28 + -1
                _30 = zaer[_27]
                zmdl[_29] = _30
                _pc = 31
            case 31:  # L.1274
                i = _int(i + 1)
                _pc = 26
                continue
            case 32:  # __label_000012
                ml[0] = il
                _31 = gndalt[0]
                _pc = 33 if _31 <= 0.0 else 34
                continue
            case 33:  # <D.20445>
                _pc = 40
                continue
            case 34:  # L.1277
                _32 = gndalt[0]
                _33 = 6.0e+0 - _32
                _34 = _33
                dalt = _f32(_div(_34, 6.0e+0))
                _pc = 35 if dalt <= 0.0 else 36
                continue
            case 35:  # <D.20447>
                _pc = 40
                continue
            case 36:  # L.1278
                i = _int(1)
                _pc = 37
            case 37:  # <D.20449>
                D_16309 = _int(i > 6)
                _pc = 40 if D_16309 != 0 else 38
                continue
            case 38:  # __label_000015
                _35 = i + -1
                _36 = _f32(_35)
                _37 = dalt * _36
                _38 = gndalt[0]
                _39 = _int(i)
                _40 = _39 + -1
                _41 = _37 + _38
                zmdl[_40] = _41
                _pc = 39
            case 39:  # L.1279
                i = _int(i + 1)
                _pc = 37
                continue
            case 40:  # __label_000090
                _42 = icld[0]
                _43 = _42 == 18
                _44 = icld[0]
                _45 = _44 == 19
                _46 = _43 | _45
                _pc = 41 if _46 != 0 else 64
                continue
            case 41:  # <D.20451>
                _47 = card2a_cthik[0]
                cldd = _f32(_47 * 1.00000001490116119384765625e-1)
                _48 = card2a_calt[0]
                _49 = cldd * 5.0e-1
                cld0 = _f32(_48 - _49)
                _pc = 42 if cld0 <= 0.0 else 43
                continue
            case 42:  # <D.20453>
                cld0 = _f32(0.0)
                _pc = 43
                continue
            case 43:  # L.1282
                cld1 = _f32(cld0 + cldd)
                _50 = card2a_cthik[0]
                _51 = cld1 + _50
                cld2 = _f32(_51 - cldd)
                cld3 = _f32(cld2 + cldd)
                D_16313 = _int(ml[0])
                i = _int(1)
                _pc = 44
            case 44:  # <D.20456>
                D_16316 = _int(i > D_16313)
                _pc = 49 if D_16316 != 0 else 45
                continue
            case 45:  # <D.20457>
                ij = _int(i)
                _52 = _int(i)
                _53 = _52 + -1
                _54 = zmdl[_53]
                _pc = 46 if cld0 > _54 else 47
                continue
            case 46:  # <D.20458>
                _pc = 48
                continue
            case 47:  # L.1285
                _pc = 50
                continue
            case 48:  # L.1283
                i = _int(i + 1)
                _pc = 44
                continue
            case 49:  # L.1284
                _pc = 76
                continue
            case 50:  # __label_000120
                _55 = ml[0]
                ml1 = _int(_55 - ij)
                D_16320 = _int(ml1)
                i = _int(1)
                _pc = 51
            case 51:  # <D.20460>
                D_16323 = _int(i > D_16320)
                _pc = 54 if D_16323 != 0 else 52
                continue
            case 52:  # __label_000130
                _56 = ij + i
                _57 = _56 + -1
                _58 = _int(_57)
                _59 = _58 + -1
                _60 = _int(i)
                _61 = _60 + -1
                _62 = zmdl[_59]
                zst[_61] = _62
                _pc = 53
            case 53:  # L.1286
                i = _int(i + 1)
                _pc = 51
                continue
            case 54:  # L.1287
                _63 = _int(ij)
                _64 = _63 + -1
                zmdl[_64] = cld0
                _65 = ij + 1
                _66 = _int(_65)
                _67 = _66 + -1
                zmdl[_67] = cld1
                _68 = ij + 2
                _69 = _int(_68)
                _70 = _69 + -1
                zmdl[_70] = cld2
                _71 = ij + 3
                _72 = _int(_71)
                _73 = _72 + -1
                zmdl[_73] = cld3
                ii = _int(3)
                D_16325 = _int(ml1)
                i = _int(1)
                _pc = 55
            case 55:  # <D.20462>
                D_16328 = _int(i > D_16325)
                _pc = 62 if D_16328 != 0 else 56
                continue
            case 56:  # <D.20463>
                _74 = _int(i)
                _75 = _74 + -1
                _76 = zst[_75]
                _pc = 57 if cld3 > _76 else 58
                continue
            case 57:  # <D.20464>
                _pc = 61
                continue
            case 58:  # L.1290
                ii = _int(ii + 1)
                _77 = ij + ii
                _78 = ml[0]
                _pc = 59 if _77 == _78 else 60
                continue
            case 59:  # <D.20466>
                _pc = 63
                continue
            case 60:  # L.1291
                _79 = _int(i)
                _80 = _79 + -1
                _81 = ij + ii
                _82 = _int(_81)
                _83 = _82 + -1
                _84 = zst[_80]
                zmdl[_83] = _84
                ijii = _int(ij + ii)
                _pc = 61
            case 61:  # L.1288
                i = _int(i + 1)
                _pc = 55
                continue
            case 62:  # L.1289
                _85 = ijii + 1
                ml[0] = _85
                _pc = 63
            case 63:  # __label_000145
                _86 = ml[0]
                _87 = _int(_86)
                _88 = _87 + -1
                zmdl[_88] = 1.0e+2
                _pc = 64
                continue
            case 64:  # L.1281
                _pc = 76
                continue
            case 65:  # __label_000018
                i = _int(1)
                _pc = 66
            case 66:  # <D.20469>
                D_16335 = _int(i > 16)
                _pc = 69 if D_16335 != 0 else 67
                continue
            case 67:  # __label_000020
                _89 = _int(i)
                _90 = _89 + -1
                _91 = zcld[_90]
                _92 = gndalt[0]
                _93 = _int(i)
                _94 = _93 + -1
                _95 = _91 + _92
                zmdl[_94] = _95
                _pc = 68
            case 68:  # L.1292
                i = _int(i + 1)
                _pc = 66
                continue
            case 69:  # L.1293
                i = _int(16)
                D_16337 = _int(ml[0])
                k = _int(17)
                _pc = 70
            case 70:  # <D.20471>
                D_16340 = _int(k > D_16337)
                _pc = 75 if D_16340 != 0 else 71
                continue
            case 71:  # <D.20472>
                j = _int(k + -16)
                _96 = _int(j)
                _97 = _96 + -1
                _98 = znew[_97]
                _99 = zmdl[15]
                _pc = 72 if _98 <= _99 else 73
                continue
            case 72:  # <D.20473>
                _pc = 74
                continue
            case 73:  # L.1296
                i = _int(i + 1)
                _100 = _int(j)
                _101 = _100 + -1
                _102 = _int(i)
                _103 = _102 + -1
                _104 = znew[_101]
                zmdl[_103] = _104
                _pc = 74
            case 74:  # L.1294
                k = _int(k + 1)
                _pc = 70
                continue
            case 75:  # L.1295
                ml[0] = i
                _pc = 76
                continue
            case 76:  # __label_000600
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_cirr18(_state):
    _pc = 0
    while True:
        match _pc:
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_rdnsm(_state, python):
    card1_model = _state.view(209568, '<i4')
    card1_m1 = _state.view(209580, '<i4')
    card1a_ird1 = _state.view(189440, '<i4')
    card1a_ird2 = _state.view(189444, '<i4')
    card1b_junit = _state.view(209632, '<i4')
    card1b_wmol = _state.view(209692, '<f4')
    card1b_wair1 = _state.view(209740, '<f4')
    card1b_jlow = _state.view(209744, '<i4')
    card2_ivsa = _state.view(231764, '<i4')
    cntrl_ml = _state.view(245616, '<i4')
    nsinp_zmdl = _state.view(243040, '<f4')
    nsinp_p = _state.view(243200, '<f4')
    nsinp_t = _state.view(243360, '<f4')
    nsinp_wmdl = _state.view(243520, '<f4')
    iconv = 0
    ird0 = 0
    jchar = _zeros(15, 'S1')
    k = 0
    km = 0
    D_16614 = 0
    D_16617 = 0
    D_16620 = 0
    D_16636 = 0
    C_16640 = _array([1], '<i4')
    C_16641 = _array([2], '<i4')
    D_16644 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = cntrl_ml[0]
                _pc = 1 if _1 > 24 else 2
                continue
            case 1:  # __label_000900
                cntrl_ml[0] = 24
                _pc = 2
                continue
            case 2:  # L.1303
                card1b_jlow[0] = 1
                D_16614 = _int(cntrl_ml[0])
                k = _int(1)
                _pc = 3
            case 3:  # <D.20496>
                D_16617 = _int(k > D_16614)
                _pc = -1 if D_16617 != 0 else 4
                continue
            case 4:  # <D.20497>
                km = _int(1)
                _pc = 5
            case 5:  # <D.20498>
                D_16620 = _int(km > 15)
                _pc = 10 if D_16620 != 0 else 6
                continue
            case 6:  # <D.20499>
                _2 = _int(km)
                _3 = _2 + -1
                jchar[_3:].view("u1")[1 - 1] = 32
                _pc = 7 if km > 12 else 8
                continue
            case 7:  # <D.20500>
                _pc = 9
                continue
            case 8:  # L.1308
                _4 = _int(km)
                _5 = _4 + -1
                card1b_wmol[_5] = 0.0
                _pc = 9
            case 9:  # L.1306
                km = _int(km + 1)
                _pc = 5
                continue
            case 10:  # L.1307
                ird0 = _int(1)
                iconv = _int(1)
                _6 = card1_model[0]
                _7 = _f32(_6)
                _8 = _7 > 0.0
                _9 = card1_model[0]
                _10 = _9 <= 6
                _11 = _8 & _10
                _pc = 11 if _11 != 0 else 12
                continue
            case 11:  # <D.20502>
                ird0 = _int(0)
                _pc = 12
                continue
            case 12:  # L.1309
                _12 = ird0 == 1
                _13 = card2_ivsa[0]
                _14 = _13 == 1
                _15 = _12 & _14
                _pc = 13 if _15 != 0 else 14
                continue
            case 13:  # <D.20505>
                ird0 = _int(0)
                iconv = _int(0)
                _pc = 14
                continue
            case 14:  # L.1310
                _16 = python[0]
                _pc = 15 if _16 != 0 else 16
                continue
            case 15:  # <D.20508>
                _pc = 17
                continue
            case 16:  # <D.20509>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 17
            case 17:  # __label_000081
                _17 = _int(k)
                _18 = _17 + -1
                _19 = nsinp_zmdl[_18]
                _pc = 18 if _19 <= 2.0e+0 else 19
                continue
            case 18:  # <D.20511>
                card1b_jlow[0] = k
                _pc = 19
                continue
            case 19:  # L.1312
                _20 = card1a_ird1[0]
                _pc = 20 if _20 == 1 else 22
                continue
            case 20:  # <D.20514>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 21
            case 21:  # __label_000084
                _pc = 22
                continue
            case 22:  # L.1313
                _21 = card1a_ird2[0]
                _pc = 23 if _21 == 1 else 25
                continue
            case 23:  # <D.20517>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 24
            case 24:  # __label_000082
                _pc = 25
                continue
            case 25:  # L.1314
                km = _int(1)
                _pc = 26
            case 26:  # <D.20520>
                D_16636 = _int(km > 15)
                _pc = 29 if D_16636 != 0 else 27
                continue
            case 27:  # __label_000012
                _22 = _int(km)
                _23 = _22 + -1
                _24 = jchar[_23:]
                _25 = _int(km)
                _26 = _25 + -1
                _27 = _ft_jou(_state, _24, 1)
                card1b_junit[_26] = _27
                _pc = 28
            case 28:  # L.1315
                km = _int(km + 1)
                _pc = 26
                continue
            case 29:  # L.1316
                _28 = card1_m1[0]
                _pc = 30 if _28 != 0 else 31
                continue
            case 30:  # <D.20522>
                _29 = card1_m1[0]
                card1b_junit[0] = _29
                _pc = 31
                continue
            case 31:  # L.1317
                _30 = card1_m1[0]
                _pc = 32 if _30 != 0 else 33
                continue
            case 32:  # <D.20525>
                _31 = card1_m1[0]
                card1b_junit[1] = _31
                _pc = 33
                continue
            case 33:  # L.1318
                _32 = _int(k)
                _33 = _32 + -1
                _34 = nsinp_p[_33:]
                _ft_check(_state, _34, card1b_junit[0:], C_16640)
                _35 = _int(k)
                _36 = _35 + -1
                _37 = nsinp_t[_36:]
                _ft_check(_state, _37, card1b_junit[1:], C_16641)
                _38 = _int(k)
                _39 = _38 + -1
                _40 = nsinp_t[_39:]
                _41 = _int(k)
                _42 = _41 + -1
                _43 = nsinp_p[_42:]
                _44 = _int(k)
                _45 = _44 + -1
                _46 = nsinp_zmdl[_45:]
                _ft_defalt(_state, _46, _43, _40)
                _47 = _int(k)
                _48 = _47 + -1
                _49 = nsinp_t[_48:]
                _50 = _int(k)
                _51 = _50 + -1
                _52 = nsinp_p[_51:]
                _ft_convrt(_state, _52, _49)
                km = _int(1)
                _pc = 34
            case 34:  # <D.20528>
                D_16644 = _int(km > 12)
                _pc = 37 if D_16644 != 0 else 35
                continue
            case 35:  # __label_000020
                _53 = _int(km)
                _54 = _53 + -1
                _55 = _int(km)
                _56 = _55 * 40
                _57 = _int(k)
                _58 = _56 + _57
                _59 = _58 + -41
                _60 = card1b_wmol[_54]
                nsinp_wmdl[_59] = _60
                _pc = 36
            case 36:  # L.1319
                km = _int(km + 1)
                _pc = 34
                continue
            case 37:  # L.1320
                _61 = _int(k)
                _62 = _61 + 479
                _63 = card1b_wair1[0]
                nsinp_wmdl[_62] = _63
                _pc = 38
            case 38:  # L.1304
                k = _int(k + 1)
                _pc = 3
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_watvap(_state, p, t):
    card1b_junit1 = _state.view(209640, '<i4')
    card1b_wmol1 = _state.view(209692, '<f4')
    card1b_wair = _state.view(209740, '<f4')
    constn_pzero = _state.view(2304, '<f4')
    constn_tzero = _state.view(2308, '<f4')
    constn_avogad = _state.view(2312, '<f4')
    constn_alosmt = _state.view(2316, '<f4')
    constn_airmwt = _state.view(2348, '<f4')
    constn_amwt = _state.view(2352, '<f4')
    c1 = _state.view(182700, '<f4')
    c2 = _state.view(182696, '<f4')
    c3 = _state.view(182704, '<f4')
    xlosch = _state.view(182692, '<f4')
    a = _ZERO32
    atd = _ZERO32
    b = _ZERO32
    dennum = _ZERO32
    denst = _ZERO32
    junit = 0
    pss = _ZERO32
    r = _ZERO32
    rhoair = _ZERO32
    rhp = _ZERO32
    wmol = _ZERO32
    wtem = _ZERO32
    atemp_67 = _ZERO32
    D_16729 = _ZERO32
    D_16730 = _ZERO32
    atemp_68 = _ZERO32
    D_16734 = _ZERO32
    D_16735 = _ZERO32
    atemp_69 = _ZERO32
    D_16739 = _ZERO32
    D_16740 = _ZERO32
    atemp_70 = _ZERO32
    D_16743 = _ZERO32
    D_16744 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = p[0]
                _2 = constn_pzero[0]
                _3 = _div(_1, _2)
                _4 = _3
                _5 = constn_alosmt[0]
                _6 = _4 * _5
                _7 = constn_tzero[0]
                _8 = t[0]
                _9 = _div(_7, _8)
                _10 = _9
                rhoair = _f32(_6 * _10)
                _11 = p[0]
                _12 = constn_pzero[0]
                pss = _f32(_div(_11, _12))
                _13 = constn_tzero[0]
                _14 = t[0]
                a = _f32(_div(_13, _14))
                xlosch_783_15 = xlosch[0]
                _16 = pss * xlosch_783_15
                _17 = a * _16
                card1b_wair[0] = _17
                _18 = constn_avogad[0]
                _19 = constn_amwt[0]
                b = _f32(_div(_18, _19))
                _20 = constn_airmwt[0]
                _21 = constn_amwt[0]
                r = _f32(_div(_20, _21))
                junit = _int(card1b_junit1[0])
                wmol = _f32(card1b_wmol1[0])
                _pc = 1 if junit != 10 else 2
                continue
            case 1:  # <D.20530>
                _pc = 3
                continue
            case 2:  # L.1321
                _22 = wmol * rhoair
                wtem = _f32(_22 * 9.999999974752427078783512115478515625e-7)
                _pc = 25
                continue
            case 3:  # __label_000110
                _pc = 4 if junit != 11 else 5
                continue
            case 4:  # <D.20532>
                _pc = 6
                continue
            case 5:  # L.1322
                _23 = rhoair * 9.999999974752427078783512115478515625e-7
                _24 = _23
                _25 = _div(wmol, _24)
                card1b_wmol1[0] = _25
                wtem = _f32(wmol)
                _pc = 25
                continue
            case 6:  # __label_000120
                _pc = 7 if junit != 12 else 8
                continue
            case 7:  # <D.20534>
                _pc = 9
                continue
            case 8:  # L.1323
                _26 = r * wmol
                _27 = _26 * 1.000000047497451305389404296875e-3
                wtem = _f32(rhoair * _27)
                _28 = r * wmol
                _29 = _28 * 1.0e+3
                card1b_wmol1[0] = _29
                _pc = 25
                continue
            case 9:  # __label_000130
                _pc = 10 if junit != 13 else 11
                continue
            case 10:  # <D.20536>
                _pc = 12
                continue
            case 11:  # L.1324
                _30 = b * wmol
                wtem = _f32(_30 * 9.999999974752427078783512115478515625e-7)
                _31 = b * wmol
                _32 = _div(_31, rhoair)
                card1b_wmol1[0] = _32
                _pc = 25
                continue
            case 12:  # __label_000140
                _pc = 13 if junit != 14 else 14
                continue
            case 13:  # <D.20538>
                _pc = 15
                continue
            case 14:  # L.1325
                _33 = constn_pzero[0]
                _34 = _div(wmol, _33)
                _35 = _34
                _36 = constn_alosmt[0]
                _37 = _35 * _36
                _38 = constn_tzero[0]
                _39 = t[0]
                _40 = _div(_38, _39)
                _41 = _40
                wtem = _f32(_37 * _41)
                _42 = rhoair * 9.999999974752427078783512115478515625e-7
                _43 = _42
                _44 = _div(wtem, _43)
                card1b_wmol1[0] = _44
                _pc = 25
                continue
            case 15:  # __label_000150
                _pc = 16 if junit != 15 else 17
                continue
            case 16:  # <D.20540>
                _pc = 18
                continue
            case 17:  # L.1326
                _45 = constn_tzero[0]
                _46 = wmol
                atd = _f32(_div(_45, _46))
                atemp_67 = _f32(atd)
                D_16729 = _f32(atemp_67)
                D_16730 = _f32(D_16729 * D_16729)
                _47 = atemp_67 * b
                c2_784_48 = c2[0]
                _49 = atemp_67 * c2_784_48
                c1_785_50 = c1[0]
                _51 = _49 + c1_785_50
                c3_786_52 = c3[0]
                _53 = D_16730 * c3_786_52
                _54 = _51 + _53
                _55 = __builtin_expf(_54)
                _56 = _47 * _55
                _57 = _56 * 9.999999974752427078783512115478515625e-7
                _58 = wmol
                _59 = _57 * _58
                _60 = t[0]
                wtem = _f32(_div(_59, _60))
                _61 = rhoair * 9.999999974752427078783512115478515625e-7
                _62 = _61
                _63 = _div(wtem, _62)
                card1b_wmol1[0] = _63
                _pc = 25
                continue
            case 18:  # __label_000160
                _pc = 19 if junit != 16 else 20
                continue
            case 19:  # <D.20542>
                _pc = 21
                continue
            case 20:  # L.1327
                _64 = constn_tzero[0]
                _65 = constn_tzero[0]
                _66 = wmol + _65
                _67 = _66
                atd = _f32(_div(_64, _67))
                atemp_68 = _f32(atd)
                D_16734 = _f32(atemp_68)
                D_16735 = _f32(D_16734 * D_16734)
                _68 = atemp_68 * b
                c2_787_69 = c2[0]
                _70 = atemp_68 * c2_787_69
                c1_788_71 = c1[0]
                _72 = _70 + c1_788_71
                c3_789_73 = c3[0]
                _74 = D_16735 * c3_789_73
                _75 = _72 + _74
                _76 = __builtin_expf(_75)
                _77 = _68 * _76
                _78 = _77 * 9.999999974752427078783512115478515625e-7
                _79 = constn_tzero[0]
                _80 = wmol + _79
                _81 = _80
                _82 = _78 * _81
                _83 = t[0]
                wtem = _f32(_div(_82, _83))
                _84 = rhoair * 9.999999974752427078783512115478515625e-7
                _85 = _84
                _86 = _div(wtem, _85)
                card1b_wmol1[0] = _86
                _pc = 25
                continue
            case 21:  # __label_000170
                _pc = 22 if junit != 17 else 23
                continue
            case 22:  # <D.20544>
                _pc = 24
                continue
            case 23:  # L.1328
                atemp_69 = _f32(a)
                D_16739 = _f32(atemp_69)
                D_16740 = _f32(D_16739 * D_16739)
                _87 = atemp_69 * b
                c2_790_88 = c2[0]
                _89 = atemp_69 * c2_790_88
                c1_791_90 = c1[0]
                _91 = _89 + c1_791_90
                c3_792_92 = c3[0]
                _93 = D_16740 * c3_792_92
                _94 = _91 + _93
                _95 = __builtin_expf(_94)
                _96 = _87 * _95
                _97 = _96 * 9.999999974752427078783512115478515625e-7
                _98 = _div(wmol, 1.0e+2)
                _99 = _98
                wtem = _f32(_97 * _99)
                _100 = rhoair * 9.999999974752427078783512115478515625e-7
                _101 = _100
                _102 = _div(wtem, _101)
                card1b_wmol1[0] = _102
                _pc = 25
                continue
            case 24:  # __label_000951
                _gfortran_stop_numeric(-1, 0)
                _pc = 25
            case 25:  # __label_000200
                _103 = card1b_wmol1[0]
                _104 = _103 * 2.98899996522529341039476066299357317340712469899699499365e-23
                _105 = card1b_wair[0]
                _106 = _104 * _105
                card1b_wmol1[0] = _106
                atemp_70 = _f32(a)
                D_16743 = _f32(atemp_70)
                D_16744 = _f32(D_16743 * D_16743)
                _107 = atemp_70 * b
                c2_793_108 = c2[0]
                _109 = atemp_70 * c2_793_108
                c1_794_110 = c1[0]
                _111 = _109 + c1_794_110
                c3_795_112 = c3[0]
                _113 = D_16744 * c3_795_112
                _114 = _111 + _113
                _115 = __builtin_expf(_114)
                _116 = _107 * _115
                denst = _f32(_116 * 9.999999974752427078783512115478515625e-7)
                dennum = _f32(wtem)
                _117 = _div(dennum, denst)
                _118 = _117
                rhp = _f32(_118 * 1.0e+2)
                _pc = 26
            case 26:  # __label_000012
                _pc = 27 if rhp <= 1.0e+2 else -1
                continue
            case 27:  # <D.20546>
                _pc = -1
                continue
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_vsa(_state, ihaze, vis, ceilht, depth, zinvht, z, rh, ahaze, ih):
    aa = _state.view(182736, '<f4')
    cc = _state.view(182744, '<f4')
    ee = _state.view(182720, '<f4')
    fac1 = _state.view(182848, '<f4')
    fac2 = _state.view(182784, '<f4')
    kmtom = _state.view(182708, '<f4')
    a = _zeros(2, '<f4')
    anum = _ZERO32
    b = _zeros(2, '<f4')
    c = _zeros(2, '<f4')
    ceil = _ZERO32
    d = _ZERO32
    dak = _ZERO32
    dof = _ZERO32
    e = _ZERO32
    eak = _ZERO32
    f = _ZERO32
    hmax = _ZERO32
    i = 0
    ic = 0
    k = 0
    visib = _ZERO32
    zalgo = _ZERO32
    zc = _ZERO32
    zhigh = _ZERO32
    zinv = _ZERO32
    zt = _ZERO32
    D_16836 = _ZERO32
    M_71 = _ZERO32
    D_16842 = _ZERO32
    D_16843 = _ZERO32
    M_72 = _ZERO32
    M_73 = _ZERO32
    D_16861 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                zhigh = _f32(2.0e+3)
                hmax = _f32(zhigh)
                _1 = vis[0]
                _pc = 1 if _1 > 0.0 else 2
                continue
            case 1:  # <D.20548>
                _pc = 12
                continue
            case 2:  # L.1330
                _2 = ihaze[0]
                _pc = 3 if _2 == 8 else 4
                continue
            case 3:  # <D.20550>
                vis[0] = 2.0000000298023223876953125e-1
                _pc = 4
                continue
            case 4:  # L.1331
                _3 = ihaze[0]
                _pc = 5 if _3 == 9 else 6
                continue
            case 5:  # <D.20553>
                vis[0] = 5.0e-1
                _pc = 6
                continue
            case 6:  # L.1332
                _4 = ihaze[0]
                _5 = _4 == 2
                _6 = ihaze[0]
                _7 = _6 == 5
                _8 = _5 | _7
                _pc = 7 if _8 != 0 else 8
                continue
            case 7:  # <D.20556>
                vis[0] = 5.0e+0
                _pc = 8
                continue
            case 8:  # L.1333
                _9 = ihaze[0]
                _10 = _9 == 1
                _11 = ihaze[0]
                _12 = _11 == 4
                _13 = _10 | _12
                _14 = ihaze[0]
                _15 = _14 == 7
                _16 = _13 | _15
                _pc = 9 if _16 != 0 else 10
                continue
            case 9:  # <D.20559>
                vis[0] = 2.3e+1
                _pc = 10
                continue
            case 10:  # L.1334
                _17 = ihaze[0]
                _pc = 11 if _17 == 6 else 12
                continue
            case 11:  # <D.20562>
                vis[0] = 5.0e+1
                _pc = 12
                continue
            case 12:  # __label_000005
                _18 = vis[0]
                _19 = _div(3.9119999408721923828125e+0, _18)
                d = _f32(_19 - 1.200000010430812835693359375e-2)
                _20 = ceilht[0]
                kmtom_796_21 = kmtom[0]
                zc = _f32(_20 * kmtom_796_21)
                _22 = depth[0]
                kmtom_797_23 = kmtom[0]
                zt = _f32(_22 * kmtom_797_23)
                _24 = zinvht[0]
                kmtom_798_25 = kmtom[0]
                zinv = _f32(_24 * kmtom_798_25)
                _26 = ihaze[0]
                _pc = 13 if _26 == 9 else 14
                continue
            case 13:  # <D.20565>
                zc = _f32(-1.0e+0)
                _pc = 14
                continue
            case 14:  # L.1336
                _27 = ihaze[0]
                _28 = _27 == 9
                _29 = zt > 0.0
                _30 = _28 & _29
                _31 = zinv == 0.0
                _32 = _30 & _31
                _pc = 15 if _32 != 0 else 16
                continue
            case 15:  # <D.20568>
                zinv = _f32(zt)
                _pc = 16
                continue
            case 16:  # L.1337
                ic = _int(2)
                _33 = ee[0]
                _34 = d >= _33
                _35 = zc >= 0.0
                _36 = _34 & _35
                _pc = 17 if _36 != 0 else 18
                continue
            case 17:  # <D.20571>
                ic = _int(1)
                _pc = 18
                continue
            case 18:  # L.1338
                _37 = zc < 0.0
                _38 = ic == 2
                _39 = _37 & _38
                _pc = 19 if _39 != 0 else 20
                continue
            case 19:  # <D.20574>
                ic = _int(3)
                _pc = 20
                continue
            case 20:  # L.1339
                _40 = zinv < 0.0
                _41 = ic == 3
                _42 = _40 & _41
                _pc = 21 if _42 != 0 else 22
                continue
            case 21:  # <D.20577>
                ic = _int(4)
                _pc = 22
                continue
            case 22:  # L.1340
                k = _int(1)
                _pc = {1: 23, 2: 25, 3: 27, 4: 29}.get(ic, 31)
                continue
            case 23:  # L.1343
                _pc = 31
                continue
            case 24:  # continuation_69
                _pc = 31
                continue
            case 25:  # L.1344
                _pc = 42
                continue
            case 26:  # continuation_72
                _pc = 31
                continue
            case 27:  # L.1345
                _pc = 53
                continue
            case 28:  # continuation_75
                _pc = 31
                continue
            case 29:  # L.1346
                _pc = 66
                continue
            case 30:  # continuation_78
                _pc = 31
                continue
            case 31:  # __label_000010
                _43 = zc < hmax
                _44 = ic == 2
                _45 = _43 & _44
                _pc = 32 if _45 != 0 else 33
                continue
            case 32:  # <D.20581>
                k = _int(2)
                _pc = 33
                continue
            case 33:  # L.1347
                _pc = 34 if k == 2 else 35
                continue
            case 34:  # <D.20584>
                ic = _int(-1)
                _pc = 35
                continue
            case 35:  # L.1348
                _pc = 36 if k == 2 else 37
                continue
            case 36:  # <D.20587>
                d = _f32(ee[0])
                _pc = 37
                continue
            case 37:  # L.1349
                _46 = _int(k)
                _47 = _46 + -1
                _48 = aa[0]
                a[_47] = _48
                _49 = aa[0]
                _pc = 38 if d >= _49 else 39
                continue
            case 38:  # <D.20590>
                _50 = _int(k)
                _51 = _50 + -1
                _52 = d + 1.0e+1
                a[_51] = _52
                _pc = 39
                continue
            case 39:  # L.1350
                _53 = _int(k)
                _54 = _53 + -1
                _55 = cc[0]
                c[_54] = _55
                _pc = 40 if zt <= 0.0 else 41
                continue
            case 40:  # <D.20593>
                zt = _f32(2.0e+2)
                _pc = 41
                continue
            case 41:  # L.1351
                D_16836 = _f32(zt + zc)
                M_71 = _f32(D_16836)
                M_71 = _f32(min(hmax, M_71))
                hmax = _f32(M_71)
                _pc = 67
                continue
            case 42:  # __label_000020
                _56 = _int(k)
                _57 = _56 + -1
                _58 = aa[1]
                a[_57] = _58
                e = _f32(ee[0])
                _pc = 43 if zc == 0.0 else 47
                continue
            case 43:  # <D.20596>
                _59 = _int(k)
                _60 = _59 + -1
                _61 = a[_60]
                _62 = _div(e, _61)
                eak = _f32(__builtin_logf(_62))
                _63 = _int(k)
                _64 = _63 + -1
                _65 = a[_64]
                _66 = _div(d, _65)
                dak = _f32(__builtin_logf(_66))
                anum = _f32(_div(eak, dak))
                _pc = 44 if anum > 0.0 else 45
                continue
            case 44:  # <D.20598>
                _67 = __builtin_logf(anum)
                _68 = cc[1]
                ceil = _f32(_div(_67, _68))
                _pc = 46
                continue
            case 45:  # <D.20599>
                ceil = _f32(2.0e+3)
                _pc = 46
            case 46:  # L.1353
                _pc = 47
                continue
            case 47:  # L.1352
                _pc = 48 if zc == 0.0 else 49
                continue
            case 48:  # <D.20602>
                zc = _f32(ceil)
                _pc = 49
                continue
            case 49:  # L.1354
                _69 = vis[0]
                _70 = zc * _69
                _71 = _div(_70, 3.5e+2)
                D_16842 = _f32(_71)
                D_16843 = _f32(D_16842 * D_16842)
                f = _f32(D_16843)
                dof = _f32(_div(d, f))
                _pc = 50 if dof >= 9.99999974737875163555145263671875e-5 else 51
                continue
            case 50:  # <D.20605>
                _72 = _div(d, f)
                _73 = -_72
                _74 = __builtin_expf(_73)
                _75 = 1.0e+0 - _74
                _76 = _75
                _77 = _int(k)
                _78 = _77 + -1
                _79 = f * _76
                a[_78] = _79
                _pc = 52
                continue
            case 51:  # <D.20606>
                _80 = dof * 5.0e-1
                _81 = 1.0e+0 - _80
                _82 = _81
                _83 = _int(k)
                _84 = _83 + -1
                _85 = d * _82
                a[_84] = _85
                _pc = 52
            case 52:  # L.1355
                _pc = 67
                continue
            case 53:  # __label_000040
                _86 = _int(k)
                _87 = _86 + -1
                _88 = d * 1.10000002384185791015625e+0
                a[_87] = _88
                e = _f32(ee[2])
                _89 = ihaze[0]
                _90 = _89 == 2
                _91 = ihaze[0]
                _92 = _91 == 5
                _93 = _90 | _92
                _pc = 54 if _93 != 0 else 55
                continue
            case 54:  # <D.20608>
                e = _f32(ee[1])
                _pc = 55
                continue
            case 55:  # L.1356
                _94 = ihaze[0]
                _95 = _94 == 6
                _96 = vis[0]
                _97 = _96 > 2.0e+0
                _98 = ihaze[0]
                _99 = _98 != 9
                _100 = _97 & _99
                _101 = _95 | _100
                _pc = 56 if _101 != 0 else 57
                continue
            case 56:  # <D.20611>
                e = _f32(ee[3])
                _pc = 57
                continue
            case 57:  # L.1357
                _pc = 58 if e > d else 59
                continue
            case 58:  # <D.20614>
                e = _f32(d * 9.99989986419677734375e-1)
                _pc = 59
                continue
            case 59:  # L.1358
                _102 = zt > 0.0
                _103 = zinv == 0.0
                _104 = _102 & _103
                _105 = vis[0]
                _106 = _105 <= 2.0e+0
                _107 = _104 & _106
                _pc = 60 if _107 != 0 else 61
                continue
            case 60:  # <D.20617>
                zinv = _f32(zt)
                _pc = 61
                continue
            case 61:  # L.1359
                _108 = zinv == 0.0
                _109 = vis[0]
                _110 = _109 > 2.0e+0
                _111 = _108 & _110
                _112 = ihaze[0]
                _113 = _112 != 9
                _114 = _111 & _113
                _pc = 62 if _114 != 0 else 63
                continue
            case 62:  # <D.20620>
                zinv = _f32(2.0e+3)
                _pc = 63
                continue
            case 63:  # L.1360
                _115 = zinv == 0.0
                _116 = vis[0]
                _117 = _116 <= 2.0e+0
                _118 = ihaze[0]
                _119 = _118 == 9
                _120 = _117 | _119
                _121 = _115 & _120
                _pc = 64 if _121 != 0 else 65
                continue
            case 64:  # <D.20623>
                zinv = _f32(5.0e+1)
                _pc = 65
                continue
            case 65:  # L.1361
                M_72 = _f32(zinv)
                M_72 = _f32(min(hmax, M_72))
                hmax = _f32(M_72)
                zc = _f32(0.0)
                _pc = 67
                continue
            case 66:  # __label_000050
                _122 = _int(k)
                _123 = _122 + -1
                _124 = ee[3]
                a[_123] = _124
                _125 = _int(k)
                _126 = _125 + -1
                _127 = cc[2]
                c[_126] = _127
                _pc = 67
            case 67:  # __label_000060
                _128 = _int(k)
                _129 = _128 + -1
                _130 = a[_129]
                _131 = _div(d, _130)
                _132 = _int(k)
                _133 = _132 + -1
                _134 = __builtin_logf(_131)
                b[_133] = _134
                _pc = 68 if ic == 2 else 69
                continue
            case 68:  # <D.20626>
                _135 = _int(k)
                _136 = _135 + -1
                _137 = a[_136]
                _138 = _div(e, _137)
                _139 = __builtin_logf(_138)
                _140 = _int(k)
                _141 = _140 + -1
                _142 = b[_141]
                _143 = _div(_139, _142)
                _144 = __builtin_logf(_143)
                _145 = _int(k)
                _146 = _145 + -1
                _147 = _div(_144, zc)
                c[_146] = _147
                _pc = 69
                continue
            case 69:  # L.1362
                _pc = 70 if ic == 3 else 71
                continue
            case 70:  # <D.20629>
                _148 = _int(k)
                _149 = _148 + -1
                _150 = a[_149]
                _151 = _div(e, _150)
                _152 = __builtin_logf(_151)
                _153 = _int(k)
                _154 = _153 + -1
                _155 = b[_154]
                _156 = _div(_152, _155)
                _157 = __builtin_logf(_156)
                _158 = _int(k)
                _159 = _158 + -1
                _160 = _div(_157, zinv)
                c[_159] = _160
                _pc = 71
                continue
            case 71:  # L.1363
                _161 = zc < hmax
                _162 = k == 1
                _163 = _161 & _162
                _164 = ic == 2
                _165 = _163 & _164
                _pc = 72 if _165 != 0 else 73
                continue
            case 72:  # <D.20632>
                _pc = 31
                continue
            case 73:  # L.1364
                _pc = 74 if ic == 2 else 75
                continue
            case 74:  # <D.20634>
                M_73 = _f32(zc)
                M_73 = _f32(min(hmax, M_73))
                hmax = _f32(M_73)
                _pc = 75
                continue
            case 75:  # L.1365
                zalgo = _f32(hmax)
                _pc = 76 if ic < 0 else 77
                continue
            case 76:  # <D.20637>
                zalgo = _f32(zc)
                _pc = 77
                continue
            case 77:  # L.1366
                _pc = 78 if ic < 0 else 79
                continue
            case 78:  # <D.20640>
                k = _int(1)
                _pc = 79
                continue
            case 79:  # L.1367
                i = _int(1)
                _pc = 80
            case 80:  # <D.20643>
                D_16861 = _int(i > 9)
                _pc = 102 if D_16861 != 0 else 81
                continue
            case 81:  # <D.20644>
                _166 = ic < 0
                _167 = i == 5
                _168 = _166 & _167
                _pc = 82 if _168 != 0 else 83
                continue
            case 82:  # <D.20645>
                k = _int(2)
                _pc = 83
                continue
            case 83:  # L.1370
                _169 = ic < 0
                _170 = i == 5
                _171 = _169 & _170
                _pc = 84 if _171 != 0 else 85
                continue
            case 84:  # <D.20648>
                zalgo = _f32(hmax - zc)
                _pc = 85
                continue
            case 85:  # L.1371
                _172 = 10 - i
                _173 = _int(_172)
                _174 = _173 + -1
                _175 = fac2[_174]
                _176 = 1.0e+0 - _175
                _177 = _176
                _178 = _int(i)
                _179 = _178 + -1
                _180 = zalgo * _177
                z[_179] = _180
                _pc = 86 if ic == 1 else 87
                continue
            case 86:  # <D.20651>
                _181 = _int(i)
                _182 = _181 + -1
                _183 = fac1[_182]
                _184 = _int(i)
                _185 = _184 + -1
                _186 = zalgo * _183
                z[_185] = _186
                _pc = 87
                continue
            case 87:  # L.1372
                _pc = 88 if ic == 4 else 89
                continue
            case 88:  # <D.20654>
                _187 = i + -1
                _188 = _f32(_187)
                _189 = zalgo * _188
                _190 = _int(i)
                _191 = _190 + -1
                _192 = _div(_189, 8.0e+0)
                z[_191] = _192
                _pc = 89
                continue
            case 89:  # L.1373
                _193 = ic < 0
                _194 = i <= 4
                _195 = _193 & _194
                _pc = 90 if _195 != 0 else 91
                continue
            case 90:  # <D.20657>
                _196 = i * 2
                _197 = 11 - _196
                _198 = _int(_197)
                _199 = _198 + -1
                _200 = fac2[_199]
                _201 = 1.0e+0 - _200
                _202 = _201
                _203 = _int(i)
                _204 = _203 + -1
                _205 = zalgo * _202
                z[_204] = _205
                _pc = 91
                continue
            case 91:  # L.1374
                _206 = ic < 0
                _207 = i > 4
                _208 = _206 & _207
                _pc = 92 if _208 != 0 else 93
                continue
            case 92:  # <D.20660>
                _209 = i * 2
                _210 = _209 + -9
                _211 = _int(_210)
                _212 = _211 + -1
                _213 = fac1[_212]
                _214 = _int(i)
                _215 = _214 + -1
                _216 = zalgo * _213
                z[_215] = _216
                _pc = 93
                continue
            case 93:  # L.1375
                _217 = _int(k)
                _218 = _217 + -1
                _219 = a[_218]
                _220 = _int(k)
                _221 = _220 + -1
                _222 = b[_221]
                _223 = _int(k)
                _224 = _223 + -1
                _225 = c[_224]
                _226 = _int(i)
                _227 = _226 + -1
                _228 = z[_227]
                _229 = _225 * _228
                _230 = __builtin_expf(_229)
                _231 = _222 * _230
                _232 = __builtin_expf(_231)
                _233 = _int(i)
                _234 = _233 + -1
                _235 = _219 * _232
                ahaze[_234] = _235
                _236 = ic <= 0
                _237 = i > 4
                _238 = _236 & _237
                _pc = 94 if _238 != 0 else 95
                continue
            case 94:  # <D.20663>
                _239 = _int(i)
                _240 = _239 + -1
                _241 = z[_240]
                _242 = _int(i)
                _243 = _242 + -1
                _244 = zc + _241
                z[_243] = _244
                _pc = 95
                continue
            case 95:  # L.1376
                _245 = _int(i)
                _246 = _245 + -1
                _247 = z[_246]
                kmtom_799_248 = kmtom[0]
                _249 = _int(i)
                _250 = _249 + -1
                _251 = _div(_247, kmtom_799_248)
                z[_250] = _251
                _252 = _int(i)
                _253 = _252 + -1
                _254 = ahaze[_253]
                _255 = __builtin_logf(_254)
                _256 = _255 * 6.95300006866455078125e+0
                _257 = _int(i)
                _258 = _257 + -1
                _259 = _256 + 8.64069976806640625e+1
                rh[_258] = _259
                _260 = _int(i)
                _261 = _260 + -1
                _262 = ahaze[_261]
                _263 = ee[0]
                _pc = 96 if _262 >= _263 else 97
                continue
            case 96:  # <D.20666>
                _264 = _int(i)
                _265 = _264 + -1
                rh[_265] = 1.0e+2
                _pc = 97
                continue
            case 97:  # L.1377
                _266 = _int(i)
                _267 = _266 + -1
                _268 = ahaze[_267]
                _269 = _268 + 1.200000010430812835693359375e-2
                _270 = _269
                visib = _f32(_div(3.9119999408721923828125e+0, _270))
                _271 = _int(i)
                _272 = _271 + -1
                _273 = ihaze[0]
                ih[_272] = _273
                _274 = visib <= 2.0e+0
                _275 = ic == 3
                _276 = _274 & _275
                _pc = 98 if _276 != 0 else 99
                continue
            case 98:  # <D.20669>
                _277 = _int(i)
                _278 = _277 + -1
                ih[_278] = 9
                _pc = 99
                continue
            case 99:  # L.1378
                _279 = ic == 1
                _280 = ic < 0
                _281 = i > 4
                _282 = _280 & _281
                _283 = _279 | _282
                _pc = 100 if _283 != 0 else 101
                continue
            case 100:  # <D.20672>
                _284 = _int(i)
                _285 = _284 + -1
                ih[_285] = 8
                _pc = 101
                continue
            case 101:  # L.1368
                i = _int(i + 1)
                _pc = 80
                continue
            case 102:  # L.1369
                kmtom_800_286 = kmtom[0]
                hmax = _f32(_div(hmax, kmtom_800_286))
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_lwtrn7(_state, python, nwl, v1py, v2py, dvpy, txpy, vpy, alampy, tracepy, unifpy, sumapy, irradpy, sumvvpy, modelpy, itypepy, iemsctpy, impy, iseasnpy, mlpy, ird1py, zmdlpy, ppy, tpy, wmolpy, h1py, h2py, anglepy, rangepy, ihaze=0, visibility_km=0.0):
    __BLNK___ich = _state.view(265840, '<i4')
    __BLNK___w = _state.view(266176, '<f4')
    __BLNK___wpath = _state.view(266428, '<f4')
    __BLNK___tbby = _state.view(283564, '<f4')
    __BLNK___absc = _state.view(283836, '<f4')
    __BLNK___extc = _state.view(284776, '<f4')
    __BLNK___asym = _state.view(285716, '<f4')
    card1_model = _state.view(209568, '<i4')
    card1_itype = _state.view(209572, '<i4')
    card1_iemsct = _state.view(209576, '<i4')
    card1_m1 = _state.view(209580, '<i4')
    card1_m2 = _state.view(209584, '<i4')
    card1_m3 = _state.view(209588, '<i4')
    card1_im = _state.view(209592, '<i4')
    card1_noprt = _state.view(209596, '<i4')
    card1_tbound = _state.view(209600, '<f4')
    card1_salb = _state.view(209604, '<f4')
    card1a_m4 = _state.view(189424, '<i4')
    card1a_m5 = _state.view(189428, '<i4')
    card1a_m6 = _state.view(189432, '<i4')
    card1a_mdef = _state.view(189436, '<i4')
    card1a_ird1 = _state.view(189440, '<i4')
    card1a_ird2 = _state.view(189444, '<i4')
    card1b_junit = _state.view(209632, '<i4')
    card1b_wmol = _state.view(209692, '<f4')
    card2_ihaze = _state.view(231744, '<i4')
    card2_iseasn = _state.view(231748, '<i4')
    card2_ivulcn = _state.view(231752, '<i4')
    card2_icstl = _state.view(231756, '<i4')
    card2_icld = _state.view(231760, '<i4')
    card2_ivsa = _state.view(231764, '<i4')
    card2_vis = _state.view(231768, '<f4')
    card2_wss = _state.view(231772, '<f4')
    card2_whh = _state.view(231776, '<f4')
    card2_rainrt = _state.view(231780, '<f4')
    card2a_cthik = _state.view(209616, '<f4')
    card2a_calt = _state.view(209620, '<f4')
    card2a_cext = _state.view(209624, '<f4')
    card2d_ireg = _state.view(214080, '<i4')
    card3_h1 = _state.view(246128, '<f4')
    card3_h2 = _state.view(246132, '<f4')
    card3_angle = _state.view(246136, '<f4')
    card3_range = _state.view(246140, '<f4')
    card3_beta = _state.view(246144, '<f4')
    card3_re = _state.view(246148, '<f4')
    card3_len = _state.view(246152, '<i4')
    card4_v1 = _state.view(286864, '<f4')
    card4_v2 = _state.view(286868, '<f4')
    card4_dv = _state.view(286872, '<f4')
    cnstns_pi = _state.view(246160, '<f4')
    cnstns_ca = _state.view(246164, '<f4')
    cnstns_deg = _state.view(246168, '<f4')
    cnstns_gcair = _state.view(246172, '<f4')
    cnstns_bignum = _state.view(246176, '<f4')
    cnstns_bigexp = _state.view(246180, '<f4')
    cntrl_kmax = _state.view(245600, '<i4')
    cntrl_m = _state.view(245604, '<i4')
    cntrl_ikmax = _state.view(245608, '<i4')
    cntrl_nl = _state.view(245612, '<i4')
    cntrl_ml = _state.view(245616, '<i4')
    cntrl_iklo = _state.view(245620, '<i4')
    cntrl_issgeo = _state.view(245624, '<i4')
    cntrl_imult = _state.view(245628, '<i4')
    ifil_ird = _state.view(243008, '<i4')
    ifil_ipr = _state.view(243012, '<i4')
    ifil_ipu = _state.view(243016, '<i4')
    ifil_npr = _state.view(243020, '<i4')
    ifil_ipr1 = _state.view(243024, '<i4')
    mart_rhh = _state.view(241568, '<f4')
    mdata_p = _state.view(149320, '<f4')
    mdata_t = _state.view(149520, '<f4')
    mdlz_hmdlz = _state.view(231808, '<f4')
    mnlt_tbbss = _state.view(214144, '<f4')
    mnlt_tbbms = _state.view(214416, '<f4')
    mnlt_wpms = _state.view(214552, '<f4')
    mnlt_imsmx = _state.view(223120, '<i4')
    mnlt_wpmss = _state.view(223124, '<f4')
    model_zm = _state.view(231904, '<f4')
    path_pl = _state.view(242144, '<f4')
    path_qtheta = _state.view(242416, '<f4')
    path_itest = _state.view(242688, '<i4')
    sols_wpaths = _state.view(190016, '<f4')
    sols_cszen = _state.view(208260, '<f4')
    titl_hmodel = _state.view(59956, 'S4')
    vsbd_vsb = _state.view(60224, '<f4')
    zvsaly_zvsa = _state.view(245664, '<f4')
    zvsaly_rhvsa = _state.view(245704, '<f4')
    zvsaly_ahvsa = _state.view(245744, '<f4')
    zvsaly_ihvsa = _state.view(245784, '<i4')
    irpt = _state.view(188292, '<i4')
    maxgeo = _state.view(182884, '<i4')
    alam1 = _ZERO32
    alam2 = _ZERO32
    ubound_74 = 0
    size_75 = 0
    anglem = _zeros(1, '<f4')
    angles = _ZERO32
    bendng = _zeros(1, '<f4')
    betas = _ZERO32
    cprob = _zeros(1, '<f4')
    csensv = _zeros(68, '<f4')
    g = _zeros(1, '<f4')
    gndalt = _zeros(1, '<f4')
    h1s = _ZERO32
    h2s = _ZERO32
    i = 0
    iday = _zeros(1, '<i4')
    ierror = _zeros(1, '<i4')
    iflga = 0
    iflgt = 0
    ihmet = 0
    ihvul = 0
    ii = 0
    ik = 0
    iparm = _zeros(1, '<i4')
    iph = _zeros(1, '<i4')
    ipy2 = 0
    irain = 0
    ubound_76 = 0
    stride_77 = 0
    offset_78 = 0
    size_79 = 0
    iseed = _zeros(1, '<i4')
    isourc = _zeros(1, '<i4')
    issgs = 0
    itypes = 0
    j = 0
    jprt = _zeros(1, '<i4')
    k = 0
    lens = 0
    mdel = 0
    mdels = 0
    mm1 = 0
    mm2 = 0
    mm3 = 0
    n = 0
    parm1 = _zeros(1, '<f4')
    parm2 = _zeros(1, '<f4')
    parm3 = _zeros(1, '<f4')
    parm4 = _zeros(1, '<f4')
    plst = _zeros(68, '<f4')
    ubound_80 = 0
    size_81 = 0
    psipo = _zeros(1, '<f4')
    qthets = _zeros(68, '<f4')
    rangs = _ZERO32
    ro = _ZERO32
    ubound_82 = 0
    size_83 = 0
    ubound_84 = 0
    size_85 = 0
    time = _zeros(1, '<f4')
    ubound_86 = 0
    size_87 = 0
    ubound_88 = 0
    size_89 = 0
    ubound_90 = 0
    stride_91 = 0
    offset_92 = 0
    size_93 = 0
    ubound_94 = 0
    size_95 = 0
    ubound_96 = 0
    size_97 = 0
    w15sv = _ZERO32
    zcvsa = _zeros(1, '<f4')
    zinvsa = _zeros(1, '<f4')
    ubound_98 = 0
    size_99 = 0
    ztvsa = _zeros(1, '<f4')
    D_17654 = 0
    D_17655 = 0
    D_17656 = 0
    D_17657 = 0
    D_17658 = 0
    D_17659 = 0
    D_17660 = 0
    D_17661 = 0
    D_17662 = 0
    D_17663 = 0
    D_17664 = 0
    D_17665 = 0
    D_17666 = 0
    D_17667 = 0
    D_17668 = 0
    D_17669 = 0
    D_17670 = 0
    D_17671 = 0
    D_17672 = 0
    D_17673 = 0
    D_17674 = 0
    D_17675 = 0
    D_17676 = 0
    D_17677 = 0
    D_17678 = 0
    D_17679 = 0
    D_17680 = 0
    D_17681 = 0
    D_17682 = 0
    D_17683 = 0
    D_17684 = 0
    D_17685 = 0
    D_17686 = 0
    D_17392 = 0
    D_17398 = 0
    D_17401 = 0
    C_17429 = _array([1], '<i4')
    D_17449 = 0
    D_17456 = 0
    D_17459 = 0
    D_17462 = 0
    D_17465 = 0
    D_17577 = 0
    D_17578 = 0
    D_17581 = 0
    D_17585 = 0
    D_17588 = 0
    D_17589 = 0
    D_17592 = 0
    D_17595 = 0
    D_17598 = 0
    D_17601 = 0
    D_17604 = 0
    D_17605 = 0
    D_17608 = 0
    D_17613 = 0
    D_17616 = 0
    D_17628 = 0
    D_17631 = 0
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                _1 = mlpy[0]
                ubound_98 = _int(_int(_1))
                size_99 = _int(ubound_98)
                size_99 = _int(max(size_99, 0))
                D_17684 = _int(size_99 + -1)
                size_801_2 = _int(size_99)
                _3 = _int(size_801_2)
                D_17685 = _int(_3 * 32)
                size_802_4 = _int(size_99)
                D_17686 = _int(size_802_4 * 4)
                _5 = mlpy[0]
                ubound_80 = _int(_int(_5))
                size_81 = _int(ubound_80)
                size_81 = _int(max(size_81, 0))
                D_17681 = _int(size_81 + -1)
                size_803_6 = _int(size_81)
                _7 = _int(size_803_6)
                D_17682 = _int(_7 * 32)
                size_804_8 = _int(size_81)
                D_17683 = _int(size_804_8 * 4)
                _9 = mlpy[0]
                ubound_86 = _int(_int(_9))
                size_87 = _int(ubound_86)
                size_87 = _int(max(size_87, 0))
                D_17678 = _int(size_87 + -1)
                size_805_10 = _int(size_87)
                _11 = _int(size_805_10)
                D_17679 = _int(_11 * 32)
                size_806_12 = _int(size_87)
                D_17680 = _int(size_806_12 * 4)
                _13 = nwl[0]
                ubound_90 = _int(_int(_13))
                stride_91 = _int(ubound_90)
                stride_91 = _int(max(stride_91, 0))
                size_93 = _int(stride_91 * 63)
                size_93 = _int(max(size_93, 0))
                D_17675 = _int(size_93 + -1)
                size_807_14 = _int(size_93)
                _15 = _int(size_807_14)
                D_17676 = _int(_15 * 32)
                size_808_16 = _int(size_93)
                D_17677 = _int(size_808_16 * 4)
                offset_92 = _int(~stride_91)
                _17 = nwl[0]
                ubound_96 = _int(_int(_17))
                size_97 = _int(ubound_96)
                size_97 = _int(max(size_97, 0))
                D_17672 = _int(size_97 + -1)
                size_809_18 = _int(size_97)
                _19 = _int(size_809_18)
                D_17673 = _int(_19 * 32)
                size_810_20 = _int(size_97)
                D_17674 = _int(size_810_20 * 4)
                _21 = nwl[0]
                ubound_74 = _int(_int(_21))
                size_75 = _int(ubound_74)
                size_75 = _int(max(size_75, 0))
                D_17669 = _int(size_75 + -1)
                size_811_22 = _int(size_75)
                _23 = _int(size_811_22)
                D_17670 = _int(_23 * 32)
                size_812_24 = _int(size_75)
                D_17671 = _int(size_812_24 * 4)
                _25 = nwl[0]
                ubound_88 = _int(_int(_25))
                size_89 = _int(ubound_88)
                size_89 = _int(max(size_89, 0))
                D_17666 = _int(size_89 + -1)
                size_813_26 = _int(size_89)
                _27 = _int(size_813_26)
                D_17667 = _int(_27 * 32)
                size_814_28 = _int(size_89)
                D_17668 = _int(size_814_28 * 4)
                _29 = nwl[0]
                ubound_94 = _int(_int(_29))
                size_95 = _int(ubound_94)
                size_95 = _int(max(size_95, 0))
                D_17663 = _int(size_95 + -1)
                size_815_30 = _int(size_95)
                _31 = _int(size_815_30)
                D_17664 = _int(_31 * 32)
                size_816_32 = _int(size_95)
                D_17665 = _int(size_816_32 * 4)
                _33 = nwl[0]
                ubound_82 = _int(_int(_33))
                size_83 = _int(ubound_82)
                size_83 = _int(max(size_83, 0))
                D_17660 = _int(size_83 + -1)
                size_817_34 = _int(size_83)
                _35 = _int(size_817_34)
                D_17661 = _int(_35 * 32)
                size_818_36 = _int(size_83)
                D_17662 = _int(size_818_36 * 4)
                _37 = nwl[0]
                ubound_76 = _int(_int(_37))
                stride_77 = _int(ubound_76)
                stride_77 = _int(max(stride_77, 0))
                size_79 = _int(stride_77 * 3)
                size_79 = _int(max(size_79, 0))
                D_17657 = _int(size_79 + -1)
                size_819_38 = _int(size_79)
                _39 = _int(size_819_38)
                D_17658 = _int(_39 * 32)
                size_820_40 = _int(size_79)
                D_17659 = _int(size_820_40 * 4)
                offset_78 = _int(~stride_77)
                _41 = nwl[0]
                ubound_84 = _int(_int(_41))
                size_85 = _int(ubound_84)
                size_85 = _int(max(size_85, 0))
                D_17654 = _int(size_85 + -1)
                size_821_42 = _int(size_85)
                _43 = _int(size_821_42)
                D_17655 = _int(_43 * 32)
                size_822_44 = _int(size_85)
                D_17656 = _int(size_822_44 * 4)
                ifil_ird[0] = 15
                ifil_ipr[0] = 16
                ifil_ipu[0] = 17
                ifil_ipr1[0] = 18
                _45 = python[0]
                _pc = 1 if _45 != 0 else 3
                continue
            case 1:  # <D.20678>
                _46 = ifil_ipr[0]
                ifil_ipu[0] = _46
                _47 = ifil_ipr[0]
                ifil_ipr1[0] = _47
                _pc = 3
                continue
            case 2:  # __label_000666
                _pc = 3
                continue
            case 3:  # __label_000667
                cnstns_pi[0] = 3.1415927410125732421875e+0
                _48 = cnstns_pi[0]
                _49 = _div(_48, 1.8e+2)
                cnstns_ca[0] = _49
                _50 = cnstns_ca[0]
                _51 = _div(1.0e+0, _50)
                cnstns_deg[0] = _51
                card3_range[0] = 0.0
                cnstns_gcair[0] = 2.870530029296875e+3
                cnstns_bignum[0] = 9.9999996802856924650656260769173209088e+37
                cnstns_bigexp[0] = 8.7e+1
                cntrl_kmax[0] = 63
                cntrl_nl[0] = 33
                _pc = 4
            case 4:  # __label_000100
                ii = _int(1)
                _pc = 5
            case 5:  # <D.20681>
                D_17392 = _int(ii > 4)
                _pc = 8 if D_17392 != 0 else 6
                continue
            case 6:  # __label_000010
                _52 = _int(ii)
                _53 = _52 + -1
                card2d_ireg[_53] = 0
                _pc = 7
            case 7:  # L.1381
                ii = _int(ii + 1)
                _pc = 5
                continue
            case 8:  # __label_001010
                i = _int(1)
                _pc = 9
            case 9:  # <D.20683>
                D_17398 = _int(i > 4)
                _pc = 16 if D_17398 != 0 else 10
                continue
            case 10:  # <D.20684>
                j = _int(1)
                _pc = 11
            case 11:  # <D.20685>
                D_17401 = _int(j > 40)
                _pc = 15 if D_17401 != 0 else 12
                continue
            case 12:  # <D.20686>
                _54 = _int(j)
                _55 = _54 * 5
                _56 = _int(i)
                _57 = _55 + _56
                _58 = _57 + -6
                __BLNK___absc[_58] = 0.0
                _59 = _int(j)
                _60 = _59 * 5
                _61 = _int(i)
                _62 = _60 + _61
                _63 = _62 + -6
                __BLNK___extc[_63] = 0.0
                _pc = 13
            case 13:  # __label_000080
                _64 = _int(j)
                _65 = _64 * 5
                _66 = _int(i)
                _67 = _65 + _66
                _68 = _67 + -6
                __BLNK___asym[_68] = 0.0
                _pc = 14
            case 14:  # L.1385
                j = _int(j + 1)
                _pc = 11
                continue
            case 15:  # L.1383
                i = _int(i + 1)
                _pc = 9
                continue
            case 16:  # L.1384
                jprt[0] = 0
                cntrl_iklo[0] = 1
                _69 = python[0]
                _pc = 17 if _69 != 0 else 18
                continue
            case 17:  # <D.20687>
                _70 = modelpy[0]
                card1_model[0] = _70
                _71 = itypepy[0]
                card1_itype[0] = _71
                _72 = iemsctpy[0]
                card1_iemsct[0] = _72
                _73 = impy[0]
                card1_im[0] = _73
                card1_m1[0] = 0
                card1_m2[0] = 0
                card1_m3[0] = 0
                card1a_m4[0] = 0
                card1a_m5[0] = 0
                card1a_m6[0] = 0
                card1a_mdef[0] = 0
                cntrl_imult[0] = 0
                card1_tbound[0] = 0.0
                card1_salb[0] = 0.0
                card1_noprt[0] = 0
                _pc = 19
                continue
            case 18:  # <D.20688>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 19
            case 19:  # __label_001111
                _74 = cntrl_imult[0]
                _75 = _74 == 1
                _76 = card1_noprt[0]
                _77 = _76 == 1
                _78 = _75 & _77
                _pc = 20 if _78 != 0 else 21
                continue
            case 20:  # <D.20690>
                card1_noprt[0] = 0
                _pc = 21
                continue
            case 21:  # L.1388
                card1a_ird1[0] = 0
                card1a_ird2[0] = 0
                _79 = card1_model[0]
                _pc = 22 if _79 == 0 else 23
                continue
            case 22:  # <D.20693>
                card3_len[0] = 0
                _pc = 23
                continue
            case 23:  # L.1389
                _80 = card1_model[0]
                _81 = _80 == 0
                _82 = card1_model[0]
                _83 = _82 == 7
                _84 = _81 | _83
                _pc = 24 if _84 != 0 else 25
                continue
            case 24:  # <D.20696>
                _pc = 39
                continue
            case 25:  # L.1390
                _85 = card1_m1[0]
                _pc = 26 if _85 == 0 else 27
                continue
            case 26:  # <D.20698>
                _86 = card1_model[0]
                card1_m1[0] = _86
                _pc = 27
                continue
            case 27:  # L.1391
                _87 = card1_m2[0]
                _pc = 28 if _87 == 0 else 29
                continue
            case 28:  # <D.20701>
                _88 = card1_model[0]
                card1_m2[0] = _88
                _pc = 29
                continue
            case 29:  # L.1392
                _89 = card1_m3[0]
                _pc = 30 if _89 == 0 else 31
                continue
            case 30:  # <D.20704>
                _90 = card1_model[0]
                card1_m3[0] = _90
                _pc = 31
                continue
            case 31:  # L.1393
                _91 = card1a_m4[0]
                _pc = 32 if _91 == 0 else 33
                continue
            case 32:  # <D.20707>
                _92 = card1_model[0]
                card1a_m4[0] = _92
                _pc = 33
                continue
            case 33:  # L.1394
                _93 = card1a_m5[0]
                _pc = 34 if _93 == 0 else 35
                continue
            case 34:  # <D.20710>
                _94 = card1_model[0]
                card1a_m5[0] = _94
                _pc = 35
                continue
            case 35:  # L.1395
                _95 = card1a_m6[0]
                _pc = 36 if _95 == 0 else 37
                continue
            case 36:  # <D.20713>
                _96 = card1_model[0]
                card1a_m6[0] = _96
                _pc = 37
                continue
            case 37:  # L.1396
                _97 = card1a_mdef[0]
                _pc = 38 if _97 == 0 else 39
                continue
            case 38:  # <D.20716>
                card1a_mdef[0] = 1
                _pc = 39
                continue
            case 39:  # __label_000110
                _98 = card1_model[0]
                cntrl_m[0] = _98
                _99 = card1_noprt[0]
                ifil_npr[0] = _99
                _100 = python[0]
                _pc = 40 if _100 != 0 else 41
                continue
            case 40:  # <D.20719>
                _101 = iseasnpy[0]
                card2_iseasn[0] = _101
                card2_ihaze[0] = ihaze
                card2_ivulcn[0] = 0
                card2_icstl[0] = 0
                card2_icld[0] = 0
                card2_ivsa[0] = 0
                card2_vis[0] = visibility_km
                card2_wss[0] = 0.0
                card2_whh[0] = 0.0
                card2_rainrt[0] = 0.0
                gndalt[0] = 0.0
                _pc = 42
                continue
            case 41:  # <D.20720>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 42
            case 42:  # __label_001199
                gndalt_823_102 = gndalt[0]
                _pc = 43 if gndalt_823_102 >= 6.0e+0 else 44
                continue
            case 43:  # <D.20722>
                gndalt[0] = 0.0
                _pc = 44
                continue
            case 44:  # __label_001202
                _103 = card2_vis[0]
                _104 = _103 <= 0.0
                _105 = card2_ihaze[0]
                _106 = _105 > 0
                _107 = _104 & _106
                _pc = 45 if _107 != 0 else 46
                continue
            case 45:  # <D.20725>
                _108 = card2_ihaze[0]
                _109 = _int(_108)
                _110 = _109 + -1
                _111 = vsbd_vsb[_110]
                card2_vis[0] = _111
                _pc = 46
                continue
            case 46:  # L.1400
                mart_rhh[0] = 0.0
                _112 = card1_model[0]
                _113 = _112 == 0
                _114 = card1_model[0]
                _115 = _114 == 7
                _116 = _113 | _115
                _pc = 47 if _116 != 0 else 48
                continue
            case 47:  # <D.20728>
                _pc = 55
                continue
            case 48:  # L.1401
                _117 = card1_model[0]
                _118 = _117 == 3
                _119 = card1_model[0]
                _120 = _119 == 5
                _121 = _118 | _120
                _122 = card2_iseasn[0]
                _123 = _122 == 0
                _124 = _121 & _123
                _pc = 49 if _124 != 0 else 50
                continue
            case 49:  # <D.20730>
                card2_iseasn[0] = 2
                _pc = 50
                continue
            case 50:  # L.1402
                _125 = card2_ivsa[0]
                _pc = 51 if _125 == 1 else 54
                continue
            case 51:  # <D.20733>
                _126 = card2_ihaze[0]
                _pc = 52 if _126 == 3 else 53
                continue
            case 52:  # <D.20735>
                _ft_marine(_state, card2_vis, card1_model, card2_wss, card2_whh, card2_icstl, __BLNK___extc, __BLNK___absc, C_17429)
                _pc = 53
                continue
            case 53:  # L.1404
                _pc = 54
                continue
            case 54:  # L.1403
                _127 = card2_ihaze[0]
                __BLNK___ich[0] = _127
                __BLNK___ich[1] = 6
                _128 = card2_ivulcn[0]
                _129 = _128 + 9
                __BLNK___ich[2] = _129
                _pc = 55
            case 55:  # __label_000205
                _130 = card2_rainrt[0]
                _pc = 56 if _130 == 0.0 else 57
                continue
            case 56:  # <D.20739>
                _pc = 57
                continue
            case 57:  # __label_000210
                __BLNK___ich[3] = 18
                _131 = __BLNK___ich[0]
                _pc = 58 if _131 <= 0 else 59
                continue
            case 58:  # <D.20741>
                __BLNK___ich[0] = 1
                _pc = 59
                continue
            case 59:  # L.1406
                _132 = __BLNK___ich[2]
                _pc = 60 if _132 <= 9 else 61
                continue
            case 60:  # <D.20744>
                __BLNK___ich[2] = 10
                _pc = 61
                continue
            case 61:  # L.1407
                _133 = card2_icld[0]
                _134 = _133 > 0
                _135 = card2_icld[0]
                _136 = _135 <= 11
                _137 = _134 & _136
                _pc = 62 if _137 != 0 else 63
                continue
            case 62:  # <D.20747>
                _138 = __BLNK___ich[2]
                __BLNK___ich[3] = _138
                _139 = __BLNK___ich[1]
                __BLNK___ich[2] = _139
                _140 = card2_icld[0]
                __BLNK___ich[1] = _140
                _pc = 63
                continue
            case 63:  # L.1408
                iflga = _int(0)
                iflgt = _int(0)
                card2a_cthik[0] = -9.9e+1
                card2a_calt[0] = -9.9e+1
                card2a_cext[0] = -9.9e+1
                iseed[0] = -99
                _141 = card2_icld[0]
                _pc = 64 if _141 <= 17 else 65
                continue
            case 64:  # <D.20750>
                _pc = 67
                continue
            case 65:  # L.1409
                _142 = python[0]
                _143 = not _142
                _pc = 66 if _143 != 0 else 67
                continue
            case 66:  # <D.20752>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 67
            case 67:  # __label_000230
                zcvsa[0] = -9.9e+1
                ztvsa[0] = -9.9e+1
                zinvsa[0] = -9.9e+1
                _144 = card2_ivsa[0]
                _pc = 68 if _144 == 0 else 69
                continue
            case 68:  # <D.20754>
                _pc = 72
                continue
            case 69:  # L.1411
                _145 = python[0]
                _146 = not _145
                _pc = 70 if _146 != 0 else 71
                continue
            case 70:  # <D.20756>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 71
            case 71:  # __label_001231
                _ft_vsa(_state, card2_ihaze, card2_vis, zcvsa, ztvsa, zinvsa, zvsaly_zvsa, zvsaly_rhvsa, zvsaly_ahvsa, zvsaly_ihvsa)
                _pc = 72
            case 72:  # __label_000240
                _147 = card1_model[0]
                _148 = _147 != 0
                _149 = card1_model[0]
                _150 = _149 != 7
                _151 = _148 & _150
                _pc = 73 if _151 != 0 else 74
                continue
            case 73:  # <D.20758>
                _152 = cntrl_nl[0]
                cntrl_ml[0] = _152
                _pc = 74
                continue
            case 74:  # L.1413
                mdels = _int(card1_model[0])
                i = _int(1)
                _pc = 75
            case 75:  # <D.20761>
                D_17449 = _int(i > 5)
                _pc = 81 if D_17449 != 0 else 76
                continue
            case 76:  # <D.20762>
                _pc = 77 if mdels != 0 else 78
                continue
            case 77:  # <D.20763>
                _153 = _int(mdels)
                _154 = _153 * 5
                _155 = _int(i)
                _156 = _154 + _155
                _157 = _156 + -6
                _158 = titl_hmodel[_157:]
                _159 = _int(i)
                _160 = _159 + 29
                _161 = titl_hmodel[_160:]
                __builtin_memmove(_161, _158, 4)
                _pc = 78
                continue
            case 78:  # __label_000250
                _pc = 79 if mdels == 0 else 80
                continue
            case 79:  # <D.20766>
                _162 = _int(i)
                _163 = _162 + 34
                _164 = titl_hmodel[_163:]
                _165 = _int(i)
                _166 = _165 + 29
                _167 = titl_hmodel[_166:]
                __builtin_memmove(_167, _164, 4)
                _pc = 80
                continue
            case 80:  # L.1414
                i = _int(i + 1)
                _pc = 75
                continue
            case 81:  # L.1415
                _168 = card1_im[0]
                _pc = 82 if _168 == 1 else 102
                continue
            case 82:  # <D.20769>
                _169 = card1_model[0]
                _170 = _169 == 7
                _171 = card1_im[0]
                _172 = _171 == 1
                _173 = _170 & _172
                _174 = card1_model[0]
                _175 = _174 == 0
                _176 = _173 | _175
                _pc = 83 if _176 != 0 else 101
                continue
            case 83:  # <D.20771>
                _177 = python[0]
                _pc = 84 if _177 != 0 else 97
                continue
            case 84:  # <D.20773>
                _178 = mlpy[0]
                cntrl_ml[0] = _178
                _179 = ird1py[0]
                card1a_ird1[0] = _179
                card1a_ird2[0] = 0
                D_17456 = _int(cntrl_ml[0])
                ipy2 = _int(1)
                _pc = 85
            case 85:  # <D.20775>
                D_17459 = _int(ipy2 > D_17456)
                _pc = 88 if D_17459 != 0 else 86
                continue
            case 86:  # <D.20776>
                _180 = _int(ipy2)
                _181 = _180 + -1
                _182 = _int(ipy2)
                _183 = _182 + -1
                _184 = zmdlpy[_181]
                model_zm[_183] = _184
                _185 = _int(ipy2)
                _186 = _185 + -1
                _187 = _int(ipy2)
                _188 = _187 + -1
                _189 = ppy[_186]
                mdata_p[_188] = _189
                _190 = _int(ipy2)
                _191 = _190 + -1
                _192 = _int(ipy2)
                _193 = _192 + -1
                _194 = tpy[_191]
                mdata_t[_193] = _194
                _pc = 87
            case 87:  # L.1421
                ipy2 = _int(ipy2 + 1)
                _pc = 85
                continue
            case 88:  # L.1422
                card1b_junit[0] = 10
                card1b_junit[1] = 10
                card1b_junit[2] = 17
                ipy2 = _int(4)
                _pc = 89
            case 89:  # <D.20777>
                D_17462 = _int(ipy2 > 15)
                _pc = 92 if D_17462 != 0 else 90
                continue
            case 90:  # <D.20778>
                _195 = _int(ipy2)
                _196 = _195 + -1
                card1b_junit[_196] = 14
                _pc = 91
            case 91:  # L.1423
                ipy2 = _int(ipy2 + 1)
                _pc = 89
                continue
            case 92:  # L.1424
                ipy2 = _int(1)
                _pc = 93
            case 93:  # <D.20779>
                D_17465 = _int(ipy2 > 12)
                _pc = 96 if D_17465 != 0 else 94
                continue
            case 94:  # <D.20780>
                _197 = _int(ipy2)
                _198 = _197 + -1
                _199 = _int(ipy2)
                _200 = _199 + -1
                _201 = wmolpy[_198]
                card1b_wmol[_200] = _201
                _pc = 95
            case 95:  # L.1425
                ipy2 = _int(ipy2 + 1)
                _pc = 93
                continue
            case 96:  # L.1426
                _pc = 98
                continue
            case 97:  # <D.20774>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 98
            case 98:  # __label_001250
                _202 = card2_ivsa[0]
                _pc = 99 if _202 == 1 else 100
                continue
            case 99:  # <D.20782>
                _ft_rdnsm(_state, python)
                _pc = 100
                continue
            case 100:  # __label_001251
                _pc = 101
                continue
            case 101:  # L.1419
                _pc = 102
                continue
            case 102:  # L.1418
                cntrl_m[0] = 7
                _ft_aernsm(_state, jprt, gndalt, python)
                _203 = card2_icld[0]
                _pc = 103 if _203 <= 19 else 104
                continue
            case 103:  # <D.20787>
                _pc = 113
                continue
            case 104:  # L.1428
                _204 = card2a_cthik[0]
                _pc = 105 if _204 != 0.0 else 106
                continue
            case 105:  # <D.20789>
                iflgt = _int(1)
                _pc = 106
                continue
            case 106:  # L.1429
                _205 = card2a_calt[0]
                _pc = 107 if _205 != 0.0 else 108
                continue
            case 107:  # <D.20792>
                iflga = _int(1)
                _pc = 108
                continue
            case 108:  # L.1430
                iseed_824_206 = iseed[0]
                _pc = 109 if iseed_824_206 == 0 else 110
                continue
            case 109:  # <D.20795>
                iflgt = _int(2)
                _pc = 110
                continue
            case 110:  # L.1431
                iseed_825_207 = iseed[0]
                _pc = 111 if iseed_825_207 == 0 else 112
                continue
            case 111:  # <D.20798>
                iflga = _int(2)
                _pc = 112
                continue
            case 112:  # L.1432
                _ft_cirrus(_state, card2a_cthik, card2a_calt, iseed, cprob, card2a_cext)
                _pc = 113
            case 113:  # __label_000260
                _208 = card2_ihaze[0]
                _209 = _208 == 7
                _210 = card2_icld[0]
                _211 = _210 == 11
                _212 = _209 | _211
                _pc = 114 if _212 != 0 else 115
                continue
            case 114:  # <D.20801>
                _ft_rdexa(_state, python)
                _pc = 115
                continue
            case 115:  # __label_000300
                iparm[0] = -99
                iph[0] = -99
                iday[0] = -99
                isourc[0] = -99
                parm1[0] = -9.9e+1
                parm2[0] = -9.9e+1
                parm3[0] = -9.9e+1
                parm4[0] = -9.9e+1
                time[0] = -9.9e+1
                psipo[0] = -9.9e+1
                anglem[0] = -9.9e+1
                g[0] = -9.9e+1
                _213 = python[0]
                _pc = 116 if _213 != 0 else 117
                continue
            case 116:  # <D.20804>
                _214 = h1py[0]
                card3_h1[0] = _214
                _215 = h2py[0]
                card3_h2[0] = _215
                _216 = anglepy[0]
                card3_angle[0] = _216
                _217 = rangepy[0]
                card3_range[0] = _217
                card3_beta[0] = 0.0
                ro = _f32(0.0)
                card3_len[0] = 0
                _pc = 117
                continue
            case 117:  # L.1434
                _218 = card1_iemsct[0]
                _pc = 118 if _218 == 3 else 119
                continue
            case 118:  # <D.20807>
                _pc = 122
                continue
            case 119:  # L.1435
                _219 = python[0]
                _220 = not _219
                _pc = 120 if _220 != 0 else 121
                continue
            case 120:  # <D.20809>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 121
            case 121:  # __label_001313
                _pc = 125
                continue
            case 122:  # __label_000315
                _221 = python[0]
                _222 = not _221
                _pc = 123 if _222 != 0 else 124
                continue
            case 123:  # <D.20811>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 124
            case 124:  # __label_001317
                card1_itype[0] = 3
                card3_range[0] = 0.0
                card3_beta[0] = 0.0
                card3_len[0] = 0
                _pc = 125
            case 125:  # __label_000320
                card3_re[0] = 6.37122998046875e+3
                _223 = model_zm[0]
                _224 = card3_h1[0]
                _pc = 126 if _223 > _224 else 127
                continue
            case 126:  # __label_000905
                _225 = model_zm[0]
                card3_h1[0] = _225
                _pc = 127
                continue
            case 127:  # L.1438
                h1s = _f32(card3_h1[0])
                h2s = _f32(card3_h2[0])
                angles = _f32(card3_angle[0])
                rangs = _f32(card3_range[0])
                betas = _f32(card3_beta[0])
                itypes = _int(card1_itype[0])
                lens = _int(card3_len[0])
                _226 = card1_model[0]
                _pc = 128 if _226 == 0 else 129
                continue
            case 128:  # <D.20816>
                ro = _f32(card3_re[0])
                _pc = 129
                continue
            case 129:  # L.1439
                _227 = card1_model[0]
                _pc = 130 if _227 == 1 else 131
                continue
            case 130:  # <D.20819>
                card3_re[0] = 6.37839013671875e+3
                _pc = 131
                continue
            case 131:  # L.1440
                _228 = card1_model[0]
                _pc = 132 if _228 == 4 else 133
                continue
            case 132:  # <D.20822>
                card3_re[0] = 6.35691015625e+3
                _pc = 133
                continue
            case 133:  # L.1441
                _229 = card1_model[0]
                _pc = 134 if _229 == 5 else 135
                continue
            case 134:  # <D.20825>
                card3_re[0] = 6.35691015625e+3
                _pc = 135
                continue
            case 135:  # L.1442
                _pc = 136 if ro > 0.0 else 137
                continue
            case 136:  # <D.20828>
                card3_re[0] = ro
                _pc = 137
                continue
            case 137:  # L.1443
                _230 = card1_iemsct[0]
                _pc = 138 if _230 != 2 else 139
                continue
            case 138:  # <D.20831>
                _pc = 157
                continue
            case 139:  # L.1444
                _231 = python[0]
                _232 = not _231
                _pc = 140 if _232 != 0 else 141
                continue
            case 140:  # <D.20833>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 141
            case 141:  # L.1445
                _233 = python[0]
                _pc = 142 if _233 != 0 else 143
                continue
            case 142:  # <D.20835>
                iph[0] = 2
                _pc = 143
                continue
            case 143:  # __label_001321
                _234 = python[0]
                _235 = not _234
                _pc = 144 if _235 != 0 else 145
                continue
            case 144:  # <D.20838>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 145
            case 145:  # __label_001323
                iph_826_236 = iph[0]
                _pc = 146 if iph_826_236 == 0 else 151
                continue
            case 146:  # <D.20840>
                g_827_237 = g[0]
                _pc = 147 if g_827_237 >= 1.0e+0 else 148
                continue
            case 147:  # <D.20842>
                g[0] = 9.9989998340606689453125e-1
                _pc = 148
                continue
            case 148:  # L.1449
                g_828_238 = g[0]
                _pc = 149 if g_828_238 <= -1.0e+0 else 150
                continue
            case 149:  # <D.20845>
                g[0] = -9.9989998340606689453125e-1
                _pc = 150
                continue
            case 150:  # L.1450
                _pc = 151
                continue
            case 151:  # L.1448
                iph_829_239 = iph[0]
                _pc = 152 if iph_829_239 != 1 else 153
                continue
            case 152:  # <D.20849>
                _pc = 157
                continue
            case 153:  # L.1451
                _240 = python[0]
                _241 = not _240
                _pc = 154 if _241 != 0 else 155
                continue
            case 154:  # <D.20851>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 155
            case 155:  # __label_001327
                _242 = python[0]
                _243 = not _242
                _pc = 156 if _243 != 0 else 157
                continue
            case 156:  # <D.20853>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 157
            case 157:  # __label_000330
                irpt_830_244 = irpt[0]
                _pc = 158 if irpt_830_244 == 3 else 159
                continue
            case 158:  # <D.20855>
                _pc = 168
                continue
            case 159:  # __label_000400
                _245 = python[0]
                _pc = 160 if _245 != 0 else 161
                continue
            case 160:  # <D.20857>
                _246 = v1py[0]
                card4_v1[0] = _246
                _247 = v2py[0]
                card4_v2[0] = _247
                _248 = dvpy[0]
                card4_dv[0] = _248
                _pc = 162
                continue
            case 161:  # <D.20858>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 162
            case 162:  # __label_001401
                _249 = card2_ihaze[0]
                _pc = 163 if _249 == 3 else 166
                continue
            case 163:  # <D.20860>
                _250 = card4_v1[0]
                _251 = _250 < 2.5e+2
                _252 = card4_v2[0]
                _253 = _252 < 2.5e+2
                _254 = _251 | _253
                _pc = 164 if _254 != 0 else 165
                continue
            case 164:  # <D.20862>
                card2_ihaze[0] = 4
                _pc = 165
                continue
            case 165:  # __label_001203
                _pc = 166
                continue
            case 166:  # L.1456
                irpt_831_255 = irpt[0]
                _pc = 167 if irpt_831_255 == 4 else 168
                continue
            case 167:  # <D.20866>
                _pc = 266
                continue
            case 168:  # __label_000500
                irpt_832_256 = irpt[0]
                _pc = 169 if irpt_832_256 == 3 else 170
                continue
            case 169:  # <D.20868>
                _pc = 210
                continue
            case 170:  # __label_001204
                _257 = cntrl_imult[0]
                _pc = 171 if _257 == 1 else 174
                continue
            case 171:  # <D.20870>
                _258 = card1_iemsct[0]
                _259 = _258 == 0
                _260 = card1_iemsct[0]
                _261 = _260 == 3
                _262 = _259 | _261
                _pc = 172 if _262 != 0 else 173
                continue
            case 172:  # __label_001411
                cntrl_imult[0] = 0
                _pc = 173
                continue
            case 173:  # L.1461
                _pc = 174
                continue
            case 174:  # L.1460
                mdel = _int(card1_model[0])
                _pc = 175 if mdel == 0 else 176
                continue
            case 175:  # <D.20876>
                mdel = _int(8)
                _pc = 176
                continue
            case 176:  # L.1462
                mm1 = _int(mdel)
                mm2 = _int(mdel)
                mm3 = _int(mdel)
                _263 = card1_m1[0]
                _pc = 177 if _263 != 0 else 178
                continue
            case 177:  # <D.20879>
                mm1 = _int(card1_m1[0])
                _pc = 178
                continue
            case 178:  # L.1463
                _264 = card1_m2[0]
                _pc = 179 if _264 != 0 else 180
                continue
            case 179:  # <D.20882>
                mm2 = _int(card1_m2[0])
                _pc = 180
                continue
            case 180:  # L.1464
                _265 = card1_m3[0]
                _pc = 181 if _265 != 0 else 182
                continue
            case 181:  # <D.20885>
                mm3 = _int(card1_m3[0])
                _pc = 182
                continue
            case 182:  # L.1465
                _266 = card1_model[0]
                _pc = 183 if _266 == 0 else 184
                continue
            case 183:  # <D.20888>
                _pc = 184
                continue
            case 184:  # __label_000510
                jprt_833_267 = jprt[0]
                _pc = 185 if jprt_833_267 == 0 else 186
                continue
            case 185:  # <D.20890>
                _pc = 200
                continue
            case 186:  # L.1467
                _268 = card2_iseasn[0]
                _pc = 187 if _268 == 0 else 188
                continue
            case 187:  # <D.20892>
                card2_iseasn[0] = 1
                _pc = 188
                continue
            case 188:  # L.1468
                _269 = card2_ivulcn[0]
                _pc = 189 if _269 <= 0 else 190
                continue
            case 189:  # <D.20895>
                card2_ivulcn[0] = 1
                _pc = 190
                continue
            case 190:  # L.1469
                _270 = card2_ivulcn[0]
                ihvul = _int(_270 + 10)
                _271 = card2_ivulcn[0]
                _pc = 191 if _271 == 6 else 192
                continue
            case 191:  # <D.20898>
                ihvul = _int(11)
                _pc = 192
                continue
            case 192:  # L.1470
                _272 = card2_ivulcn[0]
                _pc = 193 if _272 == 7 else 194
                continue
            case 193:  # <D.20901>
                ihvul = _int(11)
                _pc = 194
                continue
            case 194:  # L.1471
                _273 = card2_ivulcn[0]
                _pc = 195 if _273 == 8 else 196
                continue
            case 195:  # <D.20904>
                ihvul = _int(13)
                _pc = 196
                continue
            case 196:  # L.1472
                ihmet = _int(1)
                _274 = card2_ivulcn[0]
                _pc = 197 if _274 > 1 else 198
                continue
            case 197:  # <D.20907>
                ihmet = _int(2)
                _pc = 198
                continue
            case 198:  # L.1473
                _275 = card2_ihaze[0]
                _pc = 199 if _275 == 0 else 200
                continue
            case 199:  # <D.20910>
                _pc = 200
                continue
            case 200:  # __label_001517
                _276 = card1_iemsct[0]
                _pc = 201 if _276 != 2 else 202
                continue
            case 201:  # <D.20912>
                _pc = 204
                continue
            case 202:  # L.1475
                iparm_834_277 = iparm[0]
                _pc = 203 if iparm_834_277 == 1 else 204
                continue
            case 203:  # <D.20914>
                _ft_subsol(_state, parm3, parm4, time, iday)
                _pc = 204
                continue
            case 204:  # __label_000550
                _278 = card4_v1[0]
                _279 = _div(_278, 5.0e+0)
                _280 = _279 + 1.00000001490116119384765625e-1
                _281 = _int(_280)
                _282 = _f32(_281)
                _283 = _282 * 5.0e+0
                card4_v1[0] = _283
                _284 = card4_v2[0]
                _285 = _div(_284, 5.0e+0)
                _286 = _285 + 1.00000001490116119384765625e-1
                _287 = _int(_286)
                _288 = _f32(_287)
                _289 = _288 * 5.0e+0
                card4_v2[0] = _289
                alam1 = _f32(9.99999765625e+4)
                _290 = card4_v1[0]
                _pc = 205 if _290 > 0.0 else 206
                continue
            case 205:  # <D.20917>
                _291 = card4_v1[0]
                alam1 = _f32(_div(1.0e+4, _291))
                _pc = 206
                continue
            case 206:  # L.1477
                _292 = card4_v2[0]
                alam2 = _f32(_div(1.0e+4, _292))
                _293 = card4_dv[0]
                _pc = 207 if _293 < 5.0e+0 else 208
                continue
            case 207:  # <D.20920>
                card4_dv[0] = 5.0e+0
                _pc = 208
                continue
            case 208:  # L.1478
                _294 = card4_dv[0]
                _295 = _div(_294, 5.0e+0)
                _296 = _295 + 1.00000001490116119384765625e-1
                _297 = _int(_296)
                _298 = _f32(_297)
                _299 = _298 * 5.0e+0
                card4_dv[0] = _299
                _pc = 209
            case 209:  # __label_001555
                _ft_stdmdl(_state)
                _pc = 210
            case 210:  # __label_000555
                i = _int(1)
                _pc = 211
            case 211:  # <D.20923>
                D_17577 = _int(i > 68)
                _pc = 217 if D_17577 != 0 else 212
                continue
            case 212:  # <D.20924>
                D_17578 = _int(cntrl_kmax[0])
                j = _int(1)
                _pc = 213
            case 213:  # <D.20925>
                D_17581 = _int(j > D_17578)
                _pc = 216 if D_17581 != 0 else 214
                continue
            case 214:  # <D.20926>
                _300 = _int(j)
                _301 = _300 * 68
                _302 = _int(i)
                _303 = _301 + _302
                _304 = _303 + -69
                __BLNK___wpath[_304] = 0.0
                _305 = _int(j)
                _306 = _305 * 68
                _307 = _int(i)
                _308 = _306 + _307
                _309 = _308 + -69
                sols_wpaths[_309] = 0.0
                _pc = 215
            case 215:  # L.1481
                j = _int(j + 1)
                _pc = 213
                continue
            case 216:  # L.1479
                i = _int(i + 1)
                _pc = 211
                continue
            case 217:  # L.1480
                path_itest[0] = 0
                _310 = cntrl_imult[0]
                _pc = 218 if _310 == 1 else 240
                continue
            case 218:  # <D.20927>
                _311 = model_zm[0]
                card3_h1[0] = _311
                _312 = cntrl_ml[0]
                _313 = _int(_312)
                _314 = _313 + -1
                _315 = model_zm[_314]
                card3_h2[0] = _315
                card1_itype[0] = 2
                card3_angle[0] = 0.0
                card3_beta[0] = 0.0
                card3_range[0] = 0.0
                issgs = _int(cntrl_issgeo[0])
                cntrl_issgeo[0] = 0
                _ft_geo(_state, ierror, bendng, maxgeo)
                w15sv = _f32(__BLNK___w[14])
                cntrl_issgeo[0] = issgs
                _316 = cntrl_ikmax[0]
                mnlt_imsmx[0] = _316
                D_17585 = _int(mnlt_imsmx[0])
                n = _int(1)
                _pc = 219
            case 219:  # <D.20929>
                D_17588 = _int(n > D_17585)
                _pc = 225 if D_17588 != 0 else 220
                continue
            case 220:  # <D.20930>
                _317 = _int(n)
                _318 = _317 + -1
                _319 = _int(n)
                _320 = _319 + -1
                _321 = __BLNK___tbby[_318]
                mnlt_tbbms[_320] = _321
                _322 = _int(n)
                _323 = _322 + -1
                _324 = _int(n)
                _325 = _324 + -1
                _326 = path_pl[_323]
                plst[_325] = _326
                D_17589 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 221
            case 221:  # <D.20931>
                D_17592 = _int(k > D_17589)
                _pc = 224 if D_17592 != 0 else 222
                continue
            case 222:  # __label_000035
                _327 = _int(k)
                _328 = _327 * 68
                _329 = _int(n)
                _330 = _328 + _329
                _331 = _330 + -69
                _332 = _int(k)
                _333 = _332 * 34
                _334 = _int(n)
                _335 = _333 + _334
                _336 = _335 + -35
                _337 = __BLNK___wpath[_331]
                mnlt_wpms[_336] = _337
                _pc = 223
            case 223:  # L.1486
                k = _int(k + 1)
                _pc = 221
                continue
            case 224:  # L.1484
                n = _int(n + 1)
                _pc = 219
                continue
            case 225:  # L.1485
                _338 = card1_iemsct[0]
                _pc = 226 if _338 == 2 else 239
                continue
            case 226:  # <D.20933>
                _ft_ssgeo(_state, ierror, iph, iparm, parm1, parm2, parm3, parm4, psipo, g, maxgeo)
                D_17595 = _int(cntrl_ikmax[0])
                n = _int(1)
                _pc = 227
            case 227:  # <D.20935>
                D_17598 = _int(n > D_17595)
                _pc = 231 if D_17598 != 0 else 228
                continue
            case 228:  # <D.20936>
                _339 = _int(n)
                _340 = _339 + -1
                _341 = sols_cszen[_340]
                _342 = _int(n)
                _343 = _342 + -1
                _344 = abs(_341)
                csensv[_343] = _344
                _345 = _int(n)
                _346 = _345 + -1
                _347 = csensv[_346]
                _pc = 229 if _347 < 1.74000002443790435791015625e-2 else 230
                continue
            case 229:  # <D.20937>
                _348 = _int(n)
                _349 = _348 + -1
                csensv[_349] = 1.74000002443790435791015625e-2
                _pc = 230
                continue
            case 230:  # L.1489
                n = _int(n + 1)
                _pc = 227
                continue
            case 231:  # L.1490
                D_17601 = _int(cntrl_ml[0])
                n = _int(1)
                _pc = 232
            case 232:  # <D.20940>
                D_17604 = _int(n > D_17601)
                _pc = 238 if D_17604 != 0 else 233
                continue
            case 233:  # <D.20941>
                D_17605 = _int(cntrl_kmax[0])
                k = _int(1)
                _pc = 234
            case 234:  # <D.20942>
                D_17608 = _int(k > D_17605)
                _pc = 237 if D_17608 != 0 else 235
                continue
            case 235:  # <D.20943>
                _350 = _int(k)
                _351 = _350 * 68
                _352 = _int(n)
                _353 = _351 + _352
                _354 = _353 + -69
                _355 = _int(k)
                _356 = _355 * 34
                _357 = _int(n)
                _358 = _356 + _357
                _359 = _358 + -35
                _360 = sols_wpaths[_354]
                mnlt_wpmss[_359] = _360
                _pc = 236
            case 236:  # L.1494
                k = _int(k + 1)
                _pc = 234
                continue
            case 237:  # L.1492
                n = _int(n + 1)
                _pc = 232
                continue
            case 238:  # L.1493
                _pc = 239
                continue
            case 239:  # L.1488
                _pc = 240
                continue
            case 240:  # L.1483
                card3_h1[0] = h1s
                card3_h2[0] = h2s
                card3_angle[0] = angles
                card3_range[0] = rangs
                card3_beta[0] = betas
                card1_itype[0] = itypes
                card3_len[0] = lens
                cntrl_issgeo[0] = 0
                _ft_geo(_state, ierror, bendng, maxgeo)
                _ft_aertmp(_state)
                _361 = cntrl_imult[0]
                _pc = 241 if _361 != 1 else 242
                continue
            case 241:  # <D.20946>
                w15sv = _f32(__BLNK___w[14])
                _pc = 242
                continue
            case 242:  # L.1496
                _362 = cntrl_imult[0]
                _pc = 243 if _362 == 1 else 248
                continue
            case 243:  # __label_001900
                D_17613 = _int(cntrl_ikmax[0])
                n = _int(1)
                _pc = 244
            case 244:  # <D.20951>
                D_17616 = _int(n > D_17613)
                _pc = 247 if D_17616 != 0 else 245
                continue
            case 245:  # <D.20952>
                _363 = _int(n)
                _364 = _363 + -1
                _365 = _int(n)
                _366 = _365 + -1
                _367 = __BLNK___tbby[_364]
                mnlt_tbbss[_366] = _367
                _368 = _int(n)
                _369 = _368 + -1
                _370 = _int(n)
                _371 = _370 + -1
                _372 = path_qtheta[_369]
                qthets[_371] = _372
                _pc = 246
            case 246:  # L.1498
                n = _int(n + 1)
                _pc = 244
                continue
            case 247:  # L.1499
                _pc = 248
                continue
            case 248:  # L.1497
                ierror_835_373 = ierror[0]
                _pc = 249 if ierror_835_373 > 0 else 250
                continue
            case 249:  # <D.20954>
                _pc = 272
                continue
            case 250:  # L.1500
                _374 = card1_iemsct[0]
                _375 = _374 == 3
                ierror_836_376 = ierror[0]
                _377 = ierror_836_376 == -5
                _378 = _375 & _377
                _pc = 251 if _378 != 0 else 252
                continue
            case 251:  # <D.20956>
                _pc = 253
                continue
            case 252:  # L.1501
                _pc = 254
                continue
            case 253:  # __label_001557
                _pc = 272
                continue
            case 254:  # __label_000558
                _379 = card1_iemsct[0]
                _pc = 255 if _379 == 2 else 256
                continue
            case 255:  # <D.20958>
                _ft_ssgeo(_state, ierror, iph, iparm, parm1, parm2, parm3, parm4, psipo, g, maxgeo)
                _pc = 256
                continue
            case 256:  # L.1502
                __BLNK___w[14] = w15sv
                ierror_837_380 = ierror[0]
                _pc = 257 if ierror_837_380 > 0 else 258
                continue
            case 257:  # <D.20961>
                _pc = 272
                continue
            case 258:  # L.1503
                _381 = cntrl_imult[0]
                _pc = 259 if _381 == 1 else 265
                continue
            case 259:  # <D.20963>
                D_17628 = _int(mnlt_imsmx[0])
                ik = _int(1)
                _pc = 260
            case 260:  # <D.20965>
                D_17631 = _int(ik > D_17628)
                _pc = 264 if D_17631 != 0 else 261
                continue
            case 261:  # <D.20966>
                _382 = _int(ik)
                _383 = _382 + -1
                _384 = _int(ik)
                _385 = _384 + -1
                _386 = qthets[_383]
                path_qtheta[_385] = _386
                _387 = _int(ik)
                _388 = _387 + -1
                _389 = _int(ik)
                _390 = _389 + -1
                _391 = plst[_388]
                path_pl[_390] = _391
                _392 = card1_iemsct[0]
                _pc = 262 if _392 == 2 else 263
                continue
            case 262:  # <D.20967>
                _393 = _int(ik)
                _394 = _393 + -1
                _395 = _int(ik)
                _396 = _395 + -1
                _397 = csensv[_394]
                sols_cszen[_396] = _397
                _pc = 263
                continue
            case 263:  # L.1505
                ik = _int(ik + 1)
                _pc = 260
                continue
            case 264:  # L.1506
                _pc = 265
                continue
            case 265:  # L.1504
                _ft_exabin(_state)
                _pc = 266
            case 266:  # __label_001255
                _398 = card3_range[0]
                mdlz_hmdlz[7] = _398
                _pc = 267
            case 267:  # __label_001560
                _399 = python[0]
                _400 = not _399
                _pc = 268 if _400 != 0 else 269
                continue
            case 268:  # <D.20971>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 269
            case 269:  # __label_001600
                irain = _int(0)
                _401 = card2_rainrt[0]
                _pc = 270 if _401 > 0.0 else 271
                continue
            case 270:  # <D.20973>
                irain = _int(1)
                _pc = 271
                continue
            case 271:  # L.1509
                _ft_equlwc(_state)
                _ft_trans(_state, iph, isourc, iday, anglem, nwl, txpy, vpy, alampy, tracepy, unifpy, sumapy, irradpy, sumvvpy)
                _pc = 272
            case 272:  # __label_000630
                ierror_838_402 = ierror[0]
                _pc = 273 if ierror_838_402 > 0 else 276
                continue
            case 273:  # <D.20976>
                _403 = python[0]
                _404 = not _403
                _pc = 274 if _404 != 0 else 275
                continue
            case 274:  # <D.20978>
                _gfortran_stop_string(b"TAPE5 input is outside the Python API", 37, 0)
                _pc = 275
            case 275:  # L.1511
                _pc = 276
                continue
            case 276:  # __label_001630
                irpt_839_405 = irpt[0]
                _pc = 277 if irpt_839_405 == 0 else 278
                continue
            case 277:  # <D.20981>
                _pc = 293
                continue
            case 278:  # L.1512
                irpt_840_406 = irpt[0]
                _pc = 279 if irpt_840_406 == 4 else 280
                continue
            case 279:  # <D.20983>
                _pc = 159
                continue
            case 280:  # L.1513
                irpt_841_407 = irpt[0]
                _408 = irpt_841_407 > 1
                _409 = card1_iemsct[0]
                _410 = _409 > 1
                _411 = _408 & _410
                _pc = 281 if _411 != 0 else 282
                continue
            case 281:  # <D.20985>
                _gfortran_stop_numeric(-1, 0)
                _pc = 282
            case 282:  # L.1514
                irpt_842_412 = irpt[0]
                _pc = 283 if irpt_842_412 > 4 else 284
                continue
            case 283:  # <D.20987>
                _pc = 293
                continue
            case 284:  # L.1515
                irpt_843_413 = irpt[0]
                _pc = {1: 285, 2: 287, 3: 289, 4: 291}.get(irpt_843_413, 293)
                continue
            case 285:  # L.1518
                _pc = 4
                continue
            case 286:  # continuation_782
                _pc = 293
                continue
            case 287:  # L.1519
                _pc = 293
                continue
            case 288:  # continuation_785
                _pc = 293
                continue
            case 289:  # L.1520
                _pc = 115
                continue
            case 290:  # continuation_788
                _pc = 293
                continue
            case 291:  # L.1521
                _pc = 159
                continue
            case 292:  # continuation_791
                _pc = 293
                continue
            case 293:  # __label_000900
                return
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_raysct(_state, v):
    D_20996 = _ZERO32
    __result_raysct = _ZERO32
    D_17697 = _ZERO32
    D_17698 = _ZERO32
    D_17699 = _ZERO32
    _pc = 0
    while True:
        match _pc:
            case 0:  # entry
                __result_raysct = _f32(0.0)
                _1 = v[0]
                _pc = 1 if _1 <= 3.0e+3 else 2
                continue
            case 1:  # <D.20994>
                D_20996 = _f32(__result_raysct)
                return D_20996
            case 2:  # L.1522
                D_17697 = _f32(v[0])
                D_17698 = _f32(v[0])
                D_17699 = _f32(D_17698 * D_17698)
                _2 = __builtin_powif(D_17697, 3)
                _3 = D_17699 * 1.071230016e+9
                _4 = 9.267990218709925888e+18 - _3
                _5 = _4
                _6 = _div(_2, _5)
                __result_raysct = _f32(_6)
                D_20996 = _f32(__result_raysct)
                return D_20996
            case -1: return
            case _: raise RuntimeError('Invalid LOWTRAN control flow')


def _ft_abslim(_state, tk, awlwc):
    pi = _state.view(182888, '<f4')
    D_20999 = _ZERO32
    efin = _ZERO32
    eqlwc = _ZERO32
    es = _ZERO32
    esmie2 = _ZERO32
    slambd = _ZERO32
    tc = _ZERO32
    __result_abslim = _ZERO32
    D_17711 = _ZERO32
    D_17712 = _ZERO32
    D_17713 = _ZERO32
    D_17714 = _ZERO32
    D_17715 = _ZERO32
    _1 = tk[0]
    tc = _f32(_1 - 2.73149993896484375e+2)
    _2 = tc * 2.164739929139614105224609375e-2
    _3 = _2 + 5.27136993408203125e+0
    _4 = tc * 1.31197995506227016448974609375e-3
    _5 = tc * _4
    efin = _f32(_3 - _5)
    _6 = tc - 2.5e+1
    D_17711 = _f32(_6)
    D_17712 = _f32(D_17711 * D_17711)
    _7 = tc - 2.5e+1
    D_17713 = _f32(_7)
    _8 = tc - 2.5e+1
    _9 = _8
    _10 = _9 * 4.579000174999237060546875e-3
    _11 = 1.0e+0 - _10
    _12 = D_17712 * 1.189999966300092637538909912109375e-5
    _13 = _11 + _12
    _14 = __builtin_powif(D_17713, 3)
    _15 = _14 * 2.80000005403735485742799937725067138671875e-8
    _16 = _13 - _15
    _17 = _16
    es = _f32(_17 * 7.854000091552734375e+1)
    _18 = tk[0]
    _19 = _div(2.51397998046875e+3, _18)
    _20 = __builtin_expf(_19)
    slambd = _f32(_20 * 3.3835999784059822559356689453125e-4)
    _21 = es + 2.0e+0
    D_17714 = _f32(_21)
    D_17715 = _f32(D_17714 * D_17714)
    _22 = es - efin
    _23 = _22
    esmie2 = _f32(_div(_23, D_17715))
    _24 = awlwc[0]
    eqlwc = _f32(_div(_24, 1.0e+1))
    _25 = tk[0]
    _26 = _25 * 6.95100009441375732421875e-1
    _27 = _26 * 3.6e+1
    pi_844_28 = pi[0]
    _29 = _27 * pi_844_28
    _30 = eqlwc * _29
    _31 = slambd * _30
    _32 = esmie2 * _31
    __result_abslim = _f32(_32)
    D_20999 = _f32(__result_abslim)
    return D_20999


