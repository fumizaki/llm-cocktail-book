"use client";

import { useSession, signOut } from "next-auth/react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuItem,
	DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import {
	Settings,
	Loader2,
	User2,
	LogOut,
	LogIn,
	UserPlus2,
} from "lucide-react";
import { HeaderTheme } from "./theme";

export const HeaderDropdown = ({}) => {
	const { data: session, status } = useSession();
	const pathname = usePathname();

	return (
		<DropdownMenu>
			<DropdownMenuTrigger asChild>
				<Button variant="outline" size="icon">
					<Settings className={"w-4 h-4 "} />
				</Button>
			</DropdownMenuTrigger>
			{status === "loading" && (
				<DropdownMenuContent align="end" className={"flex flex-col gap-2 p-2"}>
					<Button disabled={true}>
						<Loader2 className="mr-2 h-4 w-4 animate-spin" />
						loading
					</Button>
					<HeaderTheme />
				</DropdownMenuContent>
			)}
			{status === "authenticated" && (
				<DropdownMenuContent align="end" className={"flex flex-col gap-2 p-2"}>
					<DropdownMenuItem className={"w-full"} asChild>
						<Button className={"w-full"} onClick={() => signOut()}>
							<LogOut className={"h-4 w-4 mr-2"} />
							サインアウト
						</Button>
					</DropdownMenuItem>
					<HeaderTheme />
				</DropdownMenuContent>
			)}
			{status === "unauthenticated" && (
				<DropdownMenuContent align="end" className={"flex flex-col gap-2 p-2"}>
					<DropdownMenuItem className={"w-full"} asChild>
						<Link href={`/api/auth/signin?callbackUrl=${pathname}`}>
							<LogIn className={"h-4 w-4 mr-2"} />
							サインイン
						</Link>
					</DropdownMenuItem>
					<DropdownMenuItem className={"w-full"} asChild>
						<Link href={`/auth/signup?callbackUrl=${pathname}`}>
							<UserPlus2 className={"h-4 w-4 mr-2"} />
							サインアップ
						</Link>
					</DropdownMenuItem>
					<HeaderTheme />
				</DropdownMenuContent>
			)}
		</DropdownMenu>
	);
};
