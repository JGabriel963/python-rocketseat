import { cn } from "@/lib/utils";
import Image from "next/image";
import { Poppins } from "next/font/google";

const font = Poppins({
  subsets: ["latin"],
  weight: ["400", "600"],
});

export function Logo() {
  return (
    <div className="hidden md:flex items-center gap-x-2">
      <Image src="/logo.svg" height="40" width="40" alt="Logo" />
      <p className={cn("font-semibold", font.className)}>Jotion</p>
    </div>
  );
}
