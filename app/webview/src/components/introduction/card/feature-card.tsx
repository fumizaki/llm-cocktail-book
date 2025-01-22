import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { LinkButton } from "@/components/ui/link-button";


type Props = {
	title: string;
	description: string;
	label: string;
	href: string;
	children: React.ReactNode;
}

export const FeatureCard = ({
	title,
	description,
	label,
	href,
	children
}: Props) => {
	return (
		<Card
			className={
				"relative w-96 h-full flex flex-col gap-1.5 py-3.5 pl-3.5 pr-1.5 cursor-pointer overflow-hidden border-blue-800 bg-blue-700/25"
			}
		>
			<CardHeader>
				<CardTitle>
					{title}
				</CardTitle>
				<CardDescription>
					{description}
				</CardDescription>
			</CardHeader>
			<CardContent>
				{children}
			</CardContent>
			<CardFooter>
				<LinkButton href={href} className={"w-full"}>
					{label}
				</LinkButton>
			</CardFooter>
		</Card>
	);
};
