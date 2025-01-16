import type { Metadata } from "next";
import localFont from "next/font/local";
import { ThemeProvider } from "@/hooks/theme-provider";
import { AuthProvider } from "@/hooks/auth-provider";
import { Toaster } from "@/components/ui/toaster";
import { Layout } from "@/components/layout";
import "./globals.css";

const geistSans = localFont({
	src: "./fonts/GeistVF.woff",
	variable: "--font-geist-sans",
	weight: "100 900",
});
const geistMono = localFont({
	src: "./fonts/GeistMonoVF.woff",
	variable: "--font-geist-mono",
	weight: "100 900",
});

export const metadata: Metadata = {
	title: "LLM Cocktail Book",
	description: "This is Fullstack Web Application Using LLM.",
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang="en">
			<body
				className={`${geistSans.variable} ${geistMono.variable} antialiased`}
			>
				<AuthProvider>
					<ThemeProvider
						attribute="class"
						defaultTheme="system"
						enableSystem
						disableTransitionOnChange
					>
						<Toaster />
						<Layout>{children}</Layout>
					</ThemeProvider>
				</AuthProvider>
			</body>
		</html>
	);
}
