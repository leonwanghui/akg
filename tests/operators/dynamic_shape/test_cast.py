import boot
import pytest


@pytest.mark.cast
@pytest.mark.level0
@pytest.mark.env_oncard
@pytest.mark.platform_x86_ascend_training
def test_cast():
    #boot.run("test_resnet50_cast_000", "cast_run", ((64, 128, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_001", "cast_run", ((32, 64, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_002", "cast_run", ((16, 32, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_003", "cast_run", ((4, 16, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_004", "cast_run", ((49, 4, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_005", "cast_run", ((32, 4, 112, 112, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_006", "cast_run", ((32, 4, 56, 56, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_007", "cast_run", ((32, 16, 56, 56, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_008", "cast_run", ((36, 4, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_009", "cast_run", ((4, 4, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_010", "cast_run", ((32, 4, 56, 56, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_011", "cast_run", ((16, 4, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_012", "cast_run", ((32, 16, 56, 56, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_013", "cast_run", ((32, 32, 28, 28, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_014", "cast_run", ((8, 32, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_015", "cast_run", ((72, 8, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_016", "cast_run", ((16, 8, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_017", "cast_run", ((32, 8, 56, 56, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_018", "cast_run", ((32, 8, 56, 56, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_019", "cast_run", ((32, 8, 28, 28, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_020", "cast_run", ((32, 8, 28, 28, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_021", "cast_run", ((32, 8, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_022", "cast_run", ((32, 32, 28, 28, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_023", "cast_run", ((32, 64, 14, 14, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_024", "cast_run", ((16, 64, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_025", "cast_run", ((144, 16, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_026", "cast_run", ((32, 16, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_027", "cast_run", ((32, 16, 28, 28, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_028", "cast_run", ((32, 16, 28, 28, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_029", "cast_run", ((32, 16, 14, 14, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_030", "cast_run", ((32, 16, 14, 14, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_031", "cast_run", ((64, 16, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_032", "cast_run", ((32, 64, 14, 14, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_033", "cast_run", ((32, 128, 7, 7, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_034", "cast_run", ((32, 128, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_035", "cast_run", ((288, 32, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_036", "cast_run", ((64, 32, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_037", "cast_run", ((32, 32, 14, 14, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_038", "cast_run", ((32, 32, 14, 14, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_039", "cast_run", ((32, 32, 7, 7, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_040", "cast_run", ((32, 32, 7, 7, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_041", "cast_run", ((128, 32, 16, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_042", "cast_run", ((32, 128, 7, 7, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_043", "cast_run", ((32, 4, 112, 112, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_044", "cast_run", ((32, 128, 1, 1, 16), "float32", "float16"), "dynamic")
    #boot.run("test_resnet50_cast_045", "cast_run", ((32, 2048, 1, 1), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_048", "cast_run", ((64, 128, 16, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_049", "cast_run", ((32, 64, 16, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_050", "cast_run", ((16, 32, 16, 16), "float16", "float32"), "dynamic")
    #boot.run("test_resnet50_cast_051", "cast_run", ((4, 16, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_052", "cast_run", ((49, 4, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_053", "cast_run", ((36, 4, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_054", "cast_run", ((4, 4, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_055", "cast_run", ((16, 4, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_056", "cast_run", ((8, 32, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_057", "cast_run", ((72, 8, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_058", "cast_run", ((16, 8, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_059", "cast_run", ((32, 8, 56, 56, 16), "float32", "float16"), "dynamic")
    boot.run("test_resnet50_cast_060", "cast_run", ((32, 8, 56, 56, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_061", "cast_run", ((32, 8, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_062", "cast_run", ((16, 64, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_063", "cast_run", ((144, 16, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_064", "cast_run", ((32, 16, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_065", "cast_run", ((32, 16, 28, 28, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_066", "cast_run", ((32, 16, 28, 28, 16), "float32", "float16"), "dynamic")
    boot.run("test_resnet50_cast_067", "cast_run", ((64, 16, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_068", "cast_run", ((32, 128, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_069", "cast_run", ((288, 32, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_070", "cast_run", ((64, 32, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_071", "cast_run", ((32, 32, 14, 14, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_072", "cast_run", ((32, 32, 14, 14, 16), "float32", "float16"), "dynamic")
    boot.run("test_resnet50_cast_073", "cast_run", ((128, 32, 16, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_074", "cast_run", ((32, 2048, 1, 1), "float32", "float16"), "dynamic")
    boot.run("test_resnet50_cast_075", "cast_run", ((32, 128, 1, 1, 16), "float16", "float32"), "dynamic")
    boot.run("test_resnet50_cast_080", "cast_run", ((64, 128, 16, 16), "bool", "int32"), "dynamic")
