import { cn } from "@/lib/style";
import { Header } from "@/components/layout/header";
import { Main } from "@/components/layout/main";
import { Footer } from "@/components/layout/footer";

export const Layout = ({
	children,
	className,
}: { children: React.ReactNode; className?: string }) => {
	return (
		<div className={cn("flex flex-col h-screen", className)}>
			<Header className={"flex-none"} />
			<Main className={"grow"}>{children}</Main>
			<Footer className={"flex-none"} />
		</div>
	);
};
