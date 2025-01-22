import { cn } from "@/lib/style";
import { FeatureCard } from "@/components/introduction/card/feature-card";

type Props = {
	className?: string
};

type Feature = {
	title: string;
	description: string;
	content: string;
	label: string;
	href: string
}

export async function FeatureCardList({ className }: Props) {

	const features: Feature[] = [
		{
			title: 'Chatbot',
			description: "Experience next-generation AI conversations.",
			content: "Engage in intelligent and elegant dialogues powered by sophisticated LLM blends. Explore the possibilities of cutting-edge AI interactions.",
			label: "Let's Start",
			href: "/chatbot"
		},
		{
			title: 'Workflow',
			description: "Orchestrate complex AI tasks with workflows.",
			content: "Integrate LLMs and tools to automate complex processes. Create efficient and elegant workflows that streamline your operations.",
			label: "Coming Soon",
			href: "#"
		}
	]

	return (
		<ul
			className={cn("grid grid-cols-1 sm:grid-cols-2 justify-center items-center gap-x-5 gap-y-8", className)}
		>
			{features.map((value: Feature, idx: number) => {
				return (
					<li
						key={idx}
						className={
							"w-full group relative flex justify-center items-center "
						}
					>
						<FeatureCard title={value.title} description={value.description} label={value.label} href={value.href}>
							<p>{value.content}</p>
						</FeatureCard>
					</li>
				);
			})}
		</ul>
	);
}
