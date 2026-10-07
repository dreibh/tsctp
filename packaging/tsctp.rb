class Tsctp < Formula
  desc "SCTP test tool for functionality and interoperability tests"
  homepage "https://www.nntb.no/~dreibh/tsctp/"
  url "https://www.nntb.no/~dreibh/tsctp/download/tsctp-0.8.7.tar.xz"
  sha256 "607fc96f15bc2bb547f91f70e420f00cd31b0cd226f2870778fc03a997e1ee0f"
  license "BSD-3-Clause"

  depends_on "cmake" => :build
  depends_on :linux

  def install
    system "cmake", "-S", ".", "-B", "build", *std_cmake_args
    system "cmake", "--build", "build"
    system "cmake", "--install", "build"
  end
end
